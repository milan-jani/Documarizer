import json
import os
import uuid
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any


class PromptLogger:
    """Logs all prompts and responses with timestamps and version tracking."""

    def __init__(self, log_file: Optional[str] = None):
        self.log_file = log_file or os.getenv("LOG_FILE", "logs/prompt_history.json")
        # Ensure log directory exists
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        self.entries: List[Dict[str, Any]] = self._load()

    def _load(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
            except Exception as e:
                print(f"[PromptLogger] Warning reading {self.log_file}: {e}")
        return []

    def _save(self) -> None:
        try:
            with open(self.log_file, "w", encoding="utf-8") as f:
                json.dump(self.entries, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[PromptLogger] Error saving log to {self.log_file}: {e}")

    def log(
        self,
        system_prompt: str,
        user_prompt: str,
        llm_response: str,
        technique: str,
        prompt_version: str = "final",
        was_attack: bool = False,
        attack_type: Optional[str] = None,
    ) -> str:
        """
        Log a prompt-response interaction.

        Returns:
            entry_id: str (UUID of the log entry)
        """
        entry_id = str(uuid.uuid4())
        entry = {
            "id": entry_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "prompt_version": prompt_version,
            "technique": technique,
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "llm_response": llm_response,
            "was_attack": was_attack,
            "attack_type": attack_type,
        }
        self.entries.append(entry)
        self._save()
        return entry_id

    def get_history(self) -> List[Dict[str, Any]]:
        """Return all logged entries in reverse chronological order."""
        return list(reversed(self.entries))

    def export(self, filepath: Optional[str] = None) -> str:
        """Export log to a target file."""
        target = filepath or self.log_file
        with open(target, "w", encoding="utf-8") as f:
            json.dump(self.entries, f, indent=2, ensure_ascii=False)
        return target
