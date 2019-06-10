x =[1,2,3,4]                                                                               
dic={'a':10,'b':2,'c':4,'d':30}                                                           
lst=[]                                                                                     
for key,value in dic.items():                                                              
    if value in x:                                                                         
        lst.append(value)                                                                  
print(lst)             
