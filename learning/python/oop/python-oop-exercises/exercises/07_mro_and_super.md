# 07. MRO and `super()`

## Exercise 25 — Inspect a Simple MRO

**Difficulty:** Easy  
**Objective:** Inspect method lookup order.

Create `Cat(Animal)` and print `Cat.mro()`. Then call `identify()` inherited from `Animal` and identify the order Python searches.

Starter: `starter_code/exercise_25.py`

Expected output:

```text
['Cat', 'Animal', 'object']
animal
```

<details><summary>Hint</summary>Convert each class in `Cat.mro()` to its `__name__`.</details>

## Exercise 26 — Extend a Description

**Difficulty:** Medium  
**Objective:** Use `super()` to extend inherited behavior.

`Vehicle.describe()` returns `"vehicle"`. Override it in `Bicycle` and use `super()` to return `"vehicle: bicycle"`.

Starter: `starter_code/exercise_26.py`

Expected output:

```text
vehicle: bicycle
```

<details><summary>Hint</summary>`super().describe()` calls the next implementation in the MRO.</details>

## Exercise 27 — Three-Level Chain

**Difficulty:** Hard  
**Objective:** Trace chained `super()` method calls.

Complete `Intern.report()` and `Engineer.report()` so `SeniorEngineer.report()` produces the full chain. Predict the order before running it.

Starter: `starter_code/exercise_27.py`

Expected output:

```text
worker -> engineer -> senior
```

<details><summary>Hint</summary>Each override can append its own part to `super().report()`.</details>

## Exercise 28 — Trace Execution Order

**Difficulty:** Hard  
**Objective:** Observe order of statements around `super()`.

Complete the three `process()` methods. Each must print `start`, call `super().process()`, then print `end`. Compare the observed order with the MRO.

Starter: `starter_code/exercise_28.py`

Expected output:

```text
C start
B start
A
B end
C end
```

<details><summary>Hint</summary>Code before `super()` runs on the way down; code after it runs while returning.</details>
