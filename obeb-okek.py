number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))

smaller=min(number1,number2)

for i in range(smaller,0,-1):
    if(number1%i == 0 and number2%i == 0):
        gcd=i
        break
lcm=(number1*number2)//gcd
print(f"The GCD of {number1} and {number2} is {gcd}") # greatest common divisor
print(f"The GCD of {number1} and {number2} is {lcm}") # least common multiple

for i in range(smaller,0,-1):
    print(i,end=" ")