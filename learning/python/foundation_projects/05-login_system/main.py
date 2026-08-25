print("=" * 20)
print("LOGIN SYSTEM")
print("=" * 20)

choice = input("1. Login\n2. Register\n>").strip()

def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")

def register_user():
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    if not username or not password:
        print("ERROR: Username and/or Password cannot be empty.")
        return
    
    save_user(username, password)

    print(f"User '{username}' is ready to be registered.")


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



if choice == "1":
    print("Login selected")
elif choice == "2":
    register_user()
else:
    print("Invalid Option")
