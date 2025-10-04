text="Welcome to my World. My world is python"

result=text.count("world")
result2=text.count("my",2,18)
result3=text.startswith("Welcome")
result4=text.endswith("python")

print(result)
print(result2)
print(result3)
print(result4)

text2="P\ty\tthon"

print(text2.expandtabs(2))
print(text2.expandtabs(8))

result5=text.find("python")
result6=text.find("enes")

print(result5)
print(result6)

text3="enes"

result7=text.isalnum()  
result8=text3.isalnum()

print(result7)
print(result8)

result9=text.isalpha()
result10=text3.isalpha()

print(result9)
print(result10)

text4="512"

result11=text4.isdecimal()

print(result11)