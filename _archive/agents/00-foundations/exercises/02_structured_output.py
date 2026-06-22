"""Exercise 02 — Structured output with Pydantic.

Goal: force LLM to return validated structured data instead of free text.
  1. Define a Pydantic model for your target structure.
  2. Use tool calling / JSON mode to get structured output.
  3. Validate with Pydantic — handle ValidationError gracefully.
  4. Show the difference between .model_validate() and manual string parsing.

Run: uv run python exercises/02_structured_output.py
"""

from __future__ import annotations

from pydantic import BaseModel, ValidationError


# TODO: define extraction target, e.g.:
# class Invoice(BaseModel):
#     vendor: str
#     amount: float
#     date: str
#     currency: str = "BRL"


SAMPLE_TEXTS = [
    "Nota fiscal da TechCorp, valor R$ 1.250,00, emitida em 03/06/2026.",
    "This text has no invoice data — should raise ValidationError.",
]


def extract(text: str) -> None:
    """Extract structured data from text and validate."""
    # TODO:
    # 1. Build prompt asking LLM to extract fields as JSON
    # 2. Call API with json_mode or tool schema
    # 3. Parse response, call YourModel.model_validate(data)
    # 4. Print success or catch + print ValidationError details
    raise NotImplementedError


if __name__ == "__main__":
    for text in SAMPLE_TEXTS:
        print(f"\nInput: {text}")
        extract(text)
