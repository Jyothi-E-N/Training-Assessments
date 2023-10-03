from banking.accounts.bank_account import BankAccount

class CurrentAccount(BankAccount):

    def __init__(self, accountNumber, name, password, balance):
        super().__init__(accountNumber, name, password, balance)

    def credit_interest(self):
        # no interest
        return super().credit_interest(0)