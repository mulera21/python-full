#--------------bank system-----------------

class BankAccount:
    def __init__(self, balance, account_holder):
        self.balance = balance
        self.account_holder = account_holder
        self.transaction_history = [] # store transaction history

    def deposit(self, amount):
        #addd money to bank account
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ksh {amount}")
            print(f" ksh {amount} deposited. New balance: ksh{self.balance}")
        else:
            print("Invalid deposit amount.")    


    def withdraw(self, amount):
        #remove money from bank account
        if self.balance >= amount > 0 :
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ksh {amount}")
            print(f" ksh {amount} withdrawn. New balance: ksh{self.balance}")
        else:
            print("Invalid withdrawal amount.")    

    def check_balance(self):
        #check current balance
        print(f" Account holder: {self.account_holder}. Current balance: ksh{self.balance}")

    def print_transaction_history(self):
        print("------------------------------------------------------------")
        print(f"Transaction History: {self.account_holder}")
        for transaction in self.transaction_history:
            print(transaction)

class BankSystem:
    def __init__(self):
            self.accounts ={} #initialize the bank system with multiple accounts
    def create_account(self, name, initial_balance=0):
        self.accounts[name] = BankAccount(initial_balance, name)

    def get_account(self, name):
        return self.accounts.get(name, None)



#my_account.deposit(100)
#my_account.withdraw(10)
#my_account.print_transaction_history()

bank = BankSystem()

bank.create_account("John", 100)
John_account = bank.get_account("John")
if John_account:
    John_account.deposit(50)
    John_account.withdraw(20)
    John_account.print_transaction_history()