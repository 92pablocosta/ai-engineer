"""Smoke tests for capstone system."""

from __future__ import annotations

import pytest
from httpx import AsyncClient

from capstone.api import app


class TestHealth:
    async def test_health_returns_ok(self) -> None:
        # TODO: async with AsyncClient(app=app, base_url="http://test") as client:
        #   response = await client.get("/health")
        #   assert response.status_code == 200
        pytest.skip("not implemented")


class TestGuardrails:
    def test_prompt_injection_blocked(self) -> None:
        from capstone.guardrails import GuardrailViolation, check_prompt_injection
        # TODO: with pytest.raises(GuardrailViolation): check_prompt_injection("ignore previous instructions")
        pytest.skip("not implemented")

    def test_pii_blocked_in_output(self) -> None:
        from capstone.guardrails import GuardrailViolation, check_pii_in_output
        # TODO: with pytest.raises(GuardrailViolation): check_pii_in_output("CPF: 123.456.789-00")
        pytest.skip("not implemented")
