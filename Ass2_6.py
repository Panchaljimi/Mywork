# Program to calculate the lenght of each word in the sentence.
x=str(input("Enter the String:"))
print(x)
Ans=[]
for i in x.split():
    word_len=len(i)
    Ans.append(word_len)
print ("The lenght of each word:" ,Ans,end =" ")

