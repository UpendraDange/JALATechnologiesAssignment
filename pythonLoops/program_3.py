"""
Program to equal operator and not equal operators
"""
pyList = [10,3,6,7,2,4,6,2]
evenSum = 0
oddSum = 0
for i in pyList:
    if i % 2 == 0:
        evenSum += i
    elif i % 2 != 0:
        oddSum += i

print("Sum of even number from list:",evenSum)
print("Sum of odd number from list:",oddSum)