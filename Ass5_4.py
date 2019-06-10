def fun_my(filename):
        with open(filename,'r')as file:
                words=file.read().split()
        max_len=len(max(words,key=len))
        return [word for word in words if len(word)==max_len]
print(fun_my('new.txt'))


#text file with the code as Below:
#Hi,
#how r u?
#i am really very good.
#This is the longest word text document.
