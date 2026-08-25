import json


USERS_FILE = "users.json"


def load_users():
    
    try:
        with open(USERS_FILE, "r") as file:
            users = json.load(file) # converts JSON into a python obj
        
    except FileNotFoundError:
        users = {}

        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)
    
    except json.JSONDecodeError:
        print("ERROR: The users file contains invalid JSON.")
        users = {}
    
    return users


def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def register_user():
    username = input("New username: ").strip()
    password = input(f"Password for new user '{username}': ").strip()

    if not username or not password:
        print("Username and/or password cannot be empty.")
        return
    
    users = load_users()

    if username in users:
        print("This username is already taken.")
        return
    
    users[username] = password
    save_users(users)

    print(f"SUCCESS: New user {username} created")


def login_user():
    users = load_users()

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username] == password:
        print("Login successful.")
        return True
    else:
        print("Incorrect user or password.")
        return False


def list_users():
    users = load_users()

    if not users:
        print("No users registered.")
        return

    print("\n-----Registered users-----")
    for username in users:
        print(username)
    print("--------------------------\n" )


while True:
    choice = input(
        "1. Login\n"
        "2. Register\n"
        "3. List users\n"
        "4. Exit\n"
        "> "
    ).strip()
    
    if choice == "1":
        login_user()
    elif choice == "2":
        register_user()
    elif choice == "3":
        list_users()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option")