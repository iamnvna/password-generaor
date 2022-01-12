"""
random is the single most important library used in this program..
It combines random characters from a given set to generate an output.
Combined with basic loops and if clauses, this program would accept two inputs and print expected output(s).
"""

# The random library is imported for use in the program.
import random

## The first print statement exists to welcome users to the programe.
# Much like a banner, that is underlined.
print("Welcome to Password Generator")
print("================================================")

## A set of characters are stored in a variable. This variable is later
# called upon by the random library for a set of characters defined by the user.
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"

"""
Two more variables are declared, one to hold the total number
of user passwords; The other to hold the length of the password.
Note that both inputs are wrapped in an integer to convert the string of 
input to integers. 
"""
number=int(input("how many passwords do you need? "))
length=int(input("What length should they be? "))

## The print statement below signifies the commencement of the output.
print("\nHere are your passwords: ")

"""
The random library is called into action here. Using the nested for
loops to ensure that the length and number of passwords match the user
input and does not run infinitely. 
"""
for a in range(number):
    pwd = ""
    for b in range(length):
        pwd += random.choice(chars)
    print(pwd)

print("\nThank you for using our service!")
