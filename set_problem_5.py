#Write a Python program that takes two sets and prints their symmetric difference.
#Return a set that contains all items from both sets, except items that are present in both sets:
x = {"Kotha","Moni","Shakila","Akash"}
y = {"Akash","Nabo","Namro"}
z = x.symmetric_difference(y)
print("The Symmetric difference between two sets is:",z)