from account import account
from account_manager import create_account, login
from banking import banking_menu

while True:
    print("\n===== SMART BANK =====")
    print("1. Create New Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        if account["account_number"] == "":
            print("Please create an account first.")
        elif login():
            banking_menu()
    elif choice == "3":
        print("Thank you for using Smart Bank!")
        break
    else:
        print("Invalid choice!")
