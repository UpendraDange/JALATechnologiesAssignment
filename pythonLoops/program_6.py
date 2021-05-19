"""
Write a program to print even number between 10 to 100
using while loop
"""

num = 10
while num <= 100:
    if num%2 == 0:
        print(num,end=" ")
    num+=1