# Assignment 5.2
# Create a model for represening a bank account It should have

#   account number
#   name
#   password
#   balance
#   interest rate
#   It should support

# deposit

#   should fail for negative maount

# withdraw

#   should fail if
#       amount <0
#       amount>balance
#       wrong password

# credit interest
#    credits one month interest using forumula
#     balance+=(balance*rate/1200)

# info

class BankAccount():
    
    accounts = set()
    
    # constructor of Bank class
    def __init__ (self, accountNo, name, password, balance = 0, interest_rate = 3):
        self.account_no = accountNo
        self.name = name
        self.password = password
        self.balance = balance
        self.interest_rate = interest_rate
        
    # deposite the money to account
    def deposite(self):
        
        amount = int(input("Enter the amount to be deposited: "))
        if(amount<=0):
            return "Invalid Amount"
        
        # update amount in balance
        self.balance += amount
        return f"Amount ${amount} successfully deposited\nBalance: {self.balance}"
    
    # withdraw the money from account
    def withdraw(self):
        
        amount = int(input("Enter the amount to be withdrawn: "))
        if(amount<=0):
            return "Invalid amount"
        
        elif(amount> self.balance):
            return "Insufficient balance"
        
        pass_word = str(input("Enter the password: "))
        
        if(pass_word != self.password):
            return "Wrong password"
        
        # update the balance in the account
        self.balance -= amount
        return f'Amount ${amount} successfully withdrawn \nBalance: {self.balance}'
    
    # credits one month interest using forumula
    def credit_interest(self):
        
        # let the default rate be 3
        self.balance += ((self.balance * self.interest_rate)/1200)
        return f'Monthly interest is credited to your account. \nBalance: {self.balance}'
    
    def info(self):
        return f'Account No: {self.account_no} \nName: {self.name} \nBalance: {self.balance}'

import random 
import string

def create_account(name, password):
    
    # generating the account number automatically
    while True:
        account_no = ''.join(random.choice(string.digits) for _ in range(8))
        if account_no not in BankAccount.accounts:
            BankAccount.accounts.add(account_no)
            break
            
    b = BankAccount(account_no, name, password)
    print(b.withdraw())
    
    print()
    print(b.deposite())
    
    print()
    print(b.withdraw())
    
    print()
    print(b.info())
    
    print()
    print(b.credit_interest())
    
    print()
    print(b.info())

create_account("Jyothi", "Jyo252!")
