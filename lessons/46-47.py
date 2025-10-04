#for loop

fruits=["orange","watermelon","cherry","lemon"]

for item in fruits:
    print(item)
    
i=0
for item in fruits:
    print(i,".index=",item)
    i+=1
    
#list,tuple,dictionary,set=iterable,iteration, yenilenebilir

for i in "python":
    print(i)
    
for a in fruits:
    if(a=="cherry"):
        break
    print(a)
    
print(range(8))

for c in range(3,8):
    print(c,end=" ")
for d in range(3,28,2):
    print(d)
else:
    print("For loop is over!")
    
for e in range(3,8):
    if (e==7):
        pass #pas ve ... boş bırakmak içindir.
    else:
        print(e)
else:
    print("for loop is over!")

for f in range(3,8):
    if (f==7):
        ... # pass ile aynıdır.
    else:
        print(f)
else:
    print("for loop is over!")
    

adj=["red","big","nature"]
food=["orange","watermelon","lemon"]
myNumbers=[[3,4],[5,6]]

for outer in adj:
    for inner in food:
        print(outer,inner)
        
        
for n1,n2 in myNumbers:
    print(f"{n1},{n2}")
    
    
fruits2=["orange","watermelon","lemon"]

for index,item2 in enumerate(fruits2):
    print(f"{index},{item2}")

name=["enes","melek"]
ages=[20,20]

for name,ages in zip(name,ages):
    print(f"{name} is {ages} years old.")