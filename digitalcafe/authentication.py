import database as db

def login(username, password):
    user = db.get_user(username)
    
    if not user:
        return False, "Invalid username. Please try again."
    
    if user["password"] != password:
        return False, "Invalid password. Please try again."
    
    if not username or not password:
        return False, "Incomplete login data. Please try again."
    
    return True, {"username": username, "first_name": user["first_name"], "last_name": user["last_name"]}