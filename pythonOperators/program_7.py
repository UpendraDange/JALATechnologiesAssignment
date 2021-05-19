"""
Print the smaller and larger number.
"""

pyArr=[11,55,33,8,66,44,2]
small = pyArr[0]
large = pyArr[0]
for i in pyArr:
    if i>large:
        large = i
    elif i<small:
        small = i
print("smaller value in list:",small)
print("larger value in list:",large)