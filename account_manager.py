import random
from account import account

def create_account():
    print("\n===== CREATE ACCOUNT =====")
    account["name"] = input("Enter your name: ")

    while True:
        password = input("Create password (4+ characters): ")
        if len(password) >= 4:
            break
        print("Password must contain at least 4 characters.")

    account["password"] = password
    account["account_number"] = "SB" + str(random.randint(100000, 999999))
    account["balance"] = 0
    account["reward_points"] = 0
    account["transactions"] = []

    print("\nAccount created successfully!")
    print("Name:", account["name"])
    print("Account Number:", account["account_number"])

def login():
    print("\n===== LOGIN =====")
    attempts = 3

    while attempts > 0:
        number = input("Account number: ")
        password = input("Password: ")

        if number == account["account_number"] and password == account["password"]:
            print("Login successful!")
            print("Welcome,", account["name"])
            return True

        attempts -= 1
        print("Incorrect account number or password.")
        if attempts:
            print("Attempts remaining:", attempts)

    print("Login blocked temporarily.")
    return False
