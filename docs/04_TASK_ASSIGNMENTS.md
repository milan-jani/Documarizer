# 👥 Task Assignments

> **Team 18 — 3-Hour Hackathon Sprint Plan**
> **Start:** 11:00 AM | **End:** 2:00 PM | **3 October 2026**

---

## Team Members & Roles

| Member | Role | Primary Modules |
|--------|------|----------------|
| **Member 1** | Frontend + Demo Lead | Frontend UI, Demo preparation |
| **Member 2** | Backend Lead + LLM Integration | FastAPI server, Gemini API wrapper, API routes |
| **Member 3** | Defense Engineer | Defense prompts, Guardrails, Sanitization |
| **Member 4** | Attack & Evaluation Lead | Attack suite, Test cases, Metrics, Prompt history |

> ⚠️ If team has 3 members: Member 3 absorbs Member 4's tasks (attacks + defense are closely related)

---

## Sprint Timeline

### Phase 1: Setup & Scaffold (11:00 AM — 11:30 AM) `[30 min]`

| Who | Task | Deliverable |
|-----|------|-------------|
| **Member 1** | Set up frontend HTML/CSS/JS skeleton | Working UI with input box, output area, tabs |
| **Member 2** | Set up FastAPI project, install deps, configure Gemini API key | Server runs, `/health` endpoint works |
| **Member 3** | Write v1 defense prompts (both techniques) | Two prompt templates ready |
| **Member 4** | Define 8 attack types + write 10 test cases in JSON | `test_cases.json` complete |
| **ALL** | Read & understand interface contracts | Everyone knows the API shapes |

**Checkpoint 11:30:** Server runs, UI loads, prompts drafted, attacks defined.

---

### Phase 2: Core Integration (11:30 AM — 12:15 PM) `[45 min]`

| Who | Task | Deliverable |
|-----|------|-------------|
| **Member 1** | Connect frontend to `/api/summarize` endpoint | Can submit doc & see summary |
| **Member 2** | Implement `/api/summarize` + `/api/compare` + LLM service | Both endpoints work end-to-end |
| **Member 3** | Implement `defense.py` (both techniques) + `guardrails.py` | Defense engine integrated |
| **Member 4** | Implement `attacks.py` + `logger.py` + run v1 baseline test | V1 pass-rate recorded |

**Checkpoint 12:15:** Can summarize a document via the UI. V1 metrics captured.

---

### Phase 3: Hardening & Stretch (12:15 PM — 1:15 PM) `[60 min]`

| Who | Task | Deliverable |
|-----|------|-------------|
| **Member 1** | Build side-by-side comparison view + attack report dashboard | Comparison UI works |
| **Member 2** | Implement `/api/attack-test` + `/api/metrics` + `/api/prompt-history` | All APIs functional |
| **Member 3** | Iterate on defense prompts (v2, v3) based on attack results | Improved pass-rate |
| **Member 4** | Run full attack suite, identify failures, log everything | Complete attack report |

**Checkpoint 1:15:** All features working. Attack suite running. Prompt iterations logged.

---

### Phase 4: Polish & Demo Prep (1:15 PM — 2:00 PM) `[45 min]`

| Who | Task | Deliverable |
|-----|------|-------------|
| **Member 1** | Polish UI, prepare demo flow, test with unseen input | Demo-ready frontend |
| **Member 2** | Bug fixes, ensure all endpoints stable | Stable backend |
| **Member 3** | Document final prompts, write "where it still fails" section | Final prompt documented |
| **Member 4** | Generate final metrics (v1 vs final), finalize prompt history | Final report ready |
| **ALL** | Practice demo: each member explains their prompts | Everyone can explain everything |

**Checkpoint 2:00:** DEMO TIME 🚀

---

## Deliverables Ownership

| Deliverable | Owner | Status |
|-------------|-------|--------|
| Working prototype (web app) | Member 1 + 2 | ⬜ |
| 3 injection attack demos | Member 4 | ⬜ |
| Defense prompt explanation | Member 3 | ⬜ |
| "Where it still fails" analysis | Member 3 + 4 | ⬜ |
| 8 attack types (automated suite) | Member 4 | ⬜ |
| Pass-rate report | Member 4 | ⬜ |
| 10+ labelled test cases | Member 4 | ⬜ |
| Metric: v1 vs final comparison | Member 4 | ⬜ |
| Side-by-side technique comparison | Member 1 + 3 | ⬜ |
| Guardrails demo | Member 3 | ⬜ |
| Timestamped prompt history | ALL (Member 4 maintains) | ⬜ |
| Live demo on unseen input | Member 1 (presents) | ⬜ |

---

## Communication Rules

1. **Git commits** every 15 minutes minimum — commit message format: `[member-name] short description`
2. **Prompt changes** must be logged in `prompt_history.json` with timestamp
3. **API contract changes** must be announced to all members immediately
4. **Blocked?** Ask for help within 5 minutes — no hero debugging in a 3-hour hackathon
5. **Test early** — don't wait until Phase 4 to test integration

---

## Quick Reference: Who Owns What File

```
backend/
├── main.py              → Member 2
├── llm_service.py       → Member 2
├── defense.py           → Member 3
├── guardrails.py        → Member 3
├── attacks.py           → Member 4
├── logger.py            → Member 4
└── requirements.txt     → Member 2

frontend/
├── index.html           → Member 1
├── style.css            → Member 1
└── app.js               → Member 1

tests/
└── test_cases.json      → Member 4

logs/
└── prompt_history.json  → ALL (Member 4 maintains)

docs/                    → Shared (Member 4 primary)
```
