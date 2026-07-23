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
