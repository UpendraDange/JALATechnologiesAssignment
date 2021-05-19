"""
Write a program to print largest number among three numbers.
"""

print("Enter three element in list")
pyList=list(map(int,input().split()))

max = 0
for i in pyList:
    if i > max:
        max = i
print("Largest element:",max)