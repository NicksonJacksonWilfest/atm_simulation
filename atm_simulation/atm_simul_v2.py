# ATM Simulation with Currency Conversion

# Step 1: Set initial balance
balance_amount = 100000.00  # Initial balance in Tshs

# Step 2: Define exchange rates for supported currencies
exchange_rates = {
    "Tshs": 1,       # Base currency
    "USD": 0.0004,   # Example rate: 1 Tshs = 0.0004 USD
    "EUR": 0.00035   # Example rate: 1 Tshs = 0.00035 EUR
}

# Step 3: Set default currency
current_currency = "Tshs"

# Step 4: Create a loop for the ATM menu
while True:
    # Currency selection menu
    print("\n====== CURRENCY MENU ======")
    print("1. Tanzanian Shillings (Tshs)")
    print("2. US Dollars (USD)")
    print("3. Euros (EUR)")
    print("4. Continue to ATM Menu")

    currency_choice = input("Select your currency (1-4): ")

    if currency_choice == '1':
        current_currency = "Tshs"
    elif currency_choice == '2':
        current_currency = "USD"
    elif currency_choice == '3':
        current_currency = "EUR"
    elif currency_choice == '4':
        pass  # Proceed to ATM menu
    else:
        print("Invalid choice. Please select from 1 to 4.")
        continue

    # Step 5: Display ATM menu
    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit to Currency Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Convert balance to selected currency
            converted_balance = balance_amount * exchange_rates[current_currency]
            print(f"Your current balance is: {converted_balance:.2f} {current_currency}")

        elif choice == '2':
            deposit_amount = float(input(f"Enter amount to deposit in {current_currency}: "))
            if deposit_amount > 0:
                # Convert deposit amount to base currency (Tshs)
                balance_amount += deposit_amount / exchange_rates[current_currency]
                print(f"Successfully deposited {deposit_amount:.2f} {current_currency}.")
                converted_balance = balance_amount * exchange_rates[current_currency]
                print(f"New balance is: {converted_balance:.2f} {current_currency}")
            else:
                print("Deposit amount must be positive.")

        elif choice == '3':
            withdrawal_amount = float(input(f"Enter amount to withdraw in {current_currency}: "))
            if withdrawal_amount > 0:
                # Convert withdrawal amount to base currency (Tshs)
                withdrawal_in_tshs = withdrawal_amount / exchange_rates[current_currency]
                if withdrawal_in_tshs <= balance_amount:
                    balance_amount -= withdrawal_in_tshs
                    print(f"Successfully withdrew {withdrawal_amount:.2f} {current_currency}.")
                    converted_balance = balance_amount * exchange_rates[current_currency]
                    print(f"New balance is: {converted_balance:.2f} {current_currency}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")

        elif choice == '4':
            print("Returning to Currency Menu...")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")