class Car:

    def __init__(self,modelname,topspeed):
        self.modelname = modelname
        self.topspeed = topspeed

    def forward(self):
        print("All wheels go forward")

    def backward(self):
        print("All wheels go backward")


bmw=Car("M30",200)

bmw.forward()

print(bmw.modelname)
print(bmw.topspeed)

toyota=Car(500,100)
toyota.backward()
print(toyota.topspeed)