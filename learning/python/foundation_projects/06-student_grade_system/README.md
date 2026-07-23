# 6. Student Grade System

## Objective

Create a system that registers students, their grades, and their academic results — including generating a full class report to a file.

## Suggested Data Structure

```python
student = {
    "name": "Ana",
    "grades": [8.5, 7.0, 9.0],
    "average": 8.16,
    "status": "approved"
}
```

## Minimum Features

- Register multiple students.
- Register multiple grades for each student.
- Calculate each student's average.
- Classify students as: Approved, Recovery, Failed.
- Display the best-performing student.
- Display a complete class report.
- Write the class report to a new output file.
- Validate names and grades.

## Concepts Practiced

- Lists of dictionaries, functions, calculations, conditions, formatting, file handling, data traversal

## Extra Challenge

Allow the user to search for a student by name, and load/save the class roster from a file so it persists between runs.
