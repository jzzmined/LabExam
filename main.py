from bank_account import BankAccount
from savings_account import SavingsAccount
from check_account import CheckingAccount


MENU = """
============ BANK ACCOUNT SYSTEM ============
1. Create account
2. Deposit
3. Withdraw
4. Check balance
5. Add interest (savings only)
6. View transaction history
7. Exit
===============================================
"""

# All accounts, keyed by account number (string) -> account object
accounts = {}
next_account_number = 1001


def get_float(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.lower() in ("c", "cancel", ""):
            return None
        try:
            return float(raw)
        except ValueError:
            print(" Please enter a valid number (or 'c' to cancel).")


def choose_account():
    if not accounts:
        print(" There are no accounts yet. Create one first.")
        return None

    acct_num = input("Enter account number: ").strip()
    account = accounts.get(acct_num)
    if account is None:
        print(f" No account found with number '{acct_num}'.")
        return None
    return account


def create_account():
    global next_account_number

    print("\nAccount types: [1] Basic  [2] Savings  [3] Checking")
    acct_type = input("Choose account type (1-3): ").strip()

    if acct_type not in ("1", "2", "3"):
        print(" Invalid account type. Account not created.")
        return

    name = input("Account holder name: ").strip()
    if not name:
        print(" Name cannot be empty. Account not created.")
        return

    initial = get_float("Initial deposit (or press Enter for $0): ")
    if initial is None:
        initial = 0.0
    if initial < 0:
        print(" Initial deposit cannot be negative. Using $0 instead.")
        initial = 0.0

    account_number = str(next_account_number)
    next_account_number += 1

    if acct_type == "1":
        account = BankAccount(name, account_number, initial)

    elif acct_type == "2":
        rate = get_float("Interest rate as a decimal (e.g. 0.02 for 2%): ")
        if rate is None or rate < 0:
            rate = 0.0
        min_bal = get_float("Minimum balance required: ")
        if min_bal is None or min_bal < 0:
            min_bal = 0.0
        account = SavingsAccount(name, account_number, initial, rate, min_bal)

    else:  # "3"
        fee = get_float("Withdrawal fee: ")
        if fee is None or fee < 0:
            fee = 0.0
        account = CheckingAccount(name, account_number, initial, fee)

    accounts[account_number] = account
    print(f" Account created! Account number: {account_number}")


def deposit_menu():
    account = choose_account()
    if account is None:
        return
    amount = get_float("Amount to deposit: ")
    if amount is None:
        print(" Deposit cancelled.")
        return
    account.deposit(amount)


def withdraw_menu():
    account = choose_account()
    if account is None:
        return
    amount = get_float("Amount to withdraw: ")
    if amount is None:
        print(" Withdrawal cancelled.")
        return
    account.withdraw(amount)


def check_balance_menu():
    account = choose_account()
    if account is None:
        return
    account.show_balance()


def add_interest_menu():
    account = choose_account()
    if account is None:
        return
    if not isinstance(account, SavingsAccount):
        print(" This option is only available for savings accounts.")
        return
    account.add_interest()


def history_menu():
    account = choose_account()
    if account is None:
        return
    account.show_history()


def main():
    print("Welcome to the Bank Account System!")

    actions = {
        "1": create_account,
        "2": deposit_menu,
        "3": withdraw_menu,
        "4": check_balance_menu,
        "5": add_interest_menu,
        "6": history_menu,
    }

    while True:
        print(MENU)
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Thank you for using the Bank Account System. Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print(" Invalid option. Please choose a number from 1 to 7.")
            continue

        try:
            action()
        except Exception as error:
            print(f" Something went wrong, but the program will continue: {error}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
    except EOFError:
        print("\n\nNo more input received. Goodbye!")