from datetime import datetime


class BankAccount:

    def __init__(self, holder_name, account_number, balance=0.0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.__balance = float(balance)
        self._history = []

        if balance > 0:
            self._log(f"Account opened with initial balance ${balance:,.2f}")


    def _log(self, message):
        """Record a transaction with a timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._history.append(f"[{timestamp}] {message}")

    def _get_balance(self):
        """Protected getter so subclasses can read the balance safely."""
        return self.__balance

    def _set_balance(self, new_balance):
        """Protected setter so subclasses can adjust the balance safely."""
        self.__balance = new_balance


    def deposit(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            print(" Deposit failed: amount must be a number.")
            return False

        if amount <= 0:
            print(" Deposit failed: amount must be greater than zero.")
            return False

        self.__balance += amount
        self._log(f"Deposited ${amount:,.2f}")
        print(f" Deposited ${amount:,.2f}. New balance: ${self.__balance:,.2f}")
        return True

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            print(" Withdrawal failed: amount must be a number.")
            return False

        if amount <= 0:
            print(" Withdrawal failed: amount must be greater than zero.")
            return False

        if amount > self.__balance:
            print(" Withdrawal failed: insufficient funds.")
            return False

        self.__balance -= amount
        self._log(f"Withdrew ${amount:,.2f}")
        print(f" Withdrew ${amount:,.2f}. New balance: ${self.__balance:,.2f}")
        return True

    def show_balance(self):
        print(f" {self.holder_name} (Acct #{self.account_number}) "
              f"balance: ${self.__balance:,.2f}")

    def show_history(self):
        print(f"\n--- Transaction history for {self.holder_name} "
              f"(Acct #{self.account_number}) ---")
        if not self._history:
            print(" (no transactions yet)")
        else:
            for entry in self._history:
                print(" " + entry)
        print("-" * 50)

    def __str__(self):
        return (f"{self.__class__.__name__}({self.holder_name}, "
                f"#{self.account_number}, balance=${self.__balance:,.2f})")