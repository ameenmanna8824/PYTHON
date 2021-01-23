class Car:
	def forward(self): # It is a keyword which takes zero arguement
		print(" Left Motor Forward")
		print(" Right Motor Forward")
	
	def backward(self):
		print(" Left Motor Backward")
		print(" Right Motor Backward")
        a=12

#Objects are instances of class. Class is like a blueprint or a templates

bmw=Car()# This creates a new object and lets store it in a variable point1
bmw.x=1 # Objects can also have attributes
bmw.y=2

bmw.forward()#we can now call methods of the object using . operator
print(bmw.a) # We can print the attributes of the object 

alto = Car()
#print(alto.x) #you will get error here saying Car has no attritube x
alto.x = 'Tyre'
print(alto.x)
