# Prg: 01 Write a list comprehension to find out the odd number from the
#range of 1,300 and print TRUE if they are odd and FLASE if they are even.
a=list(range(1,300))
odd=[]
even=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print("False")
print("Even no.:",even)
print("True")
print("odd nos.:",odd)
