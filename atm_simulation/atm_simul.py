# Step 1: Set initial balance
balance_amount = 100000.00  # Initial balance in Tshs

# Step 2: Create a loop for the ATM menu
# Step 3: Display menu options
# Step 4: Get user input for menu choice
# Step 5: Implement functionality for each menu option
# Step 6: Handle invalid input
# ATM Simulation

while True:
    # Menu display
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: {balance_amount} Tshs.")

    elif choice == '2':
        # We'll add deposit logic here next
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount > 0:
            balance_amount += deposit_amount
            print(f"Successfully deposited {deposit_amount} Tshs.")
            print(f"New balance is: {balance_amount} Tshs")
        else:
            print("Deposit amount must be positive.")

    elif choice == '3':
        # We'll add withdrawal logic here next
        withdrawal_amount = float(input("Enter amount to withdraw: "))
        if withdrawal_amount > 0:
            if withdrawal_amount <= balance_amount:
                balance_amount -= withdrawal_amount
                print(f"Successfully withdrew {withdrawal_amount} Tshs.")
                print(f"New balance is: {balance_amount} Tshs")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
