"""
Write a function to reverse an array of integer values
"""

def pyReverse(pyList):
    pyList.reverse()
    return pyList


if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyList=pyReverse(pyList)
    print("List after revering",pyList)