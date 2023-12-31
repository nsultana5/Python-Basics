#Accident=Exception
#Detour=Handling exception
#multiple exception handling
#1:ZeroDivisionError
x=int(input("Enter number1:"))
y=int(input("Enter number2:"))
try:
    z=x/y
#except Exception as e:                    it's a generic exception
except ZeroDivisionError as e:             #it's a specific exception
    print(f"Division by zero exception")
    z=None

print(f"Divison is:{z}")

#2:TypeError
num1=int(input("Enter a number:"))
num2=input("Enter a string:")
try:
    z1=num1+num2
#except Exception as e:                               #generic exception
except TypeError as e:
    #print(f"exception type:{type(e).__name__}")       #find the type of exception
    print(f"Type error exception.")
    z1=None

print(f"Addition is :{z1}")

