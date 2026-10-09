#take input from user
name=input("Enter your name: ")

#   "str" is short for string in python

#remove whitespace from the input
name=name.strip()

#capitalize the input
#name=name.capitalize()     #capitalize only the first letter of the first word
name=name.title()   #capitalize the first letter of each word

#display output
print(f"Hello, {name}")

