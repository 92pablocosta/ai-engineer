# 05. Method Overriding

## Exercise 17 — Different Greetings

**Difficulty:** Easy  
**Objective:** Override an inherited method.

`Person.greet()` is already defined. Override it in `Student` so each object produces a different greeting.

Starter: `starter_code/exercise_17.py`

Expected output:

```text
Hello
Hello, teacher!
```

<details><summary>Hint</summary>The subclass method needs the same name and a compatible parameter list.</details>

## Exercise 18 — Shape Areas

**Difficulty:** Medium  
**Objective:** Override behavior that depends on subclass state.

`Shape.area()` returns zero. Implement `Rectangle.area()` using `width` and `height`. Do not add an `__init__`; assign attributes after creating the object.

Starter: `starter_code/exercise_18.py`

Expected output:

```text
12
```

<details><summary>Hint</summary>Overriding does not require calling the superclass implementation.</details>

## Exercise 19 — Fix the Non-Override

**Difficulty:** Medium  
**Objective:** Identify why a method is not overriding.

The starter expects `EmailNotification.send()` to replace `Notification.send()`, but it does not. Fix the bug and explain why inheritance is required for overriding.

Starter: `starter_code/exercise_19.py`

Expected output:

```text
Email sent
```

<details><summary>Hint</summary>Check both the class relationship and the spelling of the method name.</details>

## Exercise 20 — Compare Replacement and Extension

**Difficulty:** Medium  
**Objective:** Compare two valid override strategies.

Implement `LoudAlarm.ring()` so it fully replaces the base message. Then implement `LoggedAlarm.ring()` so it extends the base behavior using an ordinary call to the inherited method (not `super()` yet). Explain the different outputs.

Starter: `starter_code/exercise_20.py`

Expected output:

```text
LOUD ALARM
alarm
logged
```

<details><summary>Hint</summary>At this stage, an inherited implementation can be called as `Alarm.ring(self)`.</details>
