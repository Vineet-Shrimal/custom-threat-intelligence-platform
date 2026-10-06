\# Custom Threat Intelligence Platform



A full-stack \*\*Threat Intelligence Platform (TIP)\*\* built to collect, normalize, enrich, analyze, and visualize cyber threat intelligence from multiple public sources.



The project combines \*\*Python, FastAPI, PostgreSQL, React, Docker, threat-intelligence feeds, IOC enrichment, CVE analysis, risk scoring, and LLM-assisted processing\*\* into a single platform.



> \*\*Portfolio focus:\*\* This project demonstrates practical skills relevant to entry-level SOC Analyst, Cybersecurity Analyst, Threat Intelligence, and Security Operations roles.



\---



\## Key Capabilities



\* Collects intelligence from multiple public threat feeds

\* Ingests and normalizes raw threat data

\* Deduplicates and stores structured intelligence in PostgreSQL

\* Tracks \*\*IOCs, CVEs, threat articles, and APT groups\*\*

\* Integrates \*\*CISA KEV\*\* and \*\*NVD\*\* vulnerability intelligence

\* Enriches IP addresses using \*\*AbuseIPDB\*\*

\* Calculates IOC risk scores using multiple intelligence signals

\* Provides CVSS severity and KEV status for vulnerabilities

\* Uses Ollama for LLM-assisted article processing and chatbot functionality

\* Provides a REST API through FastAPI

\* Provides a React/Vite web interface for investigation and visualization

\* Supports authentication and MFA

\* Runs locally using Docker and Windows/PowerShell



\---



\## Architecture



```text

&#x20;                   ┌─────────────────────────┐

&#x20;                   │     Public Sources      │

&#x20;                   │                         │

&#x20;                   │ CISA KEV │ NVD          │

&#x20;                   │ ThreatFox │ Hacker News  │

&#x20;                   │ Ransomware.live          │

&#x20;                   └────────────┬────────────┘

&#x20;                                │

&#x20;                                ▼

&#x20;                   ┌─────────────────────────┐

&#x20;                   │     Raw Data Layer      │

&#x20;                   │       raw\_items         │

&#x20;                   └────────────┬────────────┘

&#x20;                                │

&#x20;                                ▼

&#x20;                   ┌─────────────────────────┐

&#x20;                   │ Processing \& Normalizing │

&#x20;                   │                         │

&#x20;                   │ Deduplication           │

&#x20;                   │ IOC Extraction           │

&#x20;                   │ CVE Processing           │

&#x20;                   │ Article Processing       │

&#x20;                   └────────────┬────────────┘

&#x20;                                │

&#x20;                                ▼

&#x20;                   ┌─────────────────────────┐

&#x20;                   │       PostgreSQL        │

&#x20;                   │                         │

&#x20;                   │ IOCs │ CVEs │ Articles  │

&#x20;                   │ APT Groups │ Enrichment │

&#x20;                   └────────────┬────────────┘

&#x20;                                │

&#x20;               ┌────────────────┴────────────────┐

&#x20;               ▼                                 ▼

&#x20;    ┌─────────────────────┐           ┌─────────────────────┐

&#x20;    │ Enrichment \& Risk   │           │     FastAPI API     │

&#x20;    │                     │           │                     │

&#x20;    │ AbuseIPDB           │           │ Authentication      │

&#x20;    │ NVD                 │           │ IOC APIs            │

&#x20;    │ Risk Scoring        │           │ CVE APIs            │

&#x20;    │ Confidence           │           │ Statistics          │

&#x20;    └─────────────────────┘           └──────────┬──────────┘

&#x20;                                                 │

&#x20;                                                 ▼

&#x20;                                     ┌─────────────────────┐

&#x20;                                     │    React / Vite     │

&#x20;                                     │                     │

&#x20;                                     │ Dashboard           │

&#x20;                                     │ IOCs                │

&#x20;                                     │ CVEs                │

&#x20;                                     │ Threat Feed         │

&#x20;                                     │ APT Groups          │

&#x20;                                     └─────────────────────┘

```



\---



\# Project Results



The platform was tested with real threat-intelligence data and produced the following results:



| Metric                        |      Result |

| ----------------------------- | ----------: |

| CISA KEV vulnerabilities      |   \*\*1,728\*\* |

| NVD-enriched CVEs             |   \*\*1,727\*\* |

| Critical CVEs                 |     \*\*615\*\* |

| High CVEs                     |     \*\*903\*\* |

| Medium CVEs                   |     \*\*201\*\* |

| Low CVEs                      |       \*\*8\*\* |

| Threat intelligence articles  |      \*\*50\*\* |

| Total IOCs                    |     \*\*120\*\* |

| IP addresses                  |      \*\*20\*\* |

| SHA-256 hashes                |       \*\*6\*\* |

| MD5 hashes                    |       \*\*1\*\* |

| AbuseIPDB-enriched IPs        | \*\*20 / 20\*\* |

| Low-risk IOCs                 |     \*\*119\*\* |

| Medium-risk IOCs              |       \*\*1\*\* |

| High-risk IOCs                |       \*\*0\*\* |

| High-confidence threat groups |       \*\*4\*\* |



\### Threat Groups Identified



\* Clop

\* JADEPUFFER

\* ShinyHunters

\* UNC2546



\---



\# Screenshots



\## Authentication



!\[CTI Login](docs/01\_cti\_login\_page.png)



The platform provides an authenticated interface with login and MFA support.



\---



\## Main Dashboard



!\[CTI Dashboard](docs/02\_cti\_dashboard.png)



The dashboard provides an overview of collected intelligence, vulnerabilities, IOCs, articles, and threat groups.



\---



\## Enriched Dashboard



!\[Enriched Dashboard](docs/03\_cti\_enriched\_dashboard.png)



Displays enrichment and risk-analysis results after processing IOC intelligence.



\---



\## CVE Vulnerabilities



!\[CVE Vulnerabilities](docs/04\_cti\_cve\_vulnerabilities.png)



Displays vulnerability intelligence including CVSS severity, published information, and CISA KEV status.



\---



\## Threat Intelligence Feed



!\[Threat Feed](docs/05\_cti\_threat\_feed.png)



Displays processed threat-intelligence articles collected from external sources.



\---



\## APT / Threat Groups



!\[APT Groups](docs/06\_cti\_apt\_groups.png)



Displays high-confidence threat groups identified during article processing.



\---



\# Technology Stack



\### Backend



\* Python

\* FastAPI

\* PostgreSQL

\* Pydantic

\* Uvicorn



\### Frontend



\* React

\* Vite

\* JavaScript

\* HTML

\* CSS



\### Infrastructure



\* Docker

\* Docker Desktop

\* PostgreSQL 16

\* Windows / PowerShell



\### Threat Intelligence



\* CISA Known Exploited Vulnerabilities

\* NVD

\* ThreatFox

\* Ransomware.live

\* The Hacker News

\* AbuseIPDB

\* Optional Shodan integration



\### AI



\* Ollama

\* Llama 3.2



\---



\# Intelligence Processing Pipeline



The platform follows a multi-stage processing workflow:



```text

External Threat Feeds

&#x20;       │

&#x20;       ▼

Raw Data Ingestion

&#x20;       │

&#x20;       ▼

Normalization

&#x20;       │

&#x20;       ▼

Deduplication

&#x20;       │

&#x20;       ▼

IOC / CVE / Article Processing

&#x20;       │

&#x20;       ▼

Threat Intelligence Database

&#x20;       │

&#x20;       ├──────────────► NVD Enrichment

&#x20;       │

&#x20;       ├──────────────► AbuseIPDB Enrichment

&#x20;       │

&#x20;       ├──────────────► Risk Scoring

&#x20;       │

&#x20;       └──────────────► Threat Group Identification

&#x20;       │

&#x20;       ▼

FastAPI

&#x20;       │

&#x20;       ▼

React Dashboard

```



\---



\# IOC Risk Scoring



The platform assigns risk based on multiple intelligence signals rather than relying on a single indicator.



Signals can include:



\* AbuseIPDB reputation

\* Number of reports

\* IOC confidence

\* Threat intelligence context

\* Indicator type

\* Other enrichment metadata



Example:



```text

IOC

&#x20;│

&#x20;├── AbuseIPDB score

&#x20;├── Abuse reports

&#x20;├── Confidence

&#x20;└── Intelligence context

&#x20;         │

&#x20;         ▼

&#x20;     Risk Score

&#x20;         │

&#x20;         ▼

&#x20;   LOW / MEDIUM / HIGH

```



During testing, the platform identified one medium-risk IOC:



```text

IOC: 103.102.31.18

Risk Score: 49

AbuseIPDB Score: 25

Reports: 11

Risk Level: MEDIUM

```



\---



\# API



The backend is exposed through FastAPI.



Local API:



```text

http://127.0.0.1:8001

```



Swagger documentation:



```text

http://127.0.0.1:8001/docs

```



\### Example API endpoints



```text

POST /login

POST /chat

GET  /stats

GET  /iocs

GET  /iocs/recurring

GET  /ioc/{value}

```



The API provides access to authentication, statistics, IOC investigation, recurring indicators, and chatbot functionality.



\---



\# Local Setup



\## Requirements



Install the following:



\* Python 3.12+

\* Node.js

\* npm

\* Docker Desktop

\* Git



\---



\## 1. Clone the Repository



```powershell

git clone https://github.com/Vineet-Shrimal/custom-threat-intelligence-platform.git

cd custom-threat-intelligence-platform

```



\---



\## 2. Start PostgreSQL



The project uses PostgreSQL through Docker.



Example:



```powershell

docker start cti-postgres

```



If the container does not exist yet, create it according to your PostgreSQL configuration.



\---



\## 3. Configure Backend Environment



Create:



```text

backend/.env

```



Use `backend/.env.example` as the template.



Do \*\*not\*\* commit `.env` files containing real credentials or API keys.



\---



\## 4. Install Backend Dependencies



```powershell

cd backend

```



Create a virtual environment:



```powershell

python -m venv venv

```



Install dependencies:



```powershell

.\\venv\\Scripts\\python.exe -m pip install -r requirements.txt

```



\---



\## 5. Start the FastAPI Backend



From the project root:



```powershell

.\\backend\\venv\\Scripts\\python.exe -m uvicorn backend.api:app --host 127.0.0.1 --port 8001

```



Swagger:



```text

http://127.0.0.1:8001/docs

```



> Port `8001` is used because port `8000` is occupied by a local Splunk instance in the development environment.



\---



\## 6. Start the Frontend



Open a second PowerShell terminal:



```powershell

cd frontend

npm install

npm.cmd run dev

```



The frontend will normally be available at:



```text

http://localhost:5173

```



\---



\# Database



The platform uses PostgreSQL to store structured intelligence.



Main tables include:



```text

apt\_groups

articles

cves

ioc\_enrichment

ioc\_sightings

iocs

raw\_items

```



The `raw\_items` layer preserves ingested intelligence before it is processed into structured entities.



\---



\# Security Considerations



The project was developed with basic security practices in mind:



\* Secrets stored outside source code

\* `.env` files excluded from Git

\* Environment variable templates provided

\* JWT-based authentication

\* MFA support

\* Separate database roles

\* API authentication

\* CORS configuration

\* Local-only development services



\*\*Never commit real API keys, passwords, JWT secrets, MFA secrets, or other credentials.\*\*



\---



\# Known Limitations



\* Some public feeds require API keys or have rate limits.

\* Threat-intelligence feeds can change format over time.

\* LLM-based extraction can produce incorrect classifications.

\* Threat-group classification therefore uses additional high-confidence validation rules.

\* Shodan enrichment is included as an optional integration but was not treated as a verified enrichment result because the configured request returned HTTP 401.

\* The platform is intended as a portfolio/lab project rather than a production-grade enterprise TIP.



\---



\# Project Structure



```text

custom-threat-intelligence-platform/

│

├── backend/

│   ├── api.py

│   ├── auth.py

│   ├── chatbot.py

│   ├── compute\_risk.py

│   ├── processor\_articles.py

│   ├── processor\_structured.py

│   ├── connector\_cisa\_kev.py

│   ├── connector\_hackernews.py

│   ├── connector\_nvd.py

│   ├── connector\_rl\_iocs.py

│   ├── connector\_threatfox.py

│   ├── setup\_admin.py

│   ├── schema\_patch.sql

│   └── requirements.txt

│

├── frontend/

│   ├── src/

│   ├── public/

│   ├── package.json

│   └── vite.config.\*

│

├── docs/

│   ├── 01\_cti\_login\_page.png

│   ├── 02\_cti\_dashboard.png

│   ├── 03\_cti\_enriched\_dashboard.png

│   ├── 04\_cti\_cve\_vulnerabilities.png

│   ├── 05\_cti\_threat\_feed.png

│   └── 06\_cti\_apt\_groups.png

│

├── ORIGINAL\_PROJECT\_CREDIT.md

├── README.md

└── .gitignore

```



\---



\# Project Attribution



This project is an \*\*adapted and reworked implementation\*\* based on the original Custom Threat Intelligence Platform project by \*\*Aditya Raj\*\*.



Original project:



```text

https://github.com/adityrajtiwary/Custom-Threat-intel-Platform

```



The repository has been substantially adapted for portfolio development, including changes to the processing pipeline, enrichment workflow, risk scoring, frontend/API configuration, threat-group handling, documentation, and local deployment.



See \[`ORIGINAL\_PROJECT\_CREDIT.md`](ORIGINAL\_PROJECT\_CREDIT.md) for additional attribution details.



\---



\# Portfolio Focus



This project demonstrates practical exposure to:



\* Threat Intelligence

\* IOC investigation

\* Vulnerability intelligence

\* CVE / CISA KEV analysis

\* Threat feed ingestion

\* IOC enrichment

\* Risk scoring

\* PostgreSQL

\* REST APIs

\* FastAPI

\* React

\* Docker

\* Authentication and MFA

\* Security-focused data processing

\* Basic automation and Python scripting

\* LLM-assisted cybersecurity workflows



These skills are directly relevant to \*\*SOC Analyst, Cybersecurity Analyst, Threat Intelligence Analyst, and Security Operations\*\* roles.



