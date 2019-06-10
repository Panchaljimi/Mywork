class Rectangle():
	def __init__(self,l,w,h):
		self.lenght=l
		self.width=w
		self.height=h
	def rectangle_area(self):
		self.s=(self.lenght+self.width+self.height)/2
		area=(self.s*(self.s-self.lenght)*(self.s-self.width)*(self.s-self.height))**0.5
		if area % 2==0 and len(str(area))==3:
			print("Correct Output")
		else:
			print("Sorry wrong Output")
		return area
a= Rectangle(10,50,40)
print(a.rectangle_area())
