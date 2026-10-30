balance = 10000

def check_balance():
    print("Your balance is:", balance)

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance = balance + amount
        print("Deposit successful")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: "))
    if amount > 0 and amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
    else:
        print("Invalid amount or insufficient balance")

def atm():
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your option: ")

        if option == "1":
            check_balance()
        elif option == "2":
            deposit()
        elif option == "3":
            withdraw()
        elif option == "4":
            print("Thank you")
            break
        else:
            print("Invalid option")

atm()
