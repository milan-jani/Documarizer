# 🛡️ Documarizer — Secure Document Summarization Engine

Documarizer is an advanced document summarization system built to **resist prompt injection attacks** hidden inside documents. It utilizes the Google Gemini API with layered defense techniques to ensure malicious instructions embedded in documents are strictly ignored.

## Features

- **Prompt Injection Defense**: Robust protection against role hijacking, payload splitting, system prompt extraction, and obfuscation.
- **Layered Security Architecture**: Combines input guardrails, output guardrails, and hierarchical system prompts.
- **Defense Techniques**: 
  - *XML Tag Isolation*: Wraps documents in strict XML boundary tags with an explicit instruction hierarchy.
  - *Sandwich Defense*: Wraps untrusted text in delimiters with repeated negative constraints.
- **Automated Attack Suite**: Built-in Python framework for continuous adversarial testing.

## Quick Start

```bash
# 1. Install dependencies
cd backend
pip install -r requirements.txt

# 2. Set your API key
#    Create a .env file in the project root with:
#    GEMINI_API_KEY=your_key_here

# 3. Run the server
python -m backend.main

# 4. Open the frontend
#    Navigate to http://localhost:8000 in your browser
```

## Project Structure

```
Documarizer/
├── docs/                          ← System architecture and API documentation
├── backend/
│   ├── main.py                    ← FastAPI server
│   ├── llm_service.py             ← Gemini API integration
│   ├── defense.py                 ← Defense prompts engine
│   ├── guardrails.py              ← Input/Output validation logic
│   ├── attacks.py                 ← Automated attack testing suite
│   └── logger.py                  ← Security audit and prompt history logger
├── frontend/
│   ├── index.html                 ← Web UI
│   ├── style.css
│   └── app.js                     ← UI logic and API client
├── tests/
│   ├── run_attack_suite.py        ← Test runner
│   ├── test_cases.json            ← Adversarial testing payloads
│   └── test_report.json           ← Latest DSR (Defense Success Rate) results
└── logs/                          ← Runtime execution logs
```

## Architecture Documentation
For detailed system architecture, API contracts, and evaluation metrics, please refer to the `docs/` directory.
