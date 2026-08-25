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
        pass

    return users


def login_user():
    users = load_users()

    username = input("Enter you username: ".strip())
    password = input("Enter your password: ").strip()

    if username in users and users[username] == password:
        print(f"Welcome, {username}")
    else:
        print("ERROR: Invalid username or password")


def list_users():
    pass


 # Main Program
choice = input("1. Login\n2. Register\n>").strip()

if choice == "1":
    login_user()
elif choice == "2":
    register_user()
else:
    print("Invalid Option")
