username = "pablo"
password = "123"

with open("test.txt", "a") as file:
    file.write(f"{username}:{password}")
