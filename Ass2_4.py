#List of numbers which has cube of odd num.

start, end = 1, 50
for num in range(start, end+1):
    if num %2!=0:
        print(num**3,end = "\n")
    

