"""Support agent tools with typed Pydantic schemas."""

from __future__ import annotations

from pydantic import BaseModel, Field


class CheckAvailabilityInput(BaseModel):
    doctor_id: str = Field(..., description="Doctor's unique identifier")
    date: str = Field(..., description="ISO 8601 date, e.g. 2026-06-15")


class CreateReminderInput(BaseModel):
    patient_id: str = Field(..., description="Patient's unique identifier")
    appointment_id: str = Field(..., description="Appointment to remind about")
    message: str = Field(..., description="Reminder message text")


class GetFaqInput(BaseModel):
    topic: str = Field(..., description="FAQ topic, e.g. 'payment', 'cancellation', 'hours'")


class EscalateToHumanInput(BaseModel):
    reason: str = Field(..., description="Why this conversation needs human attention")


async def check_availability(inp: CheckAvailabilityInput) -> dict:
    # TODO: query real availability data or return mock slots
    raise NotImplementedError


async def create_reminder(inp: CreateReminderInput) -> dict:
    # TODO: store reminder in DB or call external service
    raise NotImplementedError


async def get_faq(inp: GetFaqInput) -> dict:
    # TODO: look up FAQ from a small hardcoded dict or DB table
    raise NotImplementedError


async def escalate_to_human(inp: EscalateToHumanInput) -> dict:
    # TODO: log escalation, notify via webhook or DB flag
    raise NotImplementedError


def get_tool_schemas() -> list[dict]:
    """Return tool schemas for the LLM API."""
    # TODO: build from Pydantic model_json_schema()
    raise NotImplementedError
