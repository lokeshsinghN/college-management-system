def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False


def register(username, password):
    print(f"User {username} registered successfully.")