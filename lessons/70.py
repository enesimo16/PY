def myName(fname):
    print(fname+" YEL")
    
myName("Enes")

def names(*args):  # çoklu parametre için *
    print("My real name is "+args[0])
    
names("enes","dilek")

def my_name(name1,name2):
    print("My real name is "+name2)
    
my_name(name1="enes", name2="sükrü")


def lastname(**kwargs):
    print("His lastname is "+kwargs["lastname"])
    
lastname(firstname="Enes",lastname="YEL")


def my_fruits_function(food):
    for item in food:
        print(item)

fruits=["grape","orange"]

my_fruits_function(fruits)

def math(x):
    return x*10

print(math(100))

def my_sum(x,y):
    result=x+y
    return result

result=my_sum(4,6)
print(result)