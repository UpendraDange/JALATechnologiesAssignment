"""
Write a function to copy an array to another array.
"""

def pyCopy(pyList):
    copyList=pyList.copy()
    return copyList


if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    copyList=pyCopy(pyList)
    print("Element of the copied list",copyList)