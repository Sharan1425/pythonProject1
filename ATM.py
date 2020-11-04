# Bank Application by using classes
import sys
class ATM():
    """ATM Project"""
    Bank_name = "SBI"
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self,Amount):
        self.balance = self.balance + Amount
        print("Available balance is: ", self.balance)
    def withdraw(self,Amount):
        if Amount >= self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - Amount
            print("Available balance is: ", self.balance)

    def Bal_enquiry(self):
        print("Available balance is: ", self.balance)

name = input("Please enter your name: ")
c = ATM(name)
print("Hello {} Welcome to State Bank of India".format(name))
count = 3
password = int(input("Please enter your password: "))
while True:

    if password == 2514 :
        print("Choose the options\nDeposit\nWithdraw\nBalance Enquiry\nExit")
        option = input("Please select option: ")
        if option == "Deposit":
            Amount = int(input("Please enter the deposit amount: "))
            c.deposit(Amount)
        if option == "Withdraw":
            Amount = int(input("Please enter the withdraw amount: "))
            c.withdraw(Amount)
        if option == "Balance Enquiry":
            c.Bal_enquiry()
        if option == "Exit":
            print("Thanks for Banking with SBI")
            sys.exit()
    else:
        print("Incorrect password please enter correct password")
        count = count-1
    if count == 0:
        print("Your account is blocked due to incorrect password")








