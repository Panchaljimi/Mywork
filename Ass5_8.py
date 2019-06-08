first=[2,3,4,5,6]
sec=[1,11,25,7,11,6,18]
def fun(first,sec):
	return first[::2]+sec[1::2]
	
print(fun(first,sec))
