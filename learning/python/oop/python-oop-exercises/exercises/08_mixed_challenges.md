# 08. Mixed OOP Challenges

## Exercise 29 — Reading Tracker

**Difficulty:** Medium  
**Objective:** Design a class with state, commands, queries, and validation.

Implement `ReadingTracker` with internal `_pages_read`, `read_pages(amount)`, and `get_pages_read()`. Ignore non-positive amounts. Demonstrate valid and invalid updates.

Starter: `starter_code/exercise_29.py`

Expected output:

```text
15
15
```

<details><summary>Hint</summary>Keep the validation inside the command method.</details>

## Exercise 30 — Checkout Collaborators

**Difficulty:** Hard  
**Objective:** Make small objects delegate work to each other.

Complete `ShoppingCart` and `ReceiptPrinter`. The cart stores `Product` objects, calculates its total, then delegates printing to an object with `print_receipt(total)`. Do not make the cart format the receipt itself.

Starter: `starter_code/exercise_30.py`

Expected output:

```text
Total: 12.50
```

<details><summary>Hint</summary>The cart should call a method on the printer object.</details>

## Exercise 31 — Delivery Options

**Difficulty:** Hard  
**Objective:** Combine inheritance, overriding, and polymorphism.

Create `StandardDelivery` and `ExpressDelivery` subclasses of `Delivery`, overriding `estimate_days()`. Iterate over both options and print their estimates through the common method.

Starter: `starter_code/exercise_31.py`

Expected output:

```text
standard: 5 days
express: 2 days
```

<details><summary>Hint</summary>Store the label on each delivery object, then override only the estimate.</details>

## Exercise 32 — Notification Pipeline

**Difficulty:** Hard  
**Objective:** Design a duck-typed collaboration with validation and polymorphism.

Implement `NotificationService.send_all(message, channels)`. Reject an empty message with `ValueError`; otherwise call `send(message)` on every channel. Use unrelated `EmailChannel` and `LogChannel` classes. Then explain the behavioral contract of a channel.

Starter: `starter_code/exercise_32.py`

Expected output:

```text
email: Welcome
log: Welcome
empty message: ValueError
```

<details><summary>Hint</summary>The service only needs each channel to supply a `send` method.</details>
