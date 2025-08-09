'''
Login System
Ask for username.

If username exists:

Ask for password.

If password correct, log in.

Else, "Wrong password."

Else, "User not found.

Alright — let’s turn your simple login check into a mini authentication system with:

Login

Registration (if user doesn’t exist)

Loop until the user chooses to quit"
'''

user_db ={
    "godwin":{"password": 1234}
}

action = input("enter 'login' to logging or 'register' to create a username: ").lower()
if action == "login":
    username = input("enter your username: ")
    if username in user_db:
        password = input("enter your password: ")
        if int(password) == user_db["godwin"]["password"]:
            print("logging successfully")
        else:
            print("wrong password")
    else:
        print("user not found")

else:
    if  action == "register":
        username = input("create a username: ")
        if username in user_db:
            print("username exist")
        else:
            password = int(input("enter a valid password: "))
            #user_db[username] = {"password": password}
            user_db.update({username: {"password": password}})
            print(f"successfully registered, your username is {username} and your password is {password}")
print(user_db)
