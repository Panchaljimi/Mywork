x=[1,2,3,4,5,6,7,8,9,10]
def fun(x,n=3):
    for i in range(0,len(x),n):
        if n == len(list(x[i:i+n])):
            yield x[i+n:i:-1]
print(list(fun(x)))
