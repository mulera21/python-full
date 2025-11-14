#--------------bank system-----------------

class BankAccount:
    def __init__(self, balance, account_holder):
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        #addd money to bank account
        self.balance += amount
        print(f" &{amount} deposited. New balance: {self.balance}")


    def withdraw(self):
        #remove money from bank account
        pass

    def check_balance(self):
        #check current balance
        pass

my_account = BankAccount()
my_account.deposit()