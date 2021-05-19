"""
Write a program to remove the duplicate elements and
return the new array
"""

def pyDuplicate(pyList):
    pySet=set(pyList)
    pyList=list(pySet)
    return pyList

if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyList=pyDuplicate(pyList)
    print("List after removing duplicate value:",pyList)
