"""Exercise 02 — Tools with typed Pydantic schemas.

Goal: design tools the LLM will call correctly.
  1. Define input schemas with Pydantic — the schema IS the LLM contract.
  2. Write descriptions that remove ambiguity (test: would a different LLM call it wrong?).
  3. Make tools idempotent where possible.
  4. Test that Pydantic rejects bad input before it reaches tool logic.

Run: uv run python exercises/02_typed_tools.py
"""

from __future__ import annotations

from pydantic import BaseModel, Field


# TODO: implement 3 tools for a support/scheduling domain, e.g.:

class CheckAvailabilityInput(BaseModel):
    """Input for check_availability tool."""
    # TODO: define fields with descriptions the LLM can follow
    # doctor_id: str = Field(..., description="...")
    # date: str = Field(..., description="ISO 8601 date, e.g. 2026-06-15")
    pass


class CreateReminderInput(BaseModel):
    """Input for create_reminder tool."""
    # TODO: define fields
    pass


class EscalateToHumanInput(BaseModel):
    """Input for escalate_to_human tool."""
    # TODO: define fields — reason is mandatory
    pass


def check_availability(input: CheckAvailabilityInput) -> dict:
    """Return available appointment slots for a doctor on a given date."""
    # TODO: mock implementation — return list of time slots
    raise NotImplementedError


def create_reminder(input: CreateReminderInput) -> dict:
    """Schedule a reminder. Idempotent: same reminder_id = update, not duplicate."""
    # TODO: mock implementation
    raise NotImplementedError


def escalate_to_human(input: EscalateToHumanInput) -> dict:
    """Flag conversation for human review."""
    # TODO: mock implementation
    raise NotImplementedError


def tool_schemas() -> list[dict]:
    """Generate tool schemas from Pydantic models for LLM API."""
    # TODO: use model.model_json_schema() and wrap in tool format
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: test that bad input raises ValidationError before reaching tool
    try:
        bad = CheckAvailabilityInput()  # type: ignore
    except Exception as e:
        print(f"ValidationError caught (expected): {e}")
