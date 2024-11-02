"""
Banking program
show balance
deposition
withdrawal
exit
"""

balance = 0


def show_balance():
    print(f"your current balance is  {balance} ")


def deposit():
    global balance
    amount = float(input("Enter an amount to deposit: "))
    if amount < 0:
        print("Amount is not valid")

    else:
        balance += amount
        print(f"Successfully deposited {amount}")
        show_balance()


def withdraw():
    global balance
    amount = float(input("Enter an amount to withdraw: "))

    if amount > balance:
        print("insufficient funds")

    if amount < 0:
        print("amount must be a positive number")

    else:
        balance -= amount
        print(f"Withdrew {amount}")
        show_balance()


# Main program loop
while True:
    print("\n===== Banking Program =====")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
