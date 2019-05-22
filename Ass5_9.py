my_list=[1,2,3,4,5,6,7,8,9,10]
n=3
my_result=[my_list[i*n:(i+1)*n]for i in range((len(my_list)+ n-1)//n)]
print(my_result)
