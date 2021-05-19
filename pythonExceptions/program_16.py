"""
16. Write a program to generate NumberFormatException
"""

try:
    x=int(input("Enter a value: "))
    print("Try Block:Enter Number is: ",x)
except ValueError as ve:
    print("Invalid Input Enter Only Numbers");