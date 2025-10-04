import random

grades = []

def generate_grades():
    for _ in range(100):
        grade = random.normalvariate(70, 10)
        grade = max(0, min(100, round(grade)))
        grades.append(grade)
    return grades


midterm=float(input("Enter the midterm grade: "))
quiz=float(input("Enter the quiz grade: "))
final_exam=float(input("Enter the final exam grade: "))

average=(midterm*0.4)+(quiz*0.1)+(final_exam*0.5)
average = round(average)
grades.append(average)
print(f"Your average grade is {average} . If you want to learn your letter grade please fill the surveys!")

print("School Survey (Please rate from 1 to 5)\n")

q1 = input("1. Do you generally like your school?        (1-5): ")
q2 = input("2. Are the teachers attentive enough?        (1-5): ")
q3 = input("3. Is the school clean enough?               (1-5): ")
q4 = input("4. Do you feel safe at school?               (1-5): ")
q5 = input("5. Are the prices in the canteen reasonable? (1-5): ")

#print("\nYour Survey Answers:")
#print("Question 1:", q1)
#print("Question 2:", q2)
#print("Question 3:", q3)
#print("Question 4:", q4)
#print("Question 5:", q5)

print("Your department is part of the bell system, so your letter grade will be determined accordingly.")

generate_grades()

sorted_grades=sorted(grades, reverse=True)

user_ = sorted_grades.index(average)

if user_ < 20:
    letter = 'A'
elif user_ < 40:
    letter = 'B'
elif user_ < 60:
    letter = 'C'
elif user_ < 80:
    letter = 'D'
else:
    letter = 'F'

print(f"Your letter grade is: {letter}")