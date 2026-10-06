# Custom Threat Intelligence Platform — Adapted Portfolio Edition

A local Cyber Threat Intelligence (CTI) platform for collecting public threat feeds, normalizing and deduplicating indicators, tracking sightings, enriching IP indicators, scoring risk, and exploring results through a React dashboard and FastAPI.

> **Project provenance:** This repository is an adapted and repaired version of the [Custom Threat Intel Platform](https://github.com/adityrajtiwary/Custom-Threat-intel-Platform) by Aditya Raj. The original project is credited here. The Windows setup notes, missing-file replacements, database migration, and any further modifications should be described as adaptations—not as authorship of the original project. Review the source license before publishing a derivative.

## Features

- Collection connectors for ransomware.live, ThreatFox, CISA KEV, NVD, and The Hacker News.
- PostgreSQL JSONB raw-data landing table.
- IOC normalization, deduplication, and source sightings.
- CVE records, KEV flags, articles, and APT group records.
- Optional AbuseIPDB and Shodan enrichment (API keys required).
- Composite IOC risk scoring.
- FastAPI endpoints and React/Vite dashboard.
- Password + TOTP login and JWT sessions.
- Optional natural-language query assistant using local Ollama. SQL validation is defense in depth; configure a genuinely read-only PostgreSQL role.

## Architecture

Public feeds → Python connectors → `raw_items` → processors → IOC/CVE/article tables → enrichment + risk scoring → FastAPI → React dashboard.

## Requirements

- Python 3.12
- Node.js 20+
- Docker Desktop with WSL 2 (Windows) or Docker Engine (Linux)
- PostgreSQL 16 (Docker is one option)
- Ollama + `llama3.2` for the chatbot/article LLM features
- Optional API keys: AbuseIPDB, Shodan, NVD, ThreatFox, ransomware.live PRO

## Windows setup

Run commands in PowerShell. From the repository root:

### 1. Start PostgreSQL

If you already created the `cti-postgres` container for this project, keep using it; don't create a second one.

```powershell
docker ps
```

For a new local lab only:

```powershell
docker run --name cti-postgres -e POSTGRES_DB=threatintel -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=replace-with-a-local-password -p 5432:5432 -v cti_postgres_data:/var/lib/postgresql/data -d postgres:16
```

Use a unique local password. Do not reuse it elsewhere.

### 2. Configure backend

```powershell
cd backend
Copy-Item .env.example .env
py -3.12 -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Edit `backend\.env` with local DB credentials and any API keys you have. Never commit `.env`.

### 3. Create database schema

From the `backend` folder, copy SQL files into the running container and apply them in order:

```powershell
docker cp .\schema.sql cti-postgres:/tmp/schema.sql
docker cp .\schema_phase2.sql cti-postgres:/tmp/schema_phase2.sql
docker cp .\schema_patch.sql cti-postgres:/tmp/schema_patch.sql
docker exec cti-postgres psql -U postgres -d threatintel -v ON_ERROR_STOP=1 -f /tmp/schema.sql
docker exec cti-postgres psql -U postgres -d threatintel -v ON_ERROR_STOP=1 -f /tmp/schema_phase2.sql
docker exec cti-postgres psql -U postgres -d threatintel -v ON_ERROR_STOP=1 -f /tmp/schema_patch.sql
```

These commands use the container's `postgres` administrator to create the schema. Create separate application and read-only roles before using the API beyond a local test. The API role should only have `SELECT` access to the required tables; pipeline jobs need appropriate write permissions.

### 4. Set up login and MFA

```powershell
python setup_admin.py
```

The script creates credentials and a TOTP secret in `.env`. Scan the displayed QR code with an authenticator app. Keep the secret private.

### 5. Start the API

```powershell
uvicorn api:app --host 127.0.0.1 --port 8000 --reload
```

API docs: http://127.0.0.1:8000/docs

### 6. Start the frontend

Open a second PowerShell window:

```powershell
cd "D:\SOC Projects\CTI\frontend"
npm install
npm run dev
```

Open the Vite URL shown in the terminal (usually http://localhost:5173).

**Note:** Check `frontend/vite.config.js` and ensure `/api` requests proxy to `http://127.0.0.1:8000`. The frontend API client uses the `/api` path.

### 7. Optional chatbot

Install/start Ollama and pull the configured model:

```powershell
ollama pull llama3.2
```

Keep Ollama running. Configure `OLLAMA_MODEL` / `OLLAMA_URL` in `backend\.env` if needed. The chatbot is optional; the rest of the dashboard should be usable without it only if the API import is present (this edition includes `chatbot.py`).

## Pipeline scripts

Run individual connectors/processors from `backend` after the schema and `.env` are ready. The included `run_pipeline.sh` is a Bash script and is **not directly executable in PowerShell**; use WSL/Git Bash or run the Python scripts individually in the documented order. Some connectors require API keys and may be rate-limited.

## Security notes

- Keep secrets in `.env`; use `.env.example` only as a template.
- Use a dedicated least-privilege database role for the API/chatbot.
- SQL validation is not a substitute for database permissions.
- Keep API keys private and respect each provider's terms/rate limits.
- The included local setup is for a lab/demo; configure TLS, restrictive CORS, secure secrets, and deployment hardening before exposing it to a network.

## Known limitations / verify before claiming

- This package has not been validated against live provider APIs or a production deployment.
- Feed availability, API quotas, and model output vary.
- The scoring model is heuristic, not a calibrated probability of compromise.
- Review every connector and test the full pipeline with sample data before describing it as fully operational.

## Technology stack

Python, FastAPI, PostgreSQL, psycopg2, React, Vite, Axios, Recharts, Docker, Ollama, AbuseIPDB, Shodan, NVD, CISA KEV, ThreatFox.

## Acknowledgment

Original project: [Aditya Raj — Custom Threat Intel Platform](https://github.com/adityrajtiwary/Custom-Threat-intel-Platform). This repository is an adapted derivative. Preserve applicable license and attribution notices.
