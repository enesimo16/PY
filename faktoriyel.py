#Factorial with while loop!

result=1
i=1
number=int(input("Enter a integer you want to calculate of factorial: "))
while(i<number):
    result*=i
    i+=1  
print(f"The factorial of{number} is as follows (!=) {result}")