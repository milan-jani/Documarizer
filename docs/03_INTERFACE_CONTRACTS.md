# 🔗 Interface Contracts

> API contracts between all modules. Every team member must follow these interfaces.

---

## 1. REST API Endpoints (Backend ↔ Frontend)

### POST `/api/summarize`
> Summarize a document using a specific defense technique.

**Request:**
```json
{
  "document": "string (required) — the document text to summarize",
  "technique": "string (required) — 'sandwich' | 'xml_isolation'",
  "include_debug": "boolean (optional, default false) — include raw prompt in response"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "summary": "string — the generated summary",
  "technique_used": "string — 'sandwich' | 'xml_isolation'",
  "injection_detected": "boolean — true if input guardrails flagged potential injection",
  "output_flagged": "boolean — true if output guardrails flagged suspicious output",
  "timestamp": "string — ISO 8601 timestamp",
  "debug": {
    "system_prompt": "string (only if include_debug=true)",
    "user_prompt": "string (only if include_debug=true)",
    "raw_response": "string (only if include_debug=true)"
  }
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error": "string — error message",
  "error_type": "string — 'empty_input' | 'too_long' | 'off_topic' | 'invalid_format'"
}
```

**Response (500 Internal Server Error):**
```json
{
  "success": false,
  "error": "string — error message",
  "error_type": "string — 'llm_error' | 'api_timeout' | 'refusal'"
}
```

---

### POST `/api/compare`
> Run the same document through both techniques and return side-by-side results.

**Request:**
```json
{
  "document": "string (required) — the document text to summarize"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "results": {
    "sandwich": {
      "summary": "string",
      "injection_detected": "boolean",
      "output_flagged": "boolean"
    },
    "xml_isolation": {
      "summary": "string",
      "injection_detected": "boolean",
      "output_flagged": "boolean"
    }
  },
  "timestamp": "string — ISO 8601"
}
```

---

### POST `/api/attack-test`
> Run the automated attack suite against a base document.

**Request:**
```json
{
  "base_document": "string (required) — clean document to inject attacks into",
  "attack_types": "string[] (optional) — specific attack types to run, default: all",
  "technique": "string (optional) — 'sandwich' | 'xml_isolation' | 'both', default: 'both'"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "total_attacks": "number",
  "total_passed": "number",
  "total_failed": "number",
  "pass_rate": "number (0-100, percentage)",
  "results": [
    {
      "attack_type": "string — e.g., 'direct_override'",
      "attack_label": "string — human-readable name",
      "injected_text": "string — the injection payload",
      "technique": "string — 'sandwich' | 'xml_isolation'",
      "defended": "boolean — true if attack was blocked",
      "summary_output": "string — what the LLM returned",
      "failure_reason": "string | null — why defense failed (if applicable)"
    }
  ],
  "timestamp": "string — ISO 8601"
}
```

---

### GET `/api/prompt-history`
> Retrieve the timestamped prompt history log.

**Response (200 OK):**
```json
{
  "success": true,
  "entries": [
    {
      "id": "string — UUID",
      "timestamp": "string — ISO 8601",
      "prompt_version": "string — e.g., 'v1', 'v2', 'final'",
      "technique": "string",
      "system_prompt": "string",
      "user_prompt": "string",
      "llm_response": "string",
      "was_attack": "boolean",
      "attack_type": "string | null"
    }
  ],
  "total_entries": "number"
}
```

---

### GET `/api/metrics`
> Retrieve evaluation metrics (v1 vs final comparison).

**Response (200 OK):**
```json
{
  "success": true,
  "metrics": {
    "v1": {
      "pass_rate": "number",
      "attacks_tested": "number",
      "attacks_blocked": "number",
      "prompt_version": "string"
    },
    "final": {
      "pass_rate": "number",
      "attacks_tested": "number",
      "attacks_blocked": "number",
      "prompt_version": "string"
    },
    "improvement": "number — percentage improvement"
  }
}
```

---

## 2. Internal Module Interfaces (Python)

### `llm_service.py` — LLM Service

```python
class LLMService:
    """Wrapper around Google Gemini API."""

    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        """Initialize with API key and model name."""
        ...

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.3,
        max_tokens: int = 1024
    ) -> LLMResponse:
        """
        Send a prompt to Gemini and return the response.

        Returns:
            LLMResponse with fields:
                - text: str (generated text)
                - usage: dict (token counts)
                - model: str (model used)
                - finish_reason: str
        """
        ...
```

**LLMResponse Data Class:**
```python
@dataclass
class LLMResponse:
    text: str
    usage: dict       # {"input_tokens": int, "output_tokens": int}
    model: str
    finish_reason: str  # "stop" | "max_tokens" | "safety"
```

---

### `defense.py` — Defense Engine

```python
class DefenseEngine:
    """Constructs defended prompts using various techniques."""

    def build_prompt(
        self,
        document: str,
        technique: str  # "sandwich" | "xml_isolation"
    ) -> tuple[str, str]:
        """
        Build system_prompt and user_prompt for the given technique.

        Args:
            document: Raw document text (untrusted)
            technique: Which defense technique to use

        Returns:
            (system_prompt: str, user_prompt: str)
        """
        ...

    def get_technique_names(self) -> list[str]:
        """Return list of available technique identifiers."""
        ...
```

---

### `guardrails.py` — Input/Output Guardrails

```python
class InputGuardrail:
    """Validates and sanitizes input before sending to LLM."""

    def validate(self, document: str) -> GuardrailResult:
        """
        Validate input document.

        Returns:
            GuardrailResult:
                - is_valid: bool
                - error_type: str | None  ("empty_input", "too_long", "off_topic", "invalid_format")
                - error_message: str | None
                - sanitized_text: str | None  (cleaned version of input)
                - injection_warning: bool  (true if suspicious patterns detected)
        """
        ...

class OutputGuardrail:
    """Validates LLM output to detect if injection succeeded."""

    def validate(self, original_document: str, summary: str) -> GuardrailResult:
        """
        Check if the LLM output looks like a valid summary.

        Returns:
            GuardrailResult:
                - is_valid: bool
                - flagged: bool  (true if output looks suspicious)
                - flag_reason: str | None
                - cleaned_output: str | None
        """
        ...
```

**GuardrailResult Data Class:**
```python
@dataclass
class GuardrailResult:
    is_valid: bool
    error_type: str | None = None
    error_message: str | None = None
    sanitized_text: str | None = None
    injection_warning: bool = False
    flagged: bool = False
    flag_reason: str | None = None
    cleaned_output: str | None = None
```

---

### `attacks.py` — Attack Suite

```python
class AttackSuite:
    """Automated attack suite for testing defenses."""

    def get_attack_types(self) -> list[AttackType]:
        """Return all available attack type definitions."""
        ...

    def inject_attack(
        self,
        base_document: str,
        attack_type: str
    ) -> str:
        """
        Inject an attack payload into the base document.

        Returns:
            Modified document with injection embedded.
        """
        ...

    async def run_suite(
        self,
        base_document: str,
        defense_engine: DefenseEngine,
        llm_service: LLMService,
        techniques: list[str] = None  # default: all techniques
    ) -> AttackReport:
        """
        Run all attacks against all specified techniques.

        Returns:
            AttackReport with pass/fail for each attack+technique combo.
        """
        ...

    def evaluate_defense(
        self,
        original_document: str,
        injected_document: str,
        summary: str,
        attack_type: str
    ) -> bool:
        """
        Determine if the defense held (True) or failed (False).
        """
        ...
```

**AttackType Data Class:**
```python
@dataclass
class AttackType:
    id: str           # e.g., "direct_override"
    label: str        # e.g., "Direct Instruction Override"
    description: str  # Human-readable description
    payload: str      # The injection text
    expected_if_fail: str  # What the output would look like if attack succeeds
```

---

### `logger.py` — Prompt History Logger

```python
class PromptLogger:
    """Logs all prompts and responses with timestamps."""

    def __init__(self, log_file: str = "logs/prompt_history.json"):
        ...

    def log(
        self,
        system_prompt: str,
        user_prompt: str,
        llm_response: str,
        technique: str,
        prompt_version: str,
        was_attack: bool = False,
        attack_type: str | None = None
    ) -> str:
        """
        Log a prompt-response pair.

        Returns:
            entry_id: str (UUID of the log entry)
        """
        ...

    def get_history(self) -> list[dict]:
        """Return all logged entries."""
        ...

    def export(self, filepath: str = None) -> str:
        """Export log to file. Returns filepath."""
        ...
```

---

## 3. Frontend ↔ Backend Communication

| Action | Method | Endpoint | Owner |
|--------|--------|----------|-------|
| Summarize document | POST | `/api/summarize` | Member 1 (FE) → Member 2 (BE) |
| Compare techniques | POST | `/api/compare` | Member 1 (FE) → Member 2 (BE) |
| Run attack suite | POST | `/api/attack-test` | Member 1 (FE) → Member 4 (BE) |
| View prompt history | GET | `/api/prompt-history` | Member 1 (FE) → Member 2 (BE) |
| View metrics | GET | `/api/metrics` | Member 1 (FE) → Member 2 (BE) |

---

## 4. Environment Variables

```env
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.0-flash
MAX_DOCUMENT_LENGTH=10000
LOG_FILE=logs/prompt_history.json
PORT=8000
```

---

## 5. Error Codes

| Code | Error Type | Description |
|------|-----------|-------------|
| 400 | `empty_input` | Document text is empty or whitespace-only |
| 400 | `too_long` | Document exceeds MAX_DOCUMENT_LENGTH characters |
| 400 | `off_topic` | Input does not appear to be a document |
| 400 | `invalid_format` | Input contains invalid characters or encoding |
| 500 | `llm_error` | Gemini API returned an error |
| 500 | `api_timeout` | Gemini API call timed out |
| 500 | `refusal` | LLM refused to generate a response (safety filter) |
