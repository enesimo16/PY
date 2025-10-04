input_number = int(input("Enter a number: "))
prime_numbers=[]

if input_number < 0:
        print("This number is negative. Please enter a positive number.")
elif input_number == 0:
    print("Zero is not a prime number.")
elif input_number == 1:
    print("1 is not a prime number. The smallest prime number is 2.")
else:
    prime_numbers.append(2)
    for i in range(3,input_number+1,2):
        for j in range(3,int(i**0.5)+1):
            if(i%j == 0):
                break
        else:
            prime_numbers.append(i)
    print(f"{prime_numbers}")
