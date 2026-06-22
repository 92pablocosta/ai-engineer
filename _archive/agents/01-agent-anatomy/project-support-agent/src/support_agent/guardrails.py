"""Input/output guardrails."""

from __future__ import annotations

import re


DESTRUCTIVE_ACTIONS = {"cancel_appointment", "delete_record"}
PII_PATTERNS = [
    # TODO: CPF, phone, email regexes
]


class GuardrailViolation(Exception):
    def __init__(self, violations: list[str]) -> None:
        self.violations = violations
        super().__init__("; ".join(violations))


def check_output(text: str) -> None:
    """Raise GuardrailViolation if output contains PII."""
    # TODO: implement
    raise NotImplementedError


def check_action(action_name: str, confirmed: bool) -> None:
    """Raise GuardrailViolation if destructive action called without confirmation."""
    # TODO: implement
    raise NotImplementedError
