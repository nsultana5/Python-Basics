#question 1:
#Difference between normal function and lambda function
#A lambda function is denoted by "lambda" then a space and then add a colon followed an operation that we want to perform on our x and y inputs.It has only a single line expression.Lambda function doesn't have a name attached to it.Why are lambda functions useful? So the whole idea of lambda functions , or anonymous functions, are that they're made to be passed into a higher-order function.

#Normal function
def add(a,b):
    return a+b
print(add(2,3))

#Lambda function
print((lambda a,b:a+b)(2,3))

#Lambda function is used to be passed into a higher order function. So what's a higher order function that can either take in another function as an input or return a function as an output, or both.Here is an example:

def map_func(my_func, my_iter):
    result =[]
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)

    return (result)

nums =[3,4,5,6,7]
cubed=map_func(lambda x:x**3,nums)
print(cubed)

#question 2
#Difference between lists and the tuples
#Lists are described using third brackets and Tuples are described using first brackets.
#Lists elements are mutable menas we can remove elements from the list and can add elements in the list. But in tuples we cannot add and remove elements from the tuples means tuples elements are immutable.
#Example:
#list
l=[1,2,3,5,7]
print("Original lists:",l)
l[1]=3
print("Updated lists:",l)

l.append(9)
print("After appending the list is :",l)

#tuple
t =("Apple","banana","orange")
print("Original tuple:",t)
t[1]="Mango"
print("Updated tuple:",t)