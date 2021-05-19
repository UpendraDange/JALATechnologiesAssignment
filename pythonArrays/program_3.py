"""
Write a program to find the index of an array element.
"""

def findIndex(pyList):
    val=int(input("Enter element you want to find:"))
    print("Index of an element in list:",pyList.index(val))

if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    findIndex(pyList)
