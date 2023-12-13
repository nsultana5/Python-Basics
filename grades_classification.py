# Assignment 2:Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria:
– 90% or above: A+
– 80-89%: A
– 70-79%: B
– 60-69%: C
– Below 60%: Fail                                       

input_percentage = int(input("Enter the percentage:"))                   #user input
def grade_classify(percent):                                             #define a function
    if percent >= 90:
        print("Grade is A+!")
    elif (percent >=80 and percent <=89):
        print("Grade is A.")
    elif (percent >=70 and percent <=79):
        print("Grade is B.")
    elif (percent >=60 and percent <=69): 
        print("Grade is C.")
    else:
        print("Fail.")
final_grade=grade_classify(input_percentage)

