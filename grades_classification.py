                                        #Assignment 2:Grades Classification

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

