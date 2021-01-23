class cat():
    """A simple attempt to model a cat."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a cat sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
        

my_cat = cat('willie', 6)
your_cat = cat('lucy', 3)

print("My cat's name is " + my_cat.name.title() + ".")
print("My cat is " + str(my_cat.age) + " years old.")
my_cat.sit()

print("\nMy cat's name is " + your_cat.name.title() + ".")
print("My cat is " + str(your_cat.age) + " years old.")
your_cat.sit()
