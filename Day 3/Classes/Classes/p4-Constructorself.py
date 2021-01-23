class Person:

    def __init__(self,name):
        self.name=name
                            
    def talk(self):
        print(f"Hi, I am {self.name}")
		
        
a = Person("Binary")
a.talk()

b= Person("Decimal")
b.talk()
