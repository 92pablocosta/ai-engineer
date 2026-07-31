# 03. Encapsulation

## Exercise 09 — Safe Bank Withdrawal

**Difficulty:** Medium  
**Objective:** Control state changes with validation.

Complete `BankAccount.withdraw(amount)`. It should return `True` and decrease `_balance` only for a positive amount that is available; otherwise return `False` without changing state.

Starter: `starter_code/exercise_09.py`

Expected output:

```text
True
False
70
```

<details><summary>Hint</summary>Test all rules before assigning a new balance.</details>

## Exercise 10 — Valid Product Discount

**Difficulty:** Medium  
**Objective:** Validate a rule before modifying an internal attribute.

Implement `Product.apply_discount(percent)`. Accept values from 0 through 100 inclusive. Return whether the price changed; an invalid discount must leave `_price` untouched.

Starter: `starter_code/exercise_10.py`

Expected output:

```text
True
80.0
False
80.0
```

<details><summary>Hint</summary>For a percent `p`, the remaining factor is `1 - p / 100`.</details>

## Exercise 11 — AttributeError or ValueError?

**Difficulty:** Easy  
**Objective:** Distinguish missing behavior from invalid data.

Run the starter and label each marked failure as `AttributeError` or `ValueError`. Then fix the code so it prints the expected messages using `try`/`except`.

Starter: `starter_code/exercise_11.py`

Expected output:

```text
missing method: AttributeError
invalid age: ValueError
```

<details><summary>Hint</summary>Calling a name an object lacks differs from rejecting a supplied value.</details>

## Exercise 12 — Compare Two Setters

**Difficulty:** Medium  
**Objective:** Explain why encapsulated updates are safer.

The starter shows direct assignment and a `set_level()` method. Complete the method to accept levels 1–5, then explain why `game._level = 99` can still work even though it breaks the class rule.

Starter: `starter_code/exercise_12.py`

Expected output:

```text
False
1
True
4
```

<details><summary>Hint</summary>A leading underscore is a convention; the validation lives in the method.</details>
