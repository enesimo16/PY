text="9845648516"
text2="asagfas454s64adas"
result=text.isdigit()

print(result)
print(text2.isdigit())

a="EnesYEL"
b="3enes"

print(a.isidentifier())
print(b.isidentifier())

c="45646454a"
d="-98"

print(c.isnumeric())
print(d.isnumeric())

e="EnesYEL"
f="Enes\nYel"

print(e.isprintable())
print(f.isprintable())

g="  "

print(g.isspace())

h="Enes Yel Bir Markadır"

print(h.istitle())

Names=("Enes","Dilek","Melek")
result=",".join(Names)
mySeparator=":"
result2=mySeparator.join(Names)

print(result)
print(result2)

x="strawberry"
y="purple"

print(x.ljust(30))
print(y.rjust(30))


