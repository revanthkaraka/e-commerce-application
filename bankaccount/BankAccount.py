class BankAccount:
    def __init__(self,account_number,account_holder,balance=0.0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited is: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self,amount):
        if amount > 0:
            if self.balance>= amount:
                self.balance-= amount
                print(f"withdrawn : ${amount}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")
bankaccount1=BankAccount(1651010009981,"Revanth Karaka",500)
print(f"account_holder:{bankaccount1.account_holder}")
print(f"balance:{bankaccount1.balance}")
bankaccount1.deposit(1000)
print(f"deposit:{bankaccount1.balance}")
bankaccount1.withdraw(277)
print(f"withdraw:{bankaccount1.withdraw}")