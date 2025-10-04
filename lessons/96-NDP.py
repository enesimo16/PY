#OBJECT ORIENTED PROGRAMMING WITH PYTHON

class myClass:
    x="This is a test class."

obj=myClass()
print(obj.x)


class vehicle:
    brand="skoda"
    model="superb"
    color="white"

car_obj=vehicle()
print("brand=",car_obj.brand)

class car:
    def __init__(self,brand,model,color): #constructor
        self.brand=brand
        self.model=model
        self.color=color
        
car1=car("Renault","Symbol","Gray")
print(car1.brand,"-",car1.model,"-",car1.color)