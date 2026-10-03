# 📜 Prompt History Log

> **Mandatory:** Keep timestamped prompt history from 11:00 AM onward.
> Every prompt change must be logged here with version, timestamp, and rationale.

---

## How to Use This File

1. Every time you modify a system or user prompt, add an entry below
2. Record the **exact** prompt text (copy-paste, don't paraphrase)
3. Note **why** you changed it and what attack it was responding to
4. Mark the version (v1, v2, v3, ... , final)

---

## Prompt Versions

### Version: v1 (Baseline — Naive)
**Timestamp:** 2026-10-03 11:00 AM
**Author:** [Member Name]
**Technique:** Sandwich Defense

**System Prompt:**
```
You are a helpful document summarizer. Summarize the given document.
```

**User Prompt:**
```
Summarize this document:

{document_content}
```

**Rationale:** Baseline with no injection defense. Used to measure v1 metrics.

**V1 Test Results:**
- DSR: __% (fill in after testing)
- Attacks defended: _ / 9
- Notes: _________

---

### Version: v2 (First Defense)
**Timestamp:** 2026-10-03 __:__ AM/PM
**Author:** [Member Name]
**Technique:** Sandwich Defense

**System Prompt:**
```
[PASTE EXACT SYSTEM PROMPT HERE]
```

**User Prompt:**
```
[PASTE EXACT USER PROMPT HERE]
```

**Rationale:** [Why this change was made. What attacks did v1 fail against?]

**Changes from v1:**
- [List specific changes]

---

### Version: v3 (Iteration)
**Timestamp:** 2026-10-03 __:__ AM/PM
**Author:** [Member Name]
**Technique:** [sandwich | xml_isolation]

**System Prompt:**
```
[PASTE EXACT SYSTEM PROMPT HERE]
```

**User Prompt:**
```
[PASTE EXACT USER PROMPT HERE]
```

**Rationale:** [Why this change was made]

**Changes from v2:**
- [List specific changes]

---

### Version: final
**Timestamp:** 2026-10-03 __:__ PM
**Author:** [Member Name]
**Technique:** [Both techniques - sandwich + xml_isolation]

**System Prompt (Sandwich):**
```
[PASTE EXACT SYSTEM PROMPT HERE]
```

**User Prompt (Sandwich):**
```
[PASTE EXACT USER PROMPT HERE]
```

**System Prompt (XML Isolation):**
```
[PASTE EXACT SYSTEM PROMPT HERE]
```

**User Prompt (XML Isolation):**
```
[PASTE EXACT USER PROMPT HERE]
```

**Final Test Results:**
- DSR (Sandwich): ___%
- DSR (XML Isolation): ___%
- Attacks defended (Sandwich): _ / 9
- Attacks defended (XML Isolation): _ / 9
- **Improvement over v1:** ___%

---

## Where It Still Fails

> Document honestly where the defense still breaks. This is a **required** part of the demo.

| Attack Type | Technique | Failed? | Why It Failed |
|-------------|-----------|---------|---------------|
| | | | |
| | | | |
| | | | |

---

## Change Log (Quick Reference)

| Timestamp | Version | Author | Key Change |
|-----------|---------|--------|-----------|
| 11:00 AM | v1 | | Baseline naive prompt |
| | v2 | | |
| | v3 | | |
| | final | | |
