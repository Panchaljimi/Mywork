x=[1,2,3,4,[10,20,30,40,[100,200,300,400],"riyazulhaque",'5+5j'],4000]
res=[]
def convert(x):
        for i in x:
                if type(i)==list:
                        convert(i)
                else:
                        res.append(i)
print("orignal:",x)
convert(x)
print("Main:",res)
print(res.index(('5+5j')))
