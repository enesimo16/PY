fruits=["grape", "watermelon","blackberry"]

for item in range(len(fruits)):
    print(fruits[item])
    
i=0

while(i<len(fruits)):
    print(fruits[i])
    i+=1
    
[print(item) for item in fruits]   #list comprehension

new_list=[]

for item in fruits:
    if("g" in item):
        new_list.append(item)
print(new_list)

new_list=[item for item in fruits if("g" in item)] #üsttekinin kısa hali

print(new_list)