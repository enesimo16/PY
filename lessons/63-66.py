#set

fruits={"orange","lemon","cherry","peach","sunflower","lemon","lemon","lemon",True,1,False,0}
setNumber={1,6,8,9,4,2,5,9,6}
setComplex={"Enes",20}

print(fruits)
print(len(fruits))
print(setNumber)
print(setComplex)

alternativeSet=set((1,69,81,52))
print(alternativeSet)

i=len(fruits)-1
for item in fruits:
    if (i>0):
        print(item,end="-")
    else:
        print(item)
    i-=1

print("enes" not in fruits)

print("*****************************************************************************************************************************************")

fruits.add("added one")
print(fruits)

fruits2={"apricot","pear"}
fruits3={"pipe"}

fruits.update(fruits2) # update yerine | 'de kullanılabilir.
print(fruits)
fruits |= fruits3 | fruits2
print(fruits)

fruits.remove("lemon")
print(fruits)

remove_item=fruits.pop()
print(fruits)
print(f"remove item: {remove_item}")

print("*****************************************************************************************************************************************")

setNumber1={1,9,4,5,6}
setNumber2={98,52,63,48,95,9,6}
setNumber3={7.19,123,9}

result=setNumber1.union(setNumber2)  #yeni set döndürür. ayrıca .union yerine | ifadesi de kullanılabilir.
print(result)

result2=setNumber1.intersection(setNumber2) # iki set'te ortak olanları göster.r

print(result2)

setNumber1.intersection_update(setNumber2,setNumber3) # liste sett farketmeden hesaplar. Kısayolu ise &= ile de yapılabilir.
print(setNumber1)


print("*************************************************************************************************************************************")

result3=setNumber1.difference(setNumber2) # setnumber1 de olup setnumber2 de olmayanları yazar.
print(result3)

result4=setNumber1.symmetric_difference(setNumber2) # kesişim haricini yazar. kısayolu ^
print(result4)

result5=setNumber1.copy()
print(result5)

result6=setNumber1.issubset(setNumber2) # setnumber 1 dekiler settnumber2de var mı kısayolu <=
print(result6)

result7=setNumber1.issuperset(setNumber2) #setnumber 2 dekiler settnubmer1 de var mı kısayolu >=
print(result7)