"""Exercise 03 — Output guardrails.

Goal: validate agent output before it reaches the user.
  1. PII filter: agent must never return CPF, phone, or email in plaintext.
  2. Action guard: destructive actions (cancel, delete) require explicit confirmation flag.
  3. Test both guardrails — one that passes, one that fires.

Run: uv run python exercises/03_output_guardrail.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass


# Patterns to detect — adjust to your domain
PII_PATTERNS: list[re.Pattern[str]] = [
    # TODO: add regex for CPF (000.000.000-00), phone, email
]

DESTRUCTIVE_ACTIONS = {"cancel_appointment", "delete_patient", "clear_history"}


@dataclass
class GuardrailResult:
    passed: bool
    violations: list[str]


def pii_guardrail(text: str) -> GuardrailResult:
    """Block output containing PII patterns."""
    # TODO: scan text against PII_PATTERNS, return violations list
    raise NotImplementedError


def action_guardrail(action_name: str, confirmed: bool) -> GuardrailResult:
    """Block destructive actions without explicit confirmation."""
    # TODO: if action_name in DESTRUCTIVE_ACTIONS and not confirmed → violation
    raise NotImplementedError


def apply_guardrails(output: str, action: str | None = None, confirmed: bool = False) -> str:
    """Apply all guardrails. Return output if passes, raise GuardrailViolation if not."""
    # TODO: run pii_guardrail + action_guardrail (if action provided)
    # If any violation: raise GuardrailViolation(violations)
    raise NotImplementedError


class GuardrailViolation(Exception):
    def __init__(self, violations: list[str]) -> None:
        self.violations = violations
        super().__init__(f"Guardrail violations: {violations}")


if __name__ == "__main__":
    # TODO: test cases:
    # 1. apply_guardrails("Your CPF is 123.456.789-00") → should raise
    # 2. apply_guardrails("Appointment cancelled.", action="cancel_appointment", confirmed=False) → should raise
    # 3. apply_guardrails("Done.", action="cancel_appointment", confirmed=True) → should pass
    pass
