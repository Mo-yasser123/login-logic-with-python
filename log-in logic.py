register_UName = input ("Enter your username: ")
register_PWord = input("Enter your password: ")

login_UName = input ("Enter your username: ")
login_PWord = input ("Enter your password: ")

while login_UName != register_UName or login_PWord != register_PWord:
    print("Invalid username or password. Please try again.")
    login_UName = input ("Enter your username: ")
    login_PWord = input ("Enter your password: ")

if login_UName == register_UName and login_PWord == register_PWord:
    print("Login successful!")
