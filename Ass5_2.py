#Prg:2 Write a higher order function to find out the reduced output of the
#range(1,10) after using an association function as multiplication.

from functools import reduce
list=range(1,10)
res=reduce((lambda p,q:p*q),list)
#res=map(lambda n:n*n,range(10))
print("The Reduce result is:",res)
