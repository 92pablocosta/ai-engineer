"""Production guardrails — OWASP LLM Top 10 mitigations.

Focus on:
  1. Prompt injection detection (LLM01)
  2. Data leakage prevention / PII filter (LLM02)
  3. Insecure output handling — no code exec from LLM output (LLM05)
"""

from __future__ import annotations


class GuardrailViolation(Exception):
    def __init__(self, rule: str, detail: str) -> None:
        self.rule = rule
        self.detail = detail
        super().__init__(f"[{rule}] {detail}")


def check_prompt_injection(user_input: str) -> None:
    """Detect common prompt injection patterns. Raise if found."""
    # TODO: check for "ignore previous instructions", "you are now", jailbreak patterns
    raise NotImplementedError


def check_pii_in_output(output: str) -> None:
    """Block PII from reaching the user. Raise if found."""
    # TODO: CPF, phone, email, credit card patterns
    raise NotImplementedError


def check_output_is_safe(output: str) -> None:
    """Ensure LLM output is not executable code being passed to eval/exec."""
    # TODO: detect if output looks like it's trying to inject code
    raise NotImplementedError
