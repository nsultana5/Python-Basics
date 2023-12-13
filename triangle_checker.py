#Assignment 4:Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.

a,b,c = input("Enter three values:").split()
def triangle_type(x,y,z):
    if x==y and y==z and z==x:
        print("This is a Equilaterial triangle.")
    elif x==y or y==z or z==x:
        print("This is a Isosceles triangle.")
    else:
        print("This is a Scalene triangle.")
triangle=triangle_type(a,b,c)