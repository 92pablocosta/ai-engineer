# 04. Inheritance

## Exercise 13 — Employee and Manager

**Difficulty:** Easy  
**Objective:** Inherit a method from a superclass.

Create `Manager` as a subclass of `Employee`. It adds no behavior, so use `pass`. Instantiate it, assign a name, and call the inherited `introduce()` method.

Starter: `starter_code/exercise_13.py`

Expected output:

```text
I am Lin
```

<details><summary>Hint</summary>Put the superclass in parentheses after the subclass name.</details>

## Exercise 14 — Animal Sounds

**Difficulty:** Easy  
**Objective:** Recognize inherited behavior.

Complete `Dog` as a subclass of `Animal`. Do not add a method. Run it and explain where `move()` is found.

Starter: `starter_code/exercise_14.py`

Expected output:

```text
Dog moves
```

<details><summary>Hint</summary>Python looks on the object’s class, then its superclass.</details>

## Exercise 15 — Member Card

**Difficulty:** Medium  
**Objective:** Use a subclass as a more specific type.

Create `PremiumMember(Member)` with `pass`. The superclass has `show_status()`. Make the premium object show its inherited state.

Starter: `starter_code/exercise_15.py`

Expected output:

```text
Mia: active
```

<details><summary>Hint</summary>Instances can receive attributes after construction if the class does not initialize them.</details>

## Exercise 16 — Library Items

**Difficulty:** Medium  
**Objective:** Add a subclass while preserving shared behavior.

`LibraryItem` has `borrow()` and `return_item()`. Create `Magazine(LibraryItem)` with no additional behavior and show a magazine being borrowed, then returned.

Starter: `starter_code/exercise_16.py`

Expected output:

```text
True
False
```

<details><summary>Hint</summary>Call inherited methods through the magazine instance.</details>
