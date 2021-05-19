"""
Write a program to palindrome or not
"""
pyStr=input("Enter a string:")

temp=pyStr[::-1]
if temp == pyStr:
    print("String is palindrome")
else:
    print("String is not palindrome")