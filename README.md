# ATM Simulation

This project is a Python-based simulation of an Automated Teller Machine (ATM). It provides various features such as balance checking, deposits, withdrawals, multi-currency support, daily transaction limits, and multi-factor authentication (MFA) with logging.

## Features

1. **Basic ATM Operations**:
   - Check account balance.
   - Deposit funds.
   - Withdraw funds.

2. **Multi-Currency Support**:
   - Tanzanian Shillings (Tshs).
   - US Dollars (USD).
   - Euros (EUR).

3. **Daily Transaction Limits**:
   - Configurable daily withdrawal and deposit limits.

4. **Multi-Factor Authentication (MFA)**:
   - PIN verification.
   - One-Time Password (OTP).
   - Biometric simulation.

5. **Logging**:
   - Logs all transactions and activities to a file (`atm.log`).

6. **Transaction History**:
   - View detailed transaction history.

7. **Session Timeout**:
   - Automatically logs out users after a period of inactivity.

8. **Account Locking**:
   - Locks the account after multiple failed authentication attempts.

## Project Structure

## Requirements

- Python 3.12 or higher
- No additional dependencies (standard Python library)

## How to Run

1. Clone the repository:

   ```sh
   git clone https://github.com/NicksonJacksonWilfest/atm_simulation.git
   ```

2. Navigate to atm-simulation:

    ```sh
    cd atm_simulation
    ```

3. Run the desired version of ATM simulation

   ```sh
   python atm_simulation/atm_*.py
   ```

## License

None

## Author

Developed with Love by Distrodev
