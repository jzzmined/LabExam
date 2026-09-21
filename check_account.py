from bank_account import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, holder_name, account_number, balance=0.0,
                 withdrawal_fee=0.0):
        super().__init__(holder_name, account_number, balance)
        self.withdrawal_fee = float(withdrawal_fee)

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            print(" Withdrawal failed: amount must be a number.")
            return False

        if amount <= 0:
            print(" Withdrawal failed: amount must be greater than zero.")
            return False

        total_deduction = amount + self.withdrawal_fee
        current = self._get_balance()

        if total_deduction > current:
            print(f" Withdrawal failed: ${amount:,.2f} plus a "
                  f"${self.withdrawal_fee:,.2f} fee exceeds your balance.")
            return False

        self._set_balance(current - total_deduction)
        self._log(f"Withdrew ${amount:,.2f} + ${self.withdrawal_fee:,.2f} fee")
        print(f" Withdrew ${amount:,.2f} (+ ${self.withdrawal_fee:,.2f} fee). "
              f"New balance: ${self._get_balance():,.2f}")
        return True