# bank_account.py

class BankAccount:
    def __init__(self, account_balance=0.00):
        # Initialize account balance, ensuring it's not negative
        if account_balance >= 0.00:
            self.__account_balance = account_balance
        else:
            print("Account Balance cannot be negative!")
            self.__account_balance = 0.00

    def deposit(self, amount):
        """Add money to the account balance."""
        if amount > 0.00:
            self.__account_balance += amount
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist."""
        if amount > 0.00:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Amount must be positive")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

