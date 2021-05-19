"""
Write a program to print the odd and even numbers
"""

pyList=[12,45,66,32,77,84,95,45,6]
evenList=list()
oddList=list()
for i in pyList:
    if i%2 == 0:
        evenList.append(i)
    elif i%2 != 0:
        oddList.append(i)
print("Even number of list",evenList)
print("Odd number of list",oddList)
