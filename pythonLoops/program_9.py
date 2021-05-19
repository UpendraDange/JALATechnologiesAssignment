"""
Write a program to find the number is prime or not
"""

num = int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    if num%i == 0:
        count+=1
if count == 2:
    print("number is prime")
else:
    print("number is not prime")