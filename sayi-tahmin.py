#it is a number guessing game.

import random

random_number=random.randint(1,100) #random number between 1 to 100.
remaining_attempts=5 # deneme sayisi
score=100 # score
attempt_count=0 # yapilan deneme sayisi
print("Guess a number between 1 and 100.")
print(f"Your starting score: {score}")

while(remaining_attempts>0):
    guess=int(input("Your guess:")) #tahmin almak
    attempt_count+=1 # yapılan denemeyi arttir
    if(guess<1 or guess>100):
        print("Please! Enter a number between 1 and 100.")
        continue # diğer alt kodları okumaması icin. tekrar inputa döner
    if(guess==random_number):
        print(f"Congrulations! You guessed the number correctly on your {attempt_count}.attempt.")
        print(f"Your total score: {score}")
        break
    elif(guess<random_number):
        print("Try a larger number.")
    else:
        print("Try a smaller number.")
    remaining_attempts-=1
    score-=10
    if(remaining_attempts>0):
        print(f"Remaining attempts: {remaining_attempts}")
        print(f"Current score: {score}")
    else:
        print("Unfortunately! You ran out of attempts!")
        print(f"Your total score: {score} and number in memory is {random_number}")
