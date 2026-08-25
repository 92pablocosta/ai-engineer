print("=" * 20)
print("LOGIN SYSTEM")
print("=" * 20)


def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")


def register_user():
    username = input("Enter a username: ").strip()
    users = load_users()

    if username in users:
        print(f"ERROR: Username '{username}' already exists.")
        return
    
    password = input("Enter a password: ").strip()

    if not username or not password:
        print("ERROR: Username and/or Password cannot be empty.")
        return
    
    save_user(username, password)

    print(f"User '{username}' registered successfully.")


def load_users():
    users = {}

    try:
        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                username, password = line.split(":", 1)
                users[username] = password
    except FileNotFoundError:
        with open("users.txt", "w"):
            pass

    return users


def login_user():
    users = load_users()

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username in users and users[username] == password:
        print(f"Welcome, {username}")
        return True 
    else:
        print("ERROR: Invalid username or password")
        return False


def list_users():
    users = load_users()

    if not users:
        print("No users registered.")
        return

    print("Registered users:")

    for username in users:
        print(f"- {username}")


# Main Program

LOGIN_MAX_TRIES = 3
login_tries = 0 
while True:
    choice = input(
        "1. Login\n"
        "2. Register\n"
        "3. List users\n"
        "4. Exit\n"
        "> "
    ).strip()

    if choice == "1":
        if login_tries >= LOGIN_MAX_TRIES:
            print("Max login attempts reached.")
        else:
            login_success = login_user()

            if not login_success:

                login_tries += 1
                print(f"Login tries: {login_tries}")
    elif choice == "2":
        register_user()
    elif choice == "3":
        list_users()
    elif choice == "4":
        print("See you later mate!")
        break
    else:
        print("Invalid Option")
