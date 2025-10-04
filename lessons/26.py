text="   MERCEDES   "
result=text.strip()  #lstrip ve rstrip ise sol ve sağdaki yerleri siler. aynı zamanda parantez içine girilen sembol için de yapar.
print("of all cars",result,"is my favo")

text="Hello Python"
result2=str.maketrans("P","T") # P leri T yap.
print(text.translate(result2))

myDict={80:84,108:65,82:72}
result3=str.maketrans(myDict)
print(text.translate(result))

text2="I could eat strawberry all day."
result4=text2.partition("strawberry")  # Ayraç işlemi yapar öncesi ve sonrası.
result5=text2.replace("strawberry","pineapple")
print(result4)
print(result5)

