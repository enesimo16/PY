#conditional expressions

a= int(input("Enter a integer: "))
b=int(input("Enter another integer: "))

if(a>b):
    print(f"{a} is greater than {b}")
elif(a<b):
    print(f"{b} is greater than {a}")
else:
    print(f"{a} and {b} are equal.")
    


print(f"{a} is greater than {b}") if (a>b) else print(f"{a} and {b} are equal.")  if(a==b) else print(f"{b} is greater than {a}")# ternary operators , güclü ifadeler, kosullu ifadeler.