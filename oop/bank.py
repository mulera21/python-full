#--------------bank system-----------------

class BankAccount:

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