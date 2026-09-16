# AI-CNAS — AI-Powered Criminal Network Analysis System

> **Smart India Hackathon — India-Oriented GovTech Solution**

An AI-assisted investigative intelligence platform that converts fragmented FIR, CDR, financial, and other authorized investigative records into an explainable relationship graph.

![Status](https://img.shields.io/badge/Status-SIH%20Prototype-blue)
![Python](https://img.shields.io/badge/Python-3.11+-green)
![React](https://img.shields.io/badge/React-18-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-teal)

## 🎯 Problem Statement

> *"How can we help Indian investigators convert fragmented FIR, communication, financial and other authorized investigative records into an explainable relationship graph that reveals meaningful connections and anomalies without replacing human judgment?"*

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│             AI-CNAS                         │
│                                             │
│  1. DATA INGESTION                          │
│     FIR | CDR | Transactions | Reports      │
│                    ↓                        │
│  2. DOCUMENT INTELLIGENCE                   │
│     OCR | Language | NER | Relations        │
│                    ↓                        │
│  3. ENTITY RESOLUTION                       │
│     Identity matching + Human review        │
│                    ↓                        │
│  4. KNOWLEDGE GRAPH                         │
│     People | Phones | Accounts | Events     │
│                    ↓                        │
│  5. ANALYTICS                               │
│     Centrality | Communities | Anomalies    │
│                    ↓                        │
│  6. INVESTIGATOR DASHBOARD                  │
│     Graph | Timeline | Map | Evidence       │
│                                             │
│  Cross-cutting: RBAC | Audit | Provenance   │
└─────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm 9+

### Backend Setup

```bash
# From project root
cd backend
pip install -r requirements.txt

# Generate synthetic dataset
python seed/generate_dataset.py

# Start backend (from project root)
cd ..
python run.py
```

The API will be available at `http://localhost:8000`
API docs at `http://localhost:8000/docs`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The dashboard will be available at `http://localhost:5173`

### Docker Setup (Alternative)

```bash
docker-compose up --build
```

## 📊 Demo Flow

1. **Login** → Default: `admin` / `admin`
2. **Create Case** → FIR-2026-001
3. **Upload FIR** → Hindi/English FIR document → AI extracts entities
4. **Upload CDR** → Phone call records → Communication network appears
5. **Upload Transactions** → Bank records → Financial network reveals
6. **View Graph** → Interactive network visualization
7. **Explore Centrality** → Key network nodes ranked
8. **Detect Communities** → Criminal clusters identified
9. **View Anomalies** → Unusual patterns flagged as INVESTIGATIVE LEADS
10. **Explain Link** → Click any edge → See why AI made this connection
11. **Generate Report** → Complete investigation summary

## 🧠 Key Features

### Multilingual NLP
- Hindi and English FIR processing
- Named Entity Recognition (persons, phones, accounts, vehicles, locations)
- Relationship extraction from unstructured text

### Entity Resolution
- Cross-script matching (रमेश कुमार ↔ Ramesh Kumar)
- Fuzzy name matching with confidence scores
- Human-in-the-loop review for uncertain matches

### Knowledge Graph
- NetworkX-powered graph analytics
- Cytoscape.js interactive visualization
- Node types: Person, Phone, Account, Vehicle, Location, Organization

### Analytics Engine
- **Degree Centrality** — Most connected entities
- **Betweenness Centrality** — Bridge entities between groups
- **PageRank** — Entities connected to other important entities
- **Community Detection** — Louvain algorithm for cluster discovery
- **Anomaly Detection** — Transaction bursts, communication spikes, circular patterns

### Explainability
Every AI-generated link includes:
- Confidence score
- Supporting evidence records
- Source documents
- Observation period
- Processing methodology

## 🛡️ Important Disclaimer

> **AI-CNAS outputs are analytical leads generated from available source data and require independent human verification.**

The system does NOT:
- Determine guilt
- Predict criminal behavior
- Recommend arrests
- Take autonomous enforcement action

## 🔒 Security
- JWT-based authentication
- Role-Based Access Control (RBAC)
- Tamper-evident audit logs (hash chain)
- All sensitive operations logged

## 📁 Project Structure

```
ai-cnas/
├── run.py                  # Backend runner
├── docker-compose.yml      # Docker orchestration
├── backend/
│   ├── main.py             # FastAPI application
│   ├── config.py           # Settings
│   ├── database.py         # SQLAlchemy setup
│   ├── models/             # ORM models
│   ├── api/                # REST API endpoints
│   ├── services/           # Business logic
│   ├── nlp/                # NLP pipeline
│   └── seed/               # Synthetic dataset
└── frontend/
    ├── src/
    │   ├── pages/           # Dashboard, CasePage, etc.
    │   ├── components/      # Graph, Timeline, Map, etc.
    │   ├── api/             # API client
    │   └── types/           # TypeScript types
    └── package.json
```

## 🏆 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18, TypeScript, Vite |
| Visualization | Cytoscape.js, Leaflet, Recharts |
| Styling | Tailwind CSS |
| Backend | Python 3.11, FastAPI |
| Graph Analytics | NetworkX, python-louvain |
| NLP | Custom Hindi/English NER |
| Database | SQLite (SQLAlchemy) |
| Auth | JWT (python-jose) |
| Containerization | Docker |

## 👥 Team

Smart India Hackathon Submission

---

*Built for Smart India Hackathon — Empowering Indian investigators with AI-assisted intelligence*
