text="I could eat strawberry all day."
result=text.find("strawberry") # Bulma işlemi yapar fakat kelime içeride yoksa -1 verir. index de bulur fakat kelime yoksa hata verir.
print(result)   # Aynı şekilde find komunutun r hali de vardır ve sondan hesaplar.
result2=text.index("strawberry")
print(result2)
text3="I could eat strawberry all day. strawberry is the best food ever."
result3=text3.rfind("strawberry")
print(result3)

result4=text3.split(".",1)
print(result4)

text4="70"
result5=text4.zfill(10)
print(result5)