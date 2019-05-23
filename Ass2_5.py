#Copy the list and create new list which have multiplication of 3 
main_lst=[]
x=int(input("Enter the number of elements:"))
for i in range(0,x):
	val=int(input())
	main_lst.append(val)
print(main_lst)
new_lst=[i*3 for i in main_lst]
print("New copy list mutliply by 3:",new_lst)
