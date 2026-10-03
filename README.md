# 🛡️ Prompt Injection Defense — Document Summarizer

> **Problem 18** | Team 18 | Marwadi University Hackathon — 3 October 2026
> **Theme D:** Reliability, Hallucination and Safety

## What is this?

A document summarizer built to **resist prompt injection attacks** hidden inside documents. It uses Google Gemini API with layered defense techniques to ensure malicious instructions embedded in documents are ignored.

## Quick Start

```bash
# 1. Install dependencies
cd backend
pip install -r requirements.txt

# 2. Set your API key
#    Create a .env file in the project root with:
#    GEMINI_API_KEY=your_key_here

# 3. Run the server
python main.py

# 4. Open the frontend
#    Open frontend/index.html in your browser
#    Or navigate to http://localhost:8000
```

## Project Structure

```
PEGAI-Hackathon/
├── docs/                          ← Team documentation
│   ├── 01_REQUIREMENTS.md         ← What we need to build
│   ├── 02_ARCHITECTURE.md         ← System design & data flow
│   ├── 03_INTERFACE_CONTRACTS.md  ← API specs & module interfaces
│   ├── 04_TASK_ASSIGNMENTS.md     ← Who does what & when
│   ├── 05_ATTACK_TYPES.md         ← 10 attack type definitions
│   ├── 06_TEST_CASES.md           ← 12 labelled test cases
│   ├── 07_PROMPT_HISTORY.md       ← Timestamped prompt log
│   └── 08_EVALUATION_METRICS.md   ← Scoring & reporting
├── backend/
│   ├── main.py                    ← FastAPI server
│   ├── llm_service.py             ← Gemini API wrapper
│   ├── defense.py                 ← Defense prompts (2 techniques)
│   ├── guardrails.py              ← Input/Output validation
│   ├── attacks.py                 ← Automated attack suite
│   ├── logger.py                  ← Prompt history logger
│   └── requirements.txt           ← Python dependencies
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── tests/
│   └── test_cases.json            ← Test data
├── logs/
│   └── prompt_history.json        ← Runtime logs
├── .env                           ← API keys (DO NOT COMMIT)
├── .gitignore
└── README.md
```

## Defense Techniques

1. **Sandwich Defense** — Wraps document in delimiters with repeated instructions before and after
2. **XML Tag Isolation** — Wraps document in `<document>` tags with explicit instruction hierarchy

## Team

| Member | Role |
|--------|------|
| Member 1 | Frontend + Demo |
| Member 2 | Backend + API |
| Member 3 | Defense Engineering |
| Member 4 | Attack Suite + Evaluation |

## Docs for Team

Start by reading these in order:
1. [Requirements](docs/01_REQUIREMENTS.md)
2. [Architecture](docs/02_ARCHITECTURE.md)
3. [Interface Contracts](docs/03_INTERFACE_CONTRACTS.md)
4. [Your Task Assignment](docs/04_TASK_ASSIGNMENTS.md)
