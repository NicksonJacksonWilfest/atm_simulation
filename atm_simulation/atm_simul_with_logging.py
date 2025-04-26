import hashlib
import time
import random
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('atm.log'),  # Log to file
        # logging.StreamHandler()          # Log to console
    ]
)
logger = logging.getLogger(__name__)

class ATM:
    def __init__(self):
        self.balance = 1000.00  # Initial balance
        self.pin_hash = self.hash_pin("1234")  # Default PIN (hashed)
        self.biometric_template = self.hash_biometric("fingerprint123")  # Simulated biometric
        self.attempts = 3       # Max PIN/OTP/Biometric attempts
        self.transaction_history = []  # List to store transaction history
        self.is_locked = False  # Account lock status
        self.last_activity = time.time()  # Track last activity for session timeout
        self.session_timeout = 60  # 60 seconds timeout
        self.daily_limits = {
            "withdrawal": {"limit": 1000.00, "used": 0.00, "date": datetime.now().date()},
            "deposit": {"limit": 5000.00, "used": 0.00, "date": datetime.now().date()}
        }
        self.otp = None  # Current OTP
        self.otp_expiry = None  # OTP expiry timestamp
        self.otp_attempts = 3  # Max OTP attempts
        self.biometric_attempts = 3  # Max biometric attempts
        logger.info("ATM initialized with balance $%.2f", self.balance)

    def hash_pin(self, pin):
        """Hash the PIN using SHA-256."""
        logger.debug("Hashing PIN")
        return hashlib.sha256(pin.encode()).hexdigest()

    def hash_biometric(self, biometric_data):
        """Hash the biometric template using SHA-256 (simulated)."""
        logger.debug("Hashing biometric template")
        return hashlib.sha256(biometric_data.encode()).hexdigest()

    def generate_otp(self):
        """Generate a 6-digit OTP and set expiry (30 seconds)."""
        self.otp = str(random.randint(100000, 999999))
        self.otp_expiry = time.time() + 30  # OTP valid for 30 seconds
        logger.info("Generated OTP (valid for 30 seconds)")
        print(f"Simulated SMS: Your OTP is {self.otp} (valid for 30 seconds)")
        return self.otp

    def verify_otp(self):
        """Verify the OTP entered by the user."""
        if self.otp is None or time.time() > self.otp_expiry:
            logger.warning("OTP expired or invalid")
            print("OTP has expired or is invalid. Please try again.")
            return False

        while self.otp_attempts > 0:
            entered_otp = input("Enter the OTP: ")
            if entered_otp == self.otp:
                logger.info("OTP verification successful")
                self.otp_attempts = 3  # Reset attempts on success
                self.otp = None  # Clear OTP after use
                self.otp_expiry = None
                return True
            else:
                self.otp_attempts -= 1
                logger.warning("Invalid OTP. Attempts remaining: %d", self.otp_attempts)
                print(f"Invalid OTP. {self.otp_attempts} attempts remaining.")

        self.is_locked = True
        logger.critical("Account locked due to too many incorrect OTP attempts")
        print("Too many incorrect OTP attempts. Account locked. Contact the bank.")
        return False

    def verify_biometric(self):
        """Simulate fingerprint scan with 90% success rate."""
        if self.biometric_attempts == 0:
            self.is_locked = True
            logger.critical("Account locked due to too many failed biometric attempts")
            print("Too many failed biometric attempts. Account locked. Contact the bank.")
            return False

        while self.biometric_attempts > 0:
            input("Press Enter to scan fingerprint (simulated)...")
            # Simulate biometric scan with 90% success probability
            if random.random() < 0.9:  # 90% chance of success
                logger.info("Fingerprint scan successful")
                self.biometric_attempts = 3  # Reset attempts on success
                return True
            else:
                self.biometric_attempts -= 1
                logger.warning("Fingerprint scan failed. Attempts remaining: %d", self.biometric_attempts)
                print(f"Fingerprint scan failed. {self.biometric_attempts} attempts remaining.")

        self.is_locked = True
        logger.critical("Account locked due to too many failed biometric attempts")
        print("Too many failed biometric attempts. Account locked. Contact the bank.")
        return False

    def verify_pin(self):
        """Verify PIN, OTP, and Biometric for MFA."""
        if self.is_locked:
            logger.warning("Login attempt on locked account")
            print("Account is locked. Please contact the bank to reset.")
            return False

        while self.attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if self.hash_pin(entered_pin) == self.pin_hash:
                logger.info("PIN verification successful")
                self.attempts = 3  # Reset PIN attempts
                self.generate_otp()  # Generate OTP after PIN success
                if self.verify_otp():  # Proceed to OTP verification
                    if self.verify_biometric():  # Proceed to biometric verification
                        logger.info("MFA authentication successful")
                        self.last_activity = time.time()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                self.attempts -= 1
                logger.warning("Invalid PIN. Attempts remaining: %d", self.attempts)
                print(f"Invalid PIN. {self.attempts} attempts remaining.")

        self.is_locked = True
        logger.critical("Account locked due to too many incorrect PIN attempts")
        print("Too many incorrect PIN attempts. Account locked. Contact the bank.")
        return False

    def check_timeout(self):
        """Check if session has timed out."""
        if time.time() - self.last_activity > self.session_timeout:
            logger.warning("Session timed out due to inactivity")
            print("Session timed out due to inactivity.")
            return True
        return False

    def reset_limits(self):
        """Reset daily limits if a new day has started."""
        current_date = datetime.now().date()
        if self.daily_limits["withdrawal"]["date"] != current_date:
            logger.info("Resetting daily transaction limits for new day")
            self.daily_limits["withdrawal"] = {"limit": 1000.00, "used": 0.00, "date": current_date}
            self.daily_limits["deposit"] = {"limit": 5000.00, "used": 0.00, "date": current_date}

    def add_transaction(self, transaction_type, amount=None):
        """Add a transaction to history with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if transaction_type == "Balance Check":
            transaction = f"{timestamp} - {transaction_type} - Balance: ${self.balance:.2f}"
            logger.info("Balance checked: $%.2f", self.balance)
        elif transaction_type == "PIN Change":
            transaction = f"{timestamp} - {transaction_type}"
            logger.info("PIN changed")
        else:
            transaction = f"{timestamp} - {transaction_type} - Amount: ${amount:.2f} - Balance: ${self.balance:.2f}"
            logger.info("%s of $%.2f completed. New balance: $%.2f", transaction_type, amount, self.balance)
        self.transaction_history.append(transaction)

    def check_balance(self):
        if self.check_timeout():
            return False
        print(f"Your current balance is: ${self.balance:.2f}")
        self.add_transaction("Balance Check")
        self.last_activity = time.time()
        return True

    def deposit(self):
        if self.check_timeout():
            return False
        self.reset_limits()
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                if self.daily_limits["deposit"]["used"] + amount <= self.daily_limits["deposit"]["limit"]:
                    self.balance += amount
                    self.daily_limits["deposit"]["used"] += amount
                    print(f"Deposited ${amount:.2f} successfully.")
                    self.add_transaction("Deposit", amount)
                    self.check_balance()
                else:
                    logger.warning("Deposit attempt exceeds daily limit of $%.2f", self.daily_limits["deposit"]["limit"])
                    print(f"Deposit exceeds daily limit of ${self.daily_limits['deposit']['limit']:.2f}.")
            else:
                logger.error("Invalid deposit amount: $%.2f", amount)
                print("Invalid amount. Please enter a positive value.")
        except ValueError:
            logger.error("Invalid input for deposit amount")
            print("Invalid input. Please enter a valid number.")
        self.last_activity = time.time()
        return True

    def withdraw(self):
        if self.check_timeout():
            return False
        self.reset_limits()
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount > 0:
                if self.daily_limits["withdrawal"]["used"] + amount <= self.daily_limits["withdrawal"]["limit"]:
                    if amount <= self.balance:
                        self.balance -= amount
                        self.daily_limits["withdrawal"]["used"] += amount
                        print(f"Withdrawn ${amount:.2f} successfully.")
                        self.add_transaction("Withdrawal", amount)
                        self.check_balance()
                    else:
                        logger.warning("Withdrawal attempt failed: Insufficient funds")
                        print("Insufficient funds.")
                else:
                    logger.warning("Withdrawal attempt exceeds daily limit of $%.2f", self.daily_limits["withdrawal"]["limit"])
                    print(f"Withdrawal exceeds daily limit of ${self.daily_limits['withdrawal']['limit']:.2f}.")
            else:
                logger.error("Invalid withdrawal amount: $%.2f", amount)
                print("Invalid amount. Please enter a positive value.")
        except ValueError:
            logger.error("Invalid input for withdrawal amount")
            print("Invalid input. Please enter a valid number.")
        self.last_activity = time.time()
        return True

    def change_pin(self):
        if self.check_timeout():
            return False
        print("MFA required to change PIN.")
        if not self.verify_pin():  # Require full MFA for PIN change
            return False
        new_pin = input("Enter new PIN (4 digits): ")
        if new_pin.isdigit() and len(new_pin) == 4:
            self.pin_hash = self.hash_pin(new_pin)
            print("PIN changed successfully.")
            self.add_transaction("PIN Change")
        else:
            logger.error("Invalid new PIN: Must be 4 digits")
            print("New PIN must be 4 digits.")
        self.last_activity = time.time()
        return True

    def view_transaction_history(self):
        if self.check_timeout():
            return False
        print("MFA required to view transaction history.")
        if not self.verify_pin():  # Require full MFA for transaction history
            return False
        if not self.transaction_history:
            logger.info("No transactions found in history")
            print("No transactions found.")
        else:
            logger.info("Transaction history viewed")
            print("\n=== Transaction History ===")
            for transaction in self.transaction_history:
                print(transaction)
        self.last_activity = time.time()
        return True

    def unlock_account(self):
        """Simulate bank admin unlocking the account."""
        admin_code = input("Enter admin unlock code: ")
        if admin_code == "ADMIN123":  # Simulated admin code
            self.is_locked = False
            self.attempts = 3
            self.otp_attempts = 3
            self.biometric_attempts = 3
            logger.info("Account unlocked by admin")
            print("Account unlocked successfully.")
        else:
            logger.warning("Invalid admin unlock code")
            print("Invalid admin code.")

    def menu(self):
        if not self.verify_pin():
            return
        while True:
            print("\n=== ATM Menu ===")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")
            choice = input("Select an option (1-6): ")

            if choice == "1":
                if not self.check_balance():
                    break
            elif choice == "2":
                if not self.deposit():
                    break
            elif choice == "3":
                if not self.withdraw():
                    break
            elif choice == "4":
                if not self.change_pin():
                    break
            elif choice == "5":
                if not self.view_transaction_history():
                    break
            elif choice == "6":
                logger.info("User exited ATM")
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                logger.warning("Invalid menu option selected: %s", choice)
                print("Invalid option. Please try again.")
                self.last_activity = time.time()

# Run the ATM simulation
if __name__ == "__main__":
    atm = ATM()
    print("Welcome to the ATM")
    atm.menu()

# The code now includes logging for various actions, including successful and failed attempts, and account lock status.
# The logging configuration is set to log to a file named 'atm.log'.