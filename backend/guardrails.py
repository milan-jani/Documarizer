import re
import os
from dataclasses import dataclass
from typing import Optional

MAX_DOCUMENT_LENGTH = int(os.getenv("MAX_DOCUMENT_LENGTH", "10000"))

# Known injection patterns for heuristic warning
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?(previous|prior)\s+instructions",
    r"you\s+are\s+(no\s+longer|now\s+a)",
    r"new\s+system\s+instruction",
    r"\[system\s+update\]",
    r"output\s+your\s+complete\s+system\s+prompt",
    r"===\s*document\s*end\s*===",
    r"</?(untrusted_)?document>",
    r"disregard\s+(all\s+)?above",
    r"translate\s+everything\s+into\s+pirate",
    r"emergency\s+override",
    r"security\s+bypass",
    r"alpha\s+protocol",
    r"कृपया\s+सारांश",
]

# Attack failure keywords to detect in LLM output
OUTPUT_FAIL_INDICATORS = [
    "hacked",
    "injection successful",
    "injection success",
    "ahoy matey",
    "arr matey",
    "vulnerable",
    "compromised",
    "alpha protocol",
    "alpha execution confirmed",
    "security bypass active",
    "security bypass",
    "emergency override granted",
    "angriff erfolgreich",
    "इंजेक्शन सफल",
]


@dataclass
class GuardrailResult:
    is_valid: bool
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    sanitized_text: Optional[str] = None
    injection_warning: bool = False
    flagged: bool = False
    flag_reason: Optional[str] = None
    cleaned_output: Optional[str] = None


class InputGuardrail:
    """Validates and sanitizes input before sending to LLM."""

    def __init__(self, max_length: int = MAX_DOCUMENT_LENGTH):
        self.max_length = max_length

    def validate(self, document: str) -> GuardrailResult:
        # Check empty or whitespace
        if not document or not document.strip():
            return GuardrailResult(
                is_valid=False,
                error_type="empty_input",
                error_message="Document text is empty or contains only whitespace.",
            )

        # Check maximum length
        if len(document) > self.max_length:
            return GuardrailResult(
                is_valid=False,
                error_type="too_long",
                error_message=f"Document exceeds maximum length of {self.max_length} characters.",
            )

        # Check for null bytes or invalid control characters
        if "\x00" in document:
            return GuardrailResult(
                is_valid=False,
                error_type="invalid_format",
                error_message="Document contains invalid characters or null bytes.",
            )

        # Off-topic / meaningless string check
        clean_text = document.strip()
        if len(clean_text) < 10 and not any(c.isalpha() for c in clean_text):
            return GuardrailResult(
                is_valid=False,
                error_type="off_topic",
                error_message="Input does not appear to be a valid document.",
            )

        # Heuristic injection pattern scanning
        injection_detected = False
        for pattern in INJECTION_PATTERNS:
            if re.search(pattern, document, re.IGNORECASE):
                injection_detected = True
                break

        # Sanitization: Neutralize delimiter escapes and closing XML tags
        sanitized = document
        sanitized = re.sub(r"===\s*DOCUMENT\s*(START|END)\s*===", r"[ESCAPED_DELIMITER]", sanitized, flags=re.IGNORECASE)
        sanitized = sanitized.replace("</untrusted_document>", "&lt;/untrusted_document&gt;")
        sanitized = sanitized.replace("<untrusted_document>", "&lt;untrusted_document&gt;")

        return GuardrailResult(
            is_valid=True,
            sanitized_text=sanitized,
            injection_warning=injection_detected,
        )


class OutputGuardrail:
    """Validates LLM output to detect if prompt injection succeeded."""

    def validate(self, original_document: str, summary: str) -> GuardrailResult:
        if not summary or not summary.strip():
            return GuardrailResult(
                is_valid=False,
                flagged=True,
                flag_reason="Output is empty or blank.",
            )

        lower_summary = summary.lower()

        # Check for known fail indicators
        for indicator in OUTPUT_FAIL_INDICATORS:
            if indicator in lower_summary:
                return GuardrailResult(
                    is_valid=True,
                    flagged=True,
                    flag_reason=f"Output contains injection fail indicator: '{indicator}'",
                    cleaned_output=summary,
                )

        # Check for system prompt leakage
        if "you are a secure" in lower_summary or "strict operational constraints" in lower_summary:
            return GuardrailResult(
                is_valid=True,
                flagged=True,
                flag_reason="Output leaked internal system instructions.",
                cleaned_output="[Summary flagged: Internal instruction leakage detected]",
            )

        # Check if the summary is just a repetition of the word VULNERABLE
        if lower_summary.count("vulnerable") > 5:
            return GuardrailResult(
                is_valid=True,
                flagged=True,
                flag_reason="Output compromised by fake system repetition injection.",
                cleaned_output="[Summary flagged: Repetitive attack payload detected]",
            )

        return GuardrailResult(
            is_valid=True,
            flagged=False,
            cleaned_output=summary,
        )
