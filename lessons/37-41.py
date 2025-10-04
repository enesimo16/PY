import copy


fruit=["grape","watermelon"]
myNumber=list((1,2,3,4,5,6,7,8,9))
print(fruit)
print(myNumber)

fruit2=["grape","watermelon","grape","watermelon"]
fruit2=list(dict.fromkeys(fruit2)) #dict haline getirip tekrarlayanları yok eder.
print(fruit2)

fruit3=["grape","watermelon"]
new_fruit=fruit3+["lemon"]
print(new_fruit)
print(len(new_fruit))

fruit4=["grape","watermelon"]
fruit4.append("cherry")
print(fruit4)

fruit5=["grape","watermelon"]
fruit5.insert(1,"chocolate")
print(fruit5)

fruit5=["grape","watermelon"]
fruit_taple=["melon","orange"]
fruit5.extend(fruit_taple)
print(fruit5)

fruit6=["grape","watermelon"]
new_fruit2=fruit.copy()   # aynı zamanda copy işlemi fruit[:] ile de yapılır.
new_fruit2.append("apple")
print(fruit6)
print(new_fruit2)

list1=[[1,2],[3,4]]
new_list=copy.deepcopy(list1)  # cok boyutluda kopyalama işlemi fakat import copy yapmak gerek.
new_list[0][0]=70
new_list[0][1]=19
new_list[1][1]=34

print(list1)
print(new_list) # [1][0] ı yapmadığımız için 3 aynen geldi.

fruit7=["grape","watermelon"]
fruit7.remove("grape")  # çıkarma işlemi.
print(fruit7)

fruit8=["grape","watermelon"]
fruit8.pop() # sondan çıkarma.
print(fruit8)
#del fruit8 # tamamen siler ve hata verir.
print(fruit8)
fruit7.clear() # içeriklerini siler.
print(fruit7)

fruit8=["grape","watermelon"]
myNumber2=list((1,2,3,4,5,6,7,8,9))
result=fruit.index("grape")
print(result)
result2=fruit.count("grape")
print(result2)

fruit9=["grape","watermelon","melon","Orange","Lemon"]
myNumber3=[9,7,6,5,8]

fruit9.sort   # sort islemi büyük kücük algılar bu yüzden dogru yapmaz.
myNumber3.sort

print(fruit9)
print(myNumber3)

fruit9.sort(key=str.lower) # bu sekilde hepsini kücük harf yapipi siralama yaparsak daha dogru olur.
print(fruit9)

fruit10=["grape","watermelon","melon","orange","lemon"]

fruit10.sort(reverse=True) # geriye doğru sıralama yapar.
print(fruit10)

def mySort(x):
    return abs(x-20) #abs absolute mutlak demektir.

myNumberX=[9,7,6,5,8]
myNumberX.sort(key=mySort)
print(myNumberX)