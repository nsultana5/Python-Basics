#1write a function called calculate_area that takes base and height as an input and returns an area of a triangle .
def calculate_area(base,height):
    return (1/2 *base *height)

result=calculate_area(3,4)
print(f"Area of a triangle is :{result}")

#2 Modify above function to take third parameter shape type.It can be either "triangle" or "rectangle".Based on shape type it will calculate area. 

def calculate_area(dimension1,dimension2,shape="triangle"):  #dimension1 for triangle=base and for rectangle=height
    if shape=="triangle":                                    #dimension2 for triangle =height and for rectangle=width
        area=1/2*dimension1*dimension2                        #for shape="triangle" or "rectangle"
    elif shape=="rectangle":
        area=dimension1*dimension2
    else:
        print("Error:Input shape is neither triangle nor rectangle")
        area =None

    return area

triangle_area = calculate_area(5, 4, "triangle")
print("Triangle Area:", triangle_area)

rectangle_area = calculate_area(5, 10, "rectangle")
print("Rectangle Area:", rectangle_area)

default_triangle_area = calculate_area(5, 10)
print("Default Triangle Area:", default_triangle_area)

#3 Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3

def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

res=print_pattern(3)

#for input 4

def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

res=print_pattern(4)