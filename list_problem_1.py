#Write a Python program that takes a list as input and returns the first three elements using list slicing
given_input=(input("Enter a list separated by comma:").split(","))
first_three_elements=given_input[:3]
print("First three elements:",first_three_elements)