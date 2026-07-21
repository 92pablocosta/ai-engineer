# 3. Command-Line Calculator

## Objective

Create a calculator that parses expressions typed as plain text (e.g. `10 + 5`) without using `eval()`.

## Minimum Features

- Read the full expression as one input.
- Split it manually into operands and operator.
- Route the operation to a dedicated function per operator (`add`, `subtract`, `multiply`, `divide`).
- Loop until the user chooses to exit.
- Handle division by zero and malformed expressions.

## Concepts Practiced

- Functions, string parsing, `try`/`except` (`ZeroDivisionError`, `ValueError`), loops

## Extra Challenge

Support expressions with more than two operands (e.g. `10 + 5 - 3`).
