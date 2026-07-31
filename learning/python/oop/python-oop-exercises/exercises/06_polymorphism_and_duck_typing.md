# 06. Polymorphism and Duck Typing

## Exercise 21 — Render a List of Shapes

**Difficulty:** Medium  
**Objective:** Use one method call with objects of different classes.

Create `Circle` and `Square`, each with `draw()`. Iterate through a list of both and call `draw()` without checking their classes.

Starter: `starter_code/exercise_21.py`

Expected output:

```text
circle
square
```

<details><summary>Hint</summary>Polymorphism lets the loop use the shared method name.</details>

## Exercise 22 — A Polymorphic Function

**Difficulty:** Medium  
**Objective:** Pass different objects to the same function.

Complete `announce(device)` so it calls `device.status()`. Use a `Phone` and a `Laptop` that return different status text.

Starter: `starter_code/exercise_22.py`

Expected output:

```text
phone online
laptop charging
```

<details><summary>Hint</summary>The function does not need `isinstance` checks.</details>

## Exercise 23 — Duck-Typed Save

**Difficulty:** Medium  
**Objective:** Depend on available behavior rather than inheritance.

Write `save_document(storage, text)` to call `storage.save(text)`. Demonstrate it with two unrelated classes, `MemoryStorage` and `ConsoleStorage`.

Starter: `starter_code/exercise_23.py`

Expected output:

```text
memory: note
console: note
```

<details><summary>Hint</summary>No shared superclass is necessary when both objects provide `save`.</details>

## Exercise 24 — Missing Duck-Typed Method

**Difficulty:** Easy  
**Objective:** Explain an `AttributeError` in a duck-typed function.

Run the function with `BrokenStorage`, which has no `save()` method. Catch the error and print the expected line. State the informal contract required by `save_document`.

Starter: `starter_code/exercise_24.py`

Expected output:

```text
storage must provide save: AttributeError
```

<details><summary>Hint</summary>The contract is based on a method name, not a parent class.</details>
