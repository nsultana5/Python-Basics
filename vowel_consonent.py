 #Assignment 3:Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

input_char = input("Enter a single character:")
def vowel_consonant_classify(char):
    vowels="aeiouAEIOU"
    if char in vowels:
        print("It is a vowel.")
    else:
        print("It is a consonant.")

output = vowel_consonant_classify(input_char)
