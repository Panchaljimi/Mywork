class bank:
    def __init__(self):
        self.bal = 0
        print("Hello! Welcome to our Bank")
        


    def newaccount(self,name,age,add,con,gen):
        print("You choose to create new account")
        print("Welcome to the OTP Bank:")
        self.name = name
        self.age = age
        self.add = add
        self.con = con
        self.gen = gen
        print("Name:{}".format(self.name))
        print("age :{}".format(self.age))
        print("address:{}".format(self.add))
        print("contact deatils:{}".format(self.con))
        print("gender :{}".format(self.gen))
    def withdraw(self):
        amt = float(input("Enter the amount to withdraw:"))
        if 100<=amt<=1000:
            self.bal = self.bal - amt
            print("Here your money:{}".format(amt))
            print("Your  balance Aftr withdraw:",self.bal)
        else:
            print("Limited Excess")


    def deposit(self):
        dep = int(input("Enter the amount to deposit:"))
        if dep % 5 == 0:
            print("You successfully deposited amt:")
            self.bal = self.bal + dep
            print("Amount deposited:{}".format(dep))
            print("Your Current Balance is:",self.bal)
        else:
            print("Enter valid amt:")


    def enquiry(self):
        print("Enter your Choice by selecting number:")
        selection= 0
        while True:
            selection = int(input(
            "Press \n 1. Deposit amount \n 2. Outstanding Balance \n 3. Minimum Due amount \n"))
            if selection == 1:
                print("Deposit amount{}".format(self.bal))
                break
            if selection == 2:
                print("Oustanding Balance{}".format(self.bal))
                break
            if selection == 3:
                print("Minimum Due amount{}".format(self.bal))
                break

    def dd(self,bank,account_holder,branch,total_amt):
        print("Your need to enter your bank detail:")
        self.bank =bank
        self.account_holder = account_holder
        self.branch = branch
        self.total_amt = total_amt
        print("bank:{}".format(self.bank))
        print("account_holder:{}".format(self.account_holder))
        print("branch:{}".format(self.branch))
        print("total_amount:{}".format(self.total_amt))
        
selection = 0
loop = 1
s = bank()
while loop==1:
    otp = int(input("Enter OTP no:"))

    if otp==1234:

        print("Enter your Choice by selecting number:")
        selection = int(input(
            "Press \n 1. NEW account \n 2. WithDraw \n 3. Deposit \n 4. Balance inquiry \n 5. Demand Draft \n 6. Cancel \n"))
        if selection == 1:
            name = input("Enter your name:")
            age = input("Enter your age:")
            add = input("Enter your address:")
            con = input("Enter your contact detail:")
            gen = input("Enter your gender:")
            s.newaccount(name,age,add,con,gen)

        elif selection == 2:
            s.withdraw()
        elif selection == 3:
            s.deposit()
        elif selection == 4:
            s.enquiry()
        elif selection == 5:
            bank = input("enter the bank name:\n")
            account_holder = input("Enter the acct holder name:\n")
            branch = input("Enter the branch name:\n")
            total_amt = input("Enter the total amount:\n")
            s.dd(bank,account_holder,branch,int(total_amt))
        elif selection == 6:
            exit
    else:
        if otp!=1234:
            print("Sorry, try again")
            break
