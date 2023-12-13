#Assignment 5:Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b,c) of a quadratic equation as input and calculates and prints the real roots (if they exist)
#or a message indicating the complex roots.
from math import sqrt
a=float(input("Enter first coefficient a:"))
b=float(input("Enter second coefficient b:"))
c=float(input("Enter third coefficient c:"))

def quadratic_solver(x,y,z):
    d=y*y - 4 *x*z
    if d>0:
        x1=(-y+sqrt(d))/(2 *x)
        x2=(-y-sqrt(d))/(2 *x)
        print("Real and distinct roots:",(x1,x2))
    elif d==0:
        x=x1=x2=(-y)/(2 * x)
        print("Real and identical roots:",x)
    else:
        print("Complex roots:")

quadraticSolver = quadratic_solver(a,b,c)    
