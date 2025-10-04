number=int(input("Enter a integer: "))

print("Odd numbers:")
for item in range(number):
    if(item%2==0):
        continue
    print(item, end=" ")
else:
    print("\nEven numbers:")
    for item2 in range(number):
        if(item2%2==1):
            continue
        print(item2,end=" ")
    