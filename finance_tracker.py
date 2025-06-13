transactions = []
balance = 0.0

def add_income():
    global balance
    amount = float(input("Enter income amount: $"))
    balance += amount
    transactions.append(("Income", amount))
    print(f"Income added: ${amount:.2f}")

def add_expense():
    global balance
    amount = float(input("Enter expense amount: $"))
    if balance >= amount:
        balance -= amount
        transactions.append(("Expense", amount))
        print(f"Expense added: ${amount:.2f}")
    else:
        print("Error: Not enough money!")

def show_balance():
    print(f"\nCurrent Balance: ${balance:.2f}")

def show_history():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t_type, amount in transactions:
            print(f"{t_type}: ${amount:.2f}")


while True:
    print("\n--- Finance Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Check Balance")
    print("4. View History")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        show_history()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")