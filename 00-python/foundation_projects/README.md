# Python Practice Projects Guide (Merged Edition)

## Context

This guide contains **16 practical projects** for students who have completed **Python World 3** from Curso em Vídeo. It merges two project sets: the original 10-project guide and 10 additional suggestions, with overlapping concepts (contacts, grades, inventory, logs) consolidated into a single project + extra challenge instead of duplicated.

The projects are organized in increasing difficulty and focus on consolidating:

- Tuples
- Lists
- Dictionaries
- Functions
- Modules
- File handling
- Exception handling
- Input validation
- Data organization
- Basic software architecture

The recommendation is to build the projects using only Python's standard library before introducing frameworks, databases, or graphical interfaces.

---

# General Development Rules

Apply these rules to every project:

1. Use English names for variables, functions, files, and modules.
2. Place important operations inside functions.
3. Validate all user input.
4. Handle predictable errors explicitly with `try` and `except`.
5. Avoid putting the entire program inside `main.py`.
6. Separate responsibilities whenever the project becomes larger.
7. Make the program work first, then refactor it.
8. Add comments only when the code is not self-explanatory.
9. Use constants for fixed values.
10. Create a `README.md` for the larger projects.

---

# 1. Number Analyzer

## Objective

Create a terminal program that receives several numbers and generates statistics about them.

## Minimum Features

- Register numbers until the user chooses to stop.
- Display the largest number.
- Display the smallest number.
- Calculate the sum.
- Calculate the average.
- Separate even and odd numbers.
- Display numbers in ascending order.
- Reject invalid input without crashing.

## Concepts Practiced

- Lists, loops, functions, conditions, `try`/`except`, `min()`, `max()`, `sum()`, sorting

## Extra Challenge

Remove duplicated values while preserving their original order.

---

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

---

# 3. Command-Line Calculator

## Objective

Create a calculator that parses expressions typed as plain text (e.g. `10 + 5`) without using `eval()`.

## Minimum Features

- Read the full expression as one input.
- Split it manually into operands and operator.
- Route the operation to a dedicated function per operator (`add`, `subtract`, `multiply`, `divide`).
- Loop until the user chooses to exit.
- Handle division by zero and malformed expressions.

## Concepts Practiced

- Functions, string parsing, `try`/`except` (`ZeroDivisionError`, `ValueError`), loops

## Extra Challenge

Support expressions with more than two operands (e.g. `10 + 5 - 3`).

---

# 4. Hangman Game

## Objective

Create a terminal Hangman game where the program picks a secret word and the player guesses letters.

## Minimum Features

- Pick a random word from a list or file.
- Track guessed letters and remaining attempts.
- Display the word progress (`_ y t _ o n`) after each guess.
- Reject invalid input (more than one character, repeated guesses).
- End the game with a win/loss message.

## Concepts Practiced

- Functions, loops, conditions, lists, `try`/`except`, the `random` module

## Extra Challenge

Load the word list from a `.txt` file and pick a category before each round.

---

# 5. Login System with File Persistence

## Objective

Create a signup/login system where user credentials are saved to a file and persist across runs.

## Minimum Features

- Register a username and password, saved to `.txt` or `.json`.
- Authenticate a user against the stored credentials.
- List registered usernames (never passwords in plain view).
- Handle `FileNotFoundError` gracefully on first run (create the file).
- Reject duplicate usernames and empty fields.

## Concepts Practiced

- Functions, file handling, `try`/`except`, dictionaries, basic data persistence

## Extra Challenge

Lock the account after 3 failed login attempts within the same session.

---

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

---

# 7. Contact Manager

## Objective

Create a terminal-based CRUD application for managing contacts.

CRUD means:

- **Create:** register data
- **Read:** display data
- **Update:** modify data
- **Delete:** remove data

## Minimum Features

- Register name, phone number, and email.
- List all contacts.
- Search contacts by name.
- Update phone number or email.
- Delete a contact.
- Reject empty fields.
- Return clear messages when a contact is not found.

## Suggested Data Structure

```python
contact = {
    "name": "Maria",
    "phone": "83999999999",
    "email": "maria@example.com"
}
```

## Concepts Practiced

- Dictionaries, lists, functions, menus, search operations, CRUD, input validation

## Extra Challenge

Prevent two contacts from using the same email address, and persist the contact list to a `.json` file between runs.

---

# 8. Currency Converter (Custom Module)

## Objective

Build a conversion module (`converter.py`) with functions for currency conversion (BRL→USD, USD→EUR, etc.) and import it into a separate `main.py` that handles the menu/interaction.

## Minimum Features

- One function per conversion pair, or a generic function that takes a rate table.
- `main.py` imports and uses the module — no conversion logic duplicated there.
- Reject negative or non-numeric amounts.
- Display the converted value formatted to 2 decimal places.

## Concepts Practiced

- Modules, `import`, functions, separation of responsibilities, `try`/`except`

## Extra Challenge

Load exchange rates from a `.json` file instead of hardcoding them, so rates can be updated without touching the code.

---

# 9. Quiz Game

## Objective

Create a question-and-answer game with scoring.

## Suggested Data Structure

```python
question = {
    "statement": "Which keyword creates a function in Python?",
    "options": ["func", "def", "function", "method"],
    "answer": 1
}
```

## Minimum Features

- Store questions in a list.
- Display multiple-choice answers.
- Validate the selected option.
- Calculate the final score.
- Display the percentage of correct answers.
- Show which questions were answered incorrectly.
- Prevent invalid options.

## Concepts Practiced

- Lists of dictionaries, tuples, functions, loops, conditions, indexes, score calculation

## Extra Challenge

Randomize the question order using the `random` module.

---

# 10. Inventory Control System

## Objective

Create a system for managing products, prices, and stock quantities, using a **custom exception** for stock violations instead of just returning an error message.

## Suggested Data Structure

```python
product = {
    "id": 1,
    "name": "Keyboard",
    "price": 150.00,
    "quantity": 8
}
```

## Minimum Features

- Register products with an auto-generated sequential ID.
- Update product information.
- Add units to stock.
- Remove units from stock.
- Search by product name or ID.
- Display products with zero stock.
- Display products with low stock.
- Calculate the total inventory value.
- Define a custom exception (e.g. `InsufficientStockError`) and raise it when trying to remove more units than available — do not just `return False`.

## Concepts Practiced

- Lists, dictionaries, functions, calculations, validation, search, business rules, **custom exception classes**

## Extra Challenge

Persist the inventory to a `.json` file, and log every stock change (add/remove) to a separate transaction history.

---

# 11. Personal Finance Manager

## Objective

Create a system for registering income and expenses.

## Suggested Data Structure

```python
transaction = {
    "description": "Internet bill",
    "category": "bills",
    "type": "expense",
    "amount": 120.00
}
```

## Minimum Features

- Register a transaction with description, category, type, and amount.
- List all transactions.
- Calculate total income.
- Calculate total expenses.
- Calculate the current balance.
- Filter transactions by category.
- Display the largest expense.
- Reject invalid or negative amounts.

## Concepts Practiced

- Functions, lists, dictionaries, filters, calculations, exceptions, business rules

## Extra Challenge

Save transactions in a `.json` or `.csv` file.

---

# 12. Mini Text Processor

## Objective

Build a set of pure functions that process a block of text read from a `.txt` file.

## Minimum Features

- Read the source `.txt` file.
- Count total words.
- Count total characters (with/without spaces).
- Find the most frequent word.
- Find-and-replace a term (case-sensitive and case-insensitive modes).
- Save the processed result to a new output file.
- Each operation is a pure function that receives the text as a parameter (no global state).

## Concepts Practiced

- File handling, string methods, dictionaries (word frequency), functions, `try`/`except` (missing file)

## Extra Challenge

Add a function that generates a word-frequency report sorted from most to least common.

---

# 13. Log File Analyzer

## Objective

Read a text log file and generate a structured report.

## Example Log

```text
2026-07-07 INFO User logged in
2026-07-07 ERROR Database connection failed
2026-07-07 WARNING Invalid login attempt
```

## Minimum Features

- Read the file line by line.
- Split each line into: date, log level, message.
- Count `INFO`, `WARNING`, and `ERROR` occurrences.
- List only the error messages.
- Identify the most frequent message type.
- Handle a missing file.
- Ignore malformed lines instead of crashing.
- Generate a report file with the summary.

## Concepts Practiced

- File handling, strings, dictionaries, functions, exceptions, parsing, report generation

## Extra Challenge

Filter the report by a given date range or log level passed as a command-line argument (`sys.argv`).

---

# 14. Persistent Task Manager

## Objective

Create a Todo List that preserves its data after the program closes.

## Suggested Data Structure

```python
task = {
    "id": 1,
    "description": "Study Python",
    "completed": False
}
```

## Minimum Features

- Create a task.
- List all tasks.
- Mark a task as completed.
- Edit a task description.
- Delete a task.
- Filter pending tasks.
- Filter completed tasks.
- Save tasks automatically.
- Load saved tasks when the program starts.
- Handle missing or corrupted files.

## Concepts Practiced

- File handling, JSON, functions, modules, exceptions, CRUD, data persistence

## Extra Challenge

Add: priority, creation date, due date, task category.

---

# 15. Modular Banking System

## Objective

Simulate basic banking operations using multiple Python modules.

## Minimum Features

- Create an account.
- Search for an account.
- Display account balance.
- Deposit money.
- Withdraw money.
- Transfer money between accounts.
- Record transaction history.
- Reject negative values.
- Block withdrawals without sufficient balance.
- Handle non-existing accounts.
- Save account data in a file.

## Suggested Structure

```text
bank_system/
├── main.py
├── accounts.py
├── transactions.py
├── storage.py
├── validators.py
├── data/
│   └── accounts.json
└── README.md
```

## Suggested Account Structure

```python
account = {
    "number": 1001,
    "owner": "Pablo Costa",
    "balance": 500.00,
    "transactions": []
}
```

## Concepts Practiced

- Modules, functions, files, dictionaries, exceptions, separation of responsibilities, business rules, data persistence

## Extra Challenge

Create a transaction history containing: transaction type, amount, source account, destination account, date and time.

---

# 16. Help Desk System

## Objective

Create a complete support ticket management system.

This is the most complete project in this guide and can become an early portfolio project.

## Suggested Data Structure

```python
ticket = {
    "id": 1,
    "title": "Unable to access the system",
    "description": "The user receives an authentication error.",
    "priority": "high",
    "status": "open",
    "requester": "Maria",
    "comments": []
}
```

## Minimum Features

- Open a support ticket.
- List all tickets.
- Search by ticket ID.
- Update ticket status.
- Update ticket priority.
- Add comments.
- Filter by status.
- Filter by priority.
- Close a ticket.
- Save tickets in JSON.
- Load tickets when the program starts.
- Validate all required fields.
- Handle missing or corrupted files.

## Suggested Status Values

`open`, `in_progress`, `resolved`, `closed`

## Suggested Priority Values

`low`, `medium`, `high`, `critical`

## Reports

Generate a report containing:

- Total number of tickets
- Open tickets
- Tickets in progress
- Resolved tickets
- Closed tickets
- Tickets by priority
- Tickets by requester

## Suggested Structure

```text
helpdesk/
├── main.py
├── services/
│   └── ticket_service.py
├── repositories/
│   └── ticket_repository.py
├── utils/
│   └── validators.py
├── data/
│   └── tickets.json
└── README.md
```

## Concepts Practiced

- Lists, dictionaries, functions, modules, file handling, JSON, CRUD, input validation, exception handling, separation of responsibilities, basic software architecture

## Extra Challenge

Add: creation date, update date, assigned support agent, ticket history, export to CSV, dashboard summary in the terminal.

---

# Recommended Learning Path

| Stage | Projects | Main Focus |
|---|---|---|
| Beginner | 1 to 4 | Collections, loops, functions, basic validation |
| Beginner-Intermediate | 5 to 9 | Dictionaries, modules, basic files, menus |
| Intermediate | 10 to 13 | Business rules, custom exceptions, files, parsing |
| Strong Intermediate | 14 | Persistence, JSON, robust exception handling |
| Advanced for Current Level | 15 and 16 | Modularization and software architecture |

---

# Suggested Execution Strategy

For each project, follow this sequence:

## Step 1 — Write the Requirements

Before coding, write down:

- What the program must do
- What data must be stored
- What menu options are needed
- Which invalid situations must be handled

## Step 2 — Model the Data

Define how one entity will be represented (one student, one contact, one product, one transaction, one task, one ticket).

## Step 3 — Implement One Feature at a Time

Recommended order: create → list → search → update → delete → validate → save → load → refactor.

## Step 4 — Test Manually

Test at least: valid input, invalid input, empty input, non-existing ID, duplicate data, negative values, missing file, corrupted file.

## Step 5 — Refactor

After the project works: rename unclear variables, extract repeated code into functions, remove duplicated logic, separate modules, improve error messages, add documentation.

---

# Portfolio Recommendation

The strongest projects for an initial portfolio are:

1. Persistent Task Manager
2. Personal Finance Manager
3. Modular Banking System
4. Help Desk System

For portfolio projects, include: English `README.md`, project objective, features, installation instructions, usage examples, folder structure, screenshots or terminal recordings, known limitations, future improvements.

---

# Final Goal

After completing these projects, you should be more comfortable with:

- Breaking problems into smaller functions
- Representing real-world data
- Writing CRUD operations
- Validating input
- Handling failures
- Raising and handling custom exceptions
- Saving and loading data
- Organizing a program into modules
- Preparing for object-oriented programming
- Preparing for `pytest`
- Preparing for APIs with FastAPI
