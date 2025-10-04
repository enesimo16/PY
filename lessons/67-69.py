# dictionary

car={
    "brand":"Skoda",
    "model":"Octavia",
    "fuel":"Electric",
    "colors":["red","gray","dark"],
    "year":2025, #sayilmaz
    "year":2024, #sayilmaz
    "year":1750
}


print(car)
print(car["brand"])
print(len(car))

person=dict(name="Enes",age=20,country="Turkey")

print(person)
print(f"{person.get('name')}-{person.get('age')}-{person.get('country')}")

my_keys=person.keys()
print(my_keys)
person["student"]=True
print(my_keys)

my_values=person.values()
person["country"]="USA"
print(my_values)

print(car.items())

result=car.items()
print(result)
car["year"]=1999
print(result)

car.update({"year":2030})
print(car)

for item in car: #keyleri gösterir. car.keys
    print(item)
    
for item2 in car: # ya da car.value
    print(car[item2])
    

for key_item,value_item in car.items():
    print(f"{key_item}-{value_item}")
    

# yazarak kopyalanmaz! copy methodu kullan!

car2=car # X
print(car2)
car["year"]=2000
print(car2)

car2=car.copy()   #car2=dict(car) olarak da yapılabilir.
print(car2)
car["year"]=2000
print(car2)

myFriends={
    "friend1":{
        "name":"Enes Yel",
        "year":2005
    },
    "friend2":{
        "name":"Dilek Yel",
        "year":2001
    },
}

print(myFriends)

print(myFriends["friend2"]["year"])

for outer_key,outer_value in myFriends.items():
    print(outer_key)
    for inner_key in outer_value:
        print(inner_key+":",outer_value[inner_key])
        

myKeys=("key1","key2")
myValue=7
result1=dict.fromkeys(myKeys)  # değer atıyor.
print(result1)




