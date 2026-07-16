# 2. CPF/CNPJ Validator

## Objective

Create a function that receives a string and validates whether it is a properly formatted CPF or CNPJ, including check digits — without using any external library.

## Minimum Features

- Strip formatting characters (dots, dashes, slashes) before validating.
- Reject strings with wrong length or non-numeric characters.
- Calculate check digits manually using the official algorithm.
- Return a clear True/False plus a reason when invalid.
- Handle empty input and non-string input without crashing.

## Concepts Practiced

- Functions, string manipulation, loops, `try`/`except`, boolean logic

## Extra Challenge

Detect automatically whether the input is a CPF (11 digits) or CNPJ (14 digits) and validate accordingly.
