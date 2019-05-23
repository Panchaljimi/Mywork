#write a program to take out the elements from their index values.
import re
x="Hello&*$$world"
new=re.sub('[\w]'," ", x)
print(new)

	
