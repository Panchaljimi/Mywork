#ASSINGMENT -3 "OTP PASSWORD"

import random
x=random.randrange(20)
first=input("enter your first name:")
last = input("enter your last name:")
print("Random no is:",x)
#print(x)
user_value = int(input("Enter the num between 1 to 20:"))
if user_value > 20:
    print("value is not valid")
else:

    if user_value == x:
        print("OTP matched")
    else:
        print("OTP not matched")
        user_preference = str.lower(input("Enter your choice 'yes' or 'no':"))
        if user_preference == 'yes' or 'y':
            i= 0
            while(i<3):
                i = i + 1
                user_value = int(input("Enter the num between 1 to 20:"))

                if user_value == x:
                    print("OTP matched")
                    break

                else:
                    print("OTP not matched")
            if i <=4:
                print("program crashed")
        else:
            if user_preference == 'no' or 'n':
                print("Thanks for attempt")
