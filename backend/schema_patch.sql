-- Additive migration for fields referenced by the API and enrichment jobs.
-- Safe to run after schema.sql and schema_phase2.sql.
ALTER TABLE iocs
    ADD COLUMN IF NOT EXISTS risk_score INTEGER NOT NULL DEFAULT 0,
    ADD COLUMN IF NOT EXISTS risk_level TEXT NOT NULL DEFAULT 'LOW';

CREATE TABLE IF NOT EXISTS ioc_enrichment (
    ioc_id BIGINT PRIMARY KEY REFERENCES iocs(id) ON DELETE CASCADE,
    abuse_score INTEGER,
    abuse_reports INTEGER,
    abuse_country TEXT,
    abuse_isp TEXT,
    abuse_usage TEXT,
    shodan_ports TEXT,
    shodan_org TEXT,
    enriched_at TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS idx_iocs_risk_level ON iocs(risk_level);
CREATE INDEX IF NOT EXISTS idx_ioc_enrichment_abuse_score ON ioc_enrichment(abuse_score);
