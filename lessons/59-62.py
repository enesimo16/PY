# tuple

fruits=("orange","lemon","cherry","peach","sunflower")
fruits1=("orange",)  # eğer sonuna virgül koyarsak tuple koymazsak str olur
fruits2=("orange")

print(fruits)
print(len(fruits))

print(type(fruits))
print(type(fruits1))
print(type(fruits2))

complex_tuple=("Enes",20)
print(complex_tuple)

print(fruits[1])
print(fruits[0:1])
print(fruits[1:])
print(fruits[-2:-1])

search="apple"

if(search in fruits):
    print(f"yes, {search} is in the fruits tuple.")
else:
    print(f"no, {search} is not in the fruits tuple.")
    
numbers=(5,9,8,51,6)

join_tuple=fruits+numbers
print(join_tuple)

multiply_tuple=fruits*3
print(multiply_tuple)

# veri ekleme değişme cikarma fakat temp ile list yapıp değişip sonra tekrar tuple yapariz

extra_fruits=("blackberry",)

temp_fruits=list(fruits)

temp_fruits[2]="apple"

temp_fruits.append("oil")

fruits=tuple(temp_fruits)

fruits+=extra_fruits

print(fruits)

fruits3=("orange","lemon","cherry")
(x,y,z)=fruits3

print(x,y,z)


i=len(fruits)-1 
for item in fruits:
    if(i>0):
        print(item,end="---")
    else:
        print(item)
    i-=1
    
for item2 in range(len(fruits)):
    print(item2)