# 01. Classes, Objects and State

## Exercise 01 — First Book Object

**Difficulty:** Easy  
**Objective:** Create a class and instantiate objects.

Create a `Book` class with `title` and `author` attributes. Create two books, assign values through dot notation, and print both titles.

Starter: `starter_code/exercise_01.py`

Expected output:

```text
Dune
Kindred
```

<details><summary>Hint</summary>Attributes can be created on an instance with `object.attribute = value`.</details>

## Exercise 02 — Car State

**Difficulty:** Easy  
**Objective:** Initialize instance state with `__init__`.

Complete `Car` so each object receives a `brand` and starts with `mileage` equal to zero. Update one car's mileage and print both states.

Starter: `starter_code/exercise_02.py`

Expected output:

```text
Toyota: 120
Honda: 0
```

<details><summary>Hint</summary>`__init__` receives the new object as `self` automatically.</details>

## Exercise 03 — Predict Shared or Separate State

**Difficulty:** Easy  
**Objective:** Reason about state belonging to each object.

Before running the starter, predict its output. Then explain why changing `first_player.score` does not change `second_player.score`.

Starter: `starter_code/exercise_03.py`

Expected output:

```text
10
0
```

<details><summary>Hint</summary>Each call to a class creates a different object.</details>

## Exercise 04 — Fix the Missing Attribute

**Difficulty:** Medium  
**Objective:** Diagnose and fix an `AttributeError` caused by incomplete initialization.

The starter tries to print an account owner's name. Complete the class so the script runs and prints the expected result. State which attribute caused the original error.

Starter: `starter_code/exercise_04.py`

Expected output:

```text
Owner: Ada
```

<details><summary>Hint</summary>Every attribute later read by a method should be assigned before that read.</details>
