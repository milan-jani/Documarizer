# 📋 Requirements Document

> **Problem 18 — Prompt Injection Defense**
> **Theme D:** Reliability, Hallucination and Safety
> **Hackathon:** Prompt Engineering for Generative AI — 3-Hour Hackathon, 3 October 2026
> **Team No.:** 18 | **Venue:** MB314

---

## 1. Problem Statement

Build a **document summarizer** that ignores malicious instructions hidden inside the document.

The system must accept any document as input, produce a faithful summary, and **resist prompt injection attacks** embedded within the document content.

---

## 2. Functional Requirements

### FR-1: Document Summarization
| ID | Requirement | Priority |
|----|-------------|----------|
| FR-1.1 | Accept plain-text document input (paste or upload) | **Must** |
| FR-1.2 | Produce a concise, accurate summary of the document | **Must** |
| FR-1.3 | Summary must faithfully represent ONLY the document content | **Must** |
| FR-1.4 | Support documents of varying lengths (100–5000 words) | **Should** |

### FR-2: Prompt Injection Defense
| ID | Requirement | Priority |
|----|-------------|----------|
| FR-2.1 | Detect and ignore injected instructions within document text | **Must** |
| FR-2.2 | Implement at least **2 prompting techniques** for defense | **Must** |
| FR-2.3 | Show side-by-side comparison of techniques in demo | **Must** |
| FR-2.4 | Cover at least **8 attack types** with automated attack suite | **Must** (stretch) |
| FR-2.5 | Generate a **pass-rate report** for layered defenses | **Must** (stretch) |
| FR-2.6 | Document where defenses **still fail** (honesty) | **Must** |

### FR-3: Guardrails
| ID | Requirement | Priority |
|----|-------------|----------|
| FR-3.1 | Reject invalid/empty input with clear error message | **Must** |
| FR-3.2 | Detect and refuse off-topic input (non-document content) | **Must** |
| FR-3.3 | Handle refusals gracefully (LLM refuses to respond) | **Must** |
| FR-3.4 | Validate output — ensure summary is coherent and relevant | **Must** |

### FR-4: Measurement & Evaluation
| ID | Requirement | Priority |
|----|-------------|----------|
| FR-4.1 | Maintain a labelled test set of **10+ cases** | **Must** |
| FR-4.2 | Define at least **one metric** (e.g., defense success rate) | **Must** |
| FR-4.3 | Show **first version vs final version** metric comparison | **Must** |
| FR-4.4 | Automated test runner for attack suite | **Should** |

---

## 3. Non-Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-1 | Response time < 15 seconds per summarization | **Should** |
| NFR-2 | Works on new, unseen input during demo | **Must** |
| NFR-3 | Every team member can explain every prompt | **Must** |
| NFR-4 | Timestamped prompt history from 11:00 AM onward | **Must** |
| NFR-5 | Clean, usable web UI for demo | **Should** |

---

## 4. Deliverables Checklist

- [ ] Working prototype (web app)
- [ ] 3 injection attack demos with defense prompts
- [ ] 8 attack types in automated suite (stretch)
- [ ] Pass-rate report
- [ ] Labelled test set (10+ cases)
- [ ] Metric comparison: v1 vs final
- [ ] Side-by-side prompting technique comparison
- [ ] Guardrails demo (invalid input, off-topic, refusals)
- [ ] Timestamped prompt history document
- [ ] Live demo on unseen input

---

## 5. Tech Stack

| Layer | Technology |
|-------|-----------|
| **LLM** | Google Gemini API (gemini-2.0-flash) |
| **Backend** | Python (Flask / FastAPI) |
| **Frontend** | HTML/CSS/JS (single-page app) |
| **Testing** | Python automated attack suite |
| **Version Control** | Git |

---

## 6. Glossary

| Term | Definition |
|------|-----------|
| **Prompt Injection** | An attack where malicious instructions are embedded in user-provided content to hijack the LLM's behavior |
| **Guardrail** | Input/output validation logic that prevents misuse or unexpected behavior |
| **Defense Prompt** | System prompt engineered to resist injection attacks |
| **Pass Rate** | Percentage of attack attempts successfully blocked by the defense |
| **Layered Defense** | Multiple defense mechanisms applied in sequence |
