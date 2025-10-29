class Account:
    def __init__(self,owner, balance=0):
        self.owner = owner
        self._balance  = balance

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")


    def get_balance(self):
        return self._balance
    
account = Account("John Doe",1000)                 
account.deposit(500)
print(f"Account Balance: ${account.get_balance()}")