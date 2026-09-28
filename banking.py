from account import account
from transactions import add_transaction, print_receipt
from rewards import show_rewards
from calculator import interest_calculator

def check_balance():
    print("\n===== BALANCE =====")
    print("Name:", account["name"])
    print("Account:", account["account_number"])
    print("Balance: ₹", account["balance"])

    if account["balance"] < 500:
        print("WARNING: Balance is below ₹500!")

def deposit():
    print("\n===== DEPOSIT =====")
    try:
        amount = float(input("Enter amount: ₹"))
        if amount <= 0:
            print("Invalid amount.")
            return

        account["balance"] += amount
        points = int(amount // 100)
        account["reward_points"] += points
        add_transaction("DEPOSIT", amount)

        print("Deposit successful!")
        print("New balance: ₹", account["balance"])
        print("Reward points earned:", points)
        print_receipt("DEPOSIT", amount)
    except ValueError:
        print("Please enter a number.")

def withdraw():
    print("\n===== WITHDRAW =====")
    try:
        amount = float(input("Enter amount: ₹"))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > account["balance"]:
            print("Insufficient balance!")
        else:
            account["balance"] -= amount
            add_transaction("WITHDRAW", amount)
            print("Withdrawal successful!")
            print("Remaining balance: ₹", account["balance"])
            print_receipt("WITHDRAW", amount)
    except ValueError:
        print("Please enter a number.")

def transfer_money():
    print("\n===== TRANSFER =====")
    receiver = input("Receiver account number: ")

    if receiver == account["account_number"]:
        print("You cannot transfer to yourself.")
        return

    try:
        amount = float(input("Enter amount: ₹"))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > account["balance"]:
            print("Insufficient balance!")
        else:
            account["balance"] -= amount
            add_transaction("TRANSFER TO " + receiver, amount)
            print("Transfer successful!")
            print("Amount: ₹", amount)
            print("Remaining balance: ₹", account["balance"])
            print_receipt("TRANSFER", amount)
    except ValueError:
        print("Please enter a number.")

def transaction_history():
    print("\n===== TRANSACTION HISTORY =====")

    if not account["transactions"]:
        print("No transactions yet.")
        return

    for number, transaction in enumerate(account["transactions"], 1):
        print("\nTransaction", number)
        print("Type:", transaction["type"])
        print("Amount: ₹", transaction["amount"])
        print("Time:", transaction["time"])

def account_details():
    print("\n===== ACCOUNT DETAILS =====")
    print("Name:", account["name"])
    print("Account Number:", account["account_number"])
    print("Balance: ₹", account["balance"])
    print("Reward Points:", account["reward_points"])

def banking_menu():
    while True:
        print("\n===== SMART BANKING SYSTEM =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Reward Points")
        print("7. Interest Calculator")
        print("8. Account Details")
        print("9. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer_money()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            show_rewards()
        elif choice == "7":
            interest_calculator()
        elif choice == "8":
            account_details()
        elif choice == "9":
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice!")
