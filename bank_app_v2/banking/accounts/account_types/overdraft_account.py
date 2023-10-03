from banking.accounts.bank_account import BankAccount

class OverdraftAccount(BankAccount):

    def __init__(self, accountNumber, name, password, balance):
        super().__init__(accountNumber, name, password, balance)

