# 02. Methods, Commands and Queries

## Exercise 05 — Counter Commands

**Difficulty:** Easy  
**Objective:** Write methods that modify state.

Complete `Counter.increment()` and `Counter.reset()`. They are commands: they change state and should not explicitly return a value.

Starter: `starter_code/exercise_05.py`

Expected output:

```text
None
2
0
```

<details><summary>Hint</summary>A function without `return` evaluates to `None`.</details>

## Exercise 06 — Temperature Query

**Difficulty:** Easy  
**Objective:** Write a query method that reads state without modifying it.

Add `is_freezing()` to `Temperature`. It returns `True` when Celsius is at or below zero. Verify that calling it leaves `celsius` unchanged.

Starter: `starter_code/exercise_06.py`

Expected output:

```text
True
0
```

<details><summary>Hint</summary>Queries normally use `return` and do not assign to an attribute.</details>

## Exercise 07 — Wallet Deposit and Balance

**Difficulty:** Medium  
**Objective:** Combine commands and queries.

Implement a `Wallet` with `deposit(amount)` and `get_balance()`. Deposit 25 into a wallet that starts at 10. Identify which method is a command and which is a query.

Starter: `starter_code/exercise_07.py`

Expected output:

```text
35
```

<details><summary>Hint</summary>Only the command needs to change `self.balance`.</details>

## Exercise 08 — Refactor a Procedural Timer

**Difficulty:** Medium  
**Objective:** Move related state and behavior into a class.

Refactor the starter's elapsed-seconds variable and functions into a `Timer` class with `tick()` and `get_seconds()`. Do not use global state.

Starter: `starter_code/exercise_08.py`

Expected output:

```text
3
```

<details><summary>Hint</summary>The former global value should become an instance attribute.</details>
