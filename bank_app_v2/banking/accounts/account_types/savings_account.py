from banking.accounts.bank_account import BankAccount
import banking.banking_exceptions as ex

class SavingsAccount(BankAccount):

    def __init__(self, min_balance, accountNumber, name, password, balance):
        super().__init__(accountNumber, name, password, balance)
        self._min_balance = min_balance

    def check_min_balance(self, amount):
        return True if ((self._balance - amount) >= self._min_balance) else False

    def withdraw(self, amount, password):
        if(not self.check_min_balance(amount)):
            raise ex.InsufficentBalanceException(self._account_number, amount-self._balance-self._min_balance)
        
        return super().withdraw(amount, password)
