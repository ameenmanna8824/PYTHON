class Car:

	def __init__(self,x,y): # This is a constructor
		self.x=x
		self.y=y
		
	def forward(self): 
		print(" Left Motor Forward")
		print(" Right Motor Forward")
	
bmw=Car(2,3)
bmw.x=10
print(bmw.x)
print(bmw.y)
	