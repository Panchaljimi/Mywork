import random
def myinput():
    x=random.randrange(20)
    y=input("Enter the first name:")
    z=input("Enter the last name:")
    i=0
    print (x)
#print(y)
#print(z)

    while True:
        if i==3:
            print("Sorry Program Crashed")
            break
        try:
            num=int(input("Enter the num between 1 to 20"))
        except:
            print("Input valid Number")
            i=i+1
            continue
        if num>20:
            print("Wrong output")
            i=i+1
        elif num==x:
            print("OTP Successfully Matched")
            break
        else:
            i=i+1
            print("Error")
        a= "Do you want to cont..."+ str(3-i)+ " Press Yes to cont... or No to Quit\t"
        input(a)
        if a=="yes":
            continue
        else:
            print("Thanks for attempt")
            break
myinput()

    
        
