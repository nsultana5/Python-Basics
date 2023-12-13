#Write a Python program that takes a year as input and determines if it is a leap year or not.
#Condition for leap year
# 1.A year is a leap year if it is divisible by 400 2.A year is a leap year if it is divisible by 4 but not devisible by 100.
input_year =int(input("Enter a year:"))                      #user input

def is_leap(year):                                           #define a function called is_leap.
    if (year %400 ==0) or(year %4 ==0 and year %100 !=0):
        return True                                          #if block
    return False                                             #else block

result=is_leap(input_year)
if result:
    print("This is a leap year")
else:
    print("This is not a leap year")


    


    

           
