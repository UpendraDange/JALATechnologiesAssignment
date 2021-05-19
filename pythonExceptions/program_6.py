"""
6. Write a program to create your own exception
"""


def GetAge(age):
    assert age>18,"Age Must not Be less than 18Years"
    print("You are Allow to Access: ",age)

age = int(input("Enter Age:"))
GetAge(age)
