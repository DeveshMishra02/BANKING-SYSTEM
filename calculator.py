def interest_calculator():
    print("\n===== INTEREST CALCULATOR =====")

    try:
        principal = float(input("Principal amount: ₹"))
        rate = float(input("Annual interest rate (%): "))
        years = float(input("Number of years: "))

        interest = principal * rate * years / 100
        final_amount = principal + interest

        print("\nInterest earned: ₹", interest)
        print("Final amount: ₹", final_amount)
    except ValueError:
        print("Please enter valid numbers.")
