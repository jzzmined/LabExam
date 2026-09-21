from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, holder_name, account_number, balance=0.0,
                 interest_rate=0.0, minimum_balance=0.0):
        super().__init__(holder_name, account_number, balance)
        self.interest_rate = float(interest_rate)   # e.g. 0.02 = 2%
        self.minimum_balance = float(minimum_balance)

    def add_interest(self):
        current = self._get_balance()
        interest = current * self.interest_rate

        if interest <= 0:
            print(" No interest added (rate or balance is zero).")
            return False

        self._set_balance(current + interest)
        self._log(f"Added interest ${interest:,.2f} "
                   f"({self.interest_rate * 100:.2f}% rate)")
        print(f" Interest of ${interest:,.2f} added. "
              f"New balance: ${self._get_balance():,.2f}")
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

        current = self._get_balance()
        if current - amount < self.minimum_balance:
            print(f" Withdrawal failed: balance cannot drop below the "
                  f"required minimum of ${self.minimum_balance:,.2f}.")
            return False

        self._set_balance(current - amount)
        self._log(f"Withdrew ${amount:,.2f} (savings)")
        print(f" Withdrew ${amount:,.2f}. New balance: ${self._get_balance():,.2f}")
        return True