
bal=3000
import math
import random
class bank:
    def __init__(self):
        self.bal=3000
        print("Hello! Welcome to our Bank:")
        
def newaccount(self):
    print("You choose to create new account")
    print("Welcome to the OTP Bank:")
    name=input("Enter your name:")
    age=input("Enter your age:")
    add=input("Enter your address:")
    con=input("Enter your contact detail:")
    gen=input("Enter your gender:")
    print("This is your Deatils:")
    return self.name,self.age,self.add,self.con,self.gen

    #print("Your name is:",name,"\nYour age is:",age,"\nYour add is:",add,"\nYour contact detail:",con,"\nYour gender is:",gen)
def withdraw(self):
    amt=float(input("Enter the amount to withdraw:"))
    if amt in(100,1000):
        self.bal=bal-amt
        print("Here your money:")
        return self.bal
    else:
        print("Limited Excess:")
def deposit(self,amt):
    dep= int(input("Enter the amount to deposit:"))
    if dep%5==0:
        print("You successfully deposited amt:")
        self.bal=bal+dep
        return self.bal      
    else:
        print("Enter valid amt:")
def enquiry(self):
    print("Your net balance is:", bal)
    return self.bal
def dd(self):
    print("Your need to enter your bank detail:")
    bandet=input("enter the bank name:\n")
    acthol=input("Enter the acct holder name:\n")
    branch=input("Enter the branch name:\n")
    totamt=input("Enter the total amount:\n")
    return self.bandet,self.acthol,self.branch,self.totamt

bal=3000
selection=0
loop=1
s=bank()
while loop ==1:
    print("Enter your Choice by selecting number:")
    selection= int(input("Press \n 1. NEW account \n 2. WithDraw \n 3. Deposit \n 4. Balance inquiry \n 5. Demand Draft \n 6. Cancel \n"))
    if selection==1:
        s.newaccount()
    elif selection ==2:
        s.withdraw()
    elif selection==3:
        s.deposit()
    elif selection ==4:
        s.enquiry()
    elif selection == 5:
        s.dd()
    elif selection==6:
        exit
    loop==0
    print("Thank you")
        

    
    

