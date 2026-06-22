"""Tests for guardrails."""

from __future__ import annotations

import pytest

from support_agent.guardrails import GuardrailViolation, check_action, check_output


class TestOutputGuardrail:
    def test_clean_output_passes(self) -> None:
        # TODO: check_output("Sua consulta está confirmada.") should not raise
        pytest.skip("not implemented")

    def test_cpf_blocked(self) -> None:
        # TODO: with pytest.raises(GuardrailViolation): check_output("CPF: 123.456.789-00")
        pytest.skip("not implemented")


class TestActionGuardrail:
    def test_safe_action_passes(self) -> None:
        # TODO: check_action("get_faq", confirmed=False) should not raise
        pytest.skip("not implemented")

    def test_destructive_without_confirmation_blocked(self) -> None:
        # TODO: with pytest.raises(GuardrailViolation):
        #   check_action("cancel_appointment", confirmed=False)
        pytest.skip("not implemented")

    def test_destructive_with_confirmation_passes(self) -> None:
        # TODO: check_action("cancel_appointment", confirmed=True) should not raise
        pytest.skip("not implemented")
