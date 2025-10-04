import math

myNumber=int(input("Enter a number: "))
square_root=math.sqrt(myNumber)   # = myNumber**0.5

if(square_root==int(square_root)):
    print(f"The square root of {myNumber} is an integer: {int(square_root)}")
else:
    print(f"The square root of {myNumber} is not an integer: {square_root:.3f}")

