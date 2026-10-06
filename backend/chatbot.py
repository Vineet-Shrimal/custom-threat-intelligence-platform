"""Read-only natural-language query helper backed by local Ollama.

Defense in depth: SQL is allow-listed/validated here and must also run using
a PostgreSQL role that has SELECT-only permissions.
"""
import os
import re
import requests
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
ALLOWED_TABLES = {"iocs", "ioc_sightings", "ioc_enrichment", "cves", "articles", "apt_groups"}
BLOCKED = re.compile(
    r"\b(insert|update|delete|drop|alter|create|truncate|grant|revoke|copy|"
    r"execute|call|merge|into|pg_sleep|information_schema|pg_catalog)\b",
    re.IGNORECASE,
)

SCHEMA = """
Tables:
iocs(id, ioc_type, value, malware, threat_type, reason, confidence, first_seen,
     last_seen, times_seen, is_active, risk_score, risk_level)
ioc_sightings(id, ioc_id, source, seen_at, raw_item_id)
ioc_enrichment(ioc_id, abuse_score, abuse_reports, abuse_country, abuse_isp,
               abuse_usage, shodan_ports, shodan_org, enriched_at)
cves(id, cve_id, cvss_score, severity, description, kev_listed, published)
articles(id, title, link, published, summary, apt_groups, malware)
apt_groups(id, name, first_seen, last_seen, times_seen)
"""

def _validate_sql(sql: str) -> str:
    sql = sql.strip()
    # Permit one trailing semicolon, reject any additional statement.
    if sql.endswith(";"):
        sql = sql[:-1].strip()
    if not sql or ";" in sql or not re.match(r"(?is)^select\b", sql):
        raise ValueError("Only one SELECT query is allowed.")
    if BLOCKED.search(sql):
        raise ValueError("Query contains a prohibited SQL keyword.")
    if "--" in sql or "/*" in sql or "*/" in sql:
        raise ValueError("SQL comments are not allowed.")
    # Ensure referenced table names are drawn from the known schema.
    refs = re.findall(r"(?i)\b(?:from|join)\s+([a-z_][a-z0-9_]*)", sql)
    if not refs or any(t.lower() not in ALLOWED_TABLES for t in refs):
        raise ValueError("Query references a table outside the approved schema.")
    if re.search(r"(?i)\b(limit)\s+\d+", sql):
        sql = re.sub(r"(?i)\blimit\s+\d+", "LIMIT 50", sql)
    elif not re.search(r"(?i)\blimit\b", sql):
        sql += " LIMIT 50"
    return sql

def chat_query(question: str) -> dict:
    question = (question or "").strip()
    if not question:
        return {"error": "Please enter a question."}
    if len(question) > 1000:
        return {"error": "Question is too long (maximum 1000 characters)."}

    prompt = f"""Convert the user's question into one PostgreSQL SELECT query.
Use only the tables and columns below. Return ONLY SQL, no markdown.
Never query secrets, system catalogs, or unrelated data. Limit results to 50.
{SCHEMA}
Question: {question}
SQL:"""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=90,
        )
        response.raise_for_status()
        generated = response.json().get("response", "")
        sql = _validate_sql(generated)
    except requests.RequestException:
        return {"error": "Local Ollama is unavailable. Start Ollama and ensure the configured model is installed."}
    except (ValueError, KeyError, TypeError):
        return {"error": "The assistant generated an unsupported query. Try a more specific question."}

    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "threatintel"),
            user=os.getenv("API_DB_USER", os.getenv("DB_USER")),
            password=os.getenv("API_DB_PASSWORD", os.getenv("DB_PASSWORD")),
            cursor_factory=psycopg2.extras.RealDictCursor,
            connect_timeout=5,
        )
        conn.set_session(readonly=True, autocommit=False)
        with conn.cursor() as cur:
            cur.execute("SET LOCAL statement_timeout = '5s'")
            cur.execute(sql)
            rows = [dict(row) for row in cur.fetchall()]
        conn.rollback()
        return {"count": len(rows), "rows": rows, "sql": sql}
    except Exception:
        if conn:
            conn.rollback()
        return {"error": "The query could not be executed against the current database.", "sql": sql}
    finally:
        if conn:
            conn.close()
