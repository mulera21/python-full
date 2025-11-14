#--------------bank system-----------------

class BankAccount:
    def __init__(self, balance, account_holder):
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        #addd money to bank account
        if amount > 0:
            self.balance += amount
            print(f" ksh {amount} deposited. New balance: ksh{self.balance}")
        else:
            print("Invalid deposit amount.")    


    def withdraw(self, amount):
        #remove money from bank account
        if amount > 0 :
            self.balance -= amount
            print(f" ksh {amount} withdrawn. New balance: ksh{self.balance}")
        else:
            print("Invalid withdrawal amount.")    

    def check_balance(self):
        #check current balance
        pass

my_account = BankAccount(0, "John Doe")
my_account.deposit(100)
my_account.withdraw(27)