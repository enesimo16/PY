# Asal sayı kontrol uygulaması



while True:
    input_number = int(input("Enter a number: "))
    
    if input_number < 0:
        print("This number is negative. Please enter a positive number.")
    elif input_number == 0:
        print("Zero is not a prime number.")
    elif input_number == 1:
        print("1 is not a prime number. The smallest prime number is 2.")
    else:
        isPrime = True
        for i in range(2, int(input_number ** 0.5) + 1):
            if input_number % i == 0:
                isPrime = False
                break

        if isPrime:
            print(f"{input_number} is a prime number.")
        else:
            print(f"{input_number} is not a prime number.")