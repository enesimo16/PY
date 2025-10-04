#Comparing Methods
if 2>7:
    print("it is true")

#Variables
x=7
y="python"
z=int(10)
print(x)
print(y)
print(z)

x="exchange" #Data is exchangeable
print(x)
print(type(x)) #Finding type

name="enes"
lastname=name
print(lastname)

colors=["white","red","blue"] #Variables unpacking
x,y,z=colors
print(x,y,z)
print(x+y+z)

def myFunctions():
    print("Enesimo is a",x)
myFunctions()

name="enes" #string
age=20 #integer
weight=87.5 #float
comp=2j #complex
print("isim:",name,"yas:",age,"kilo:",weight,"karmasiksayi:",comp)

myList=["white","red","blue"] #List
myTuple=("white","red","blue") #Unchanged list
myRange=range(7) #Range data type for loops
myDict={"name":"enes","age":20} #dict data type

print(myList,myTuple,myDict)
print(*myRange)

#pi=3.14
#radius_of_circle=float(input("Yarı cap:"))
#area_of_circle=pi*radius_of_circle*radius_of_circle
#circumference_of_circle=2*pi*radius_of_circle
#print("Alan:" , area_of_circle)
#print("Cevre:", circumference_of_circle)

import random

state=random.getstate() #Keeping the random number of downside
print(random.random())
random.setstate(state) #Rewriting the random number that has keeped
print(random.random())

random.seed(5) #It is const of random modules
print(random.random())

