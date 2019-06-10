import random
r="abcdef^&*()ghijkl,7890JKLMNOPQRSTUVWXYZ!@#$%"
def password(n):
	p="".join(random.sample(r,n))
	return p
a=password(8)
print(a)
