from datetime import datetime
from account import account

def add_transaction(transaction_type, amount):
    account["transactions"].append({
        "type": transaction_type,
        "amount": amount,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })

def print_receipt(transaction_type, amount):
    print("\n===== MINI RECEIPT =====")
    print("Bank:", "Smart Bank")
    print("Name:", account["name"])
    print("Account:", account["account_number"])
    print("Transaction:", transaction_type)
    print("Amount: ₹", amount)
    print("Date:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("Balance: ₹", account["balance"])
