# Ass2_7 program to return true if list contain only integer or false
num=input("Enter your num to check weather it is int or not:")
try:
	new_num=int(num)
	print("Yes it is an integer num:",new_num)
except:
	print("No, Your num is not an int:",new_num)
	
