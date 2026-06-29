
print("Balance: 1000")

balance = 1000
while True:

    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exist")
    user = input("Enter your choice: ")
    if user not in["1", "2", "3", "4"]:
        print("Invalid choice")
        continue

    if user == "4":
        print("GOODBYE!")
        break
    elif user == "1":
        print(f"Your balance is: {balance}")
    elif user == "2":
        deposit = int(input("Enter deposit amount: "))
        while deposit <= 0:
            print("Invalid deposit amount")
            deposit = int(input("Enter deposit amount: "))
        else:
            balance = balance + deposit


    elif user == "3":
        withdraw = int(input("Enter withdraw amount: "))
        while withdraw <= 0:
            print("Invalid withdraw amount")
            withdraw = int(input("Enter withdraw amount: "))
            continue
        while withdraw > balance:
            print("Insuficient balance!")
            withdraw = int(input("Enter withdraw amount: "))
            continue

        else:
            balance = balance - withdraw
        print(f"You have withdrew {withdraw} ETB")
