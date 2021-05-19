"""
Write a method to verify if the array contains two
specific elements(12,23)
"""

def pyContainer(pyList):
    if 12 in pyList and 23 in pyList:
        print("List contain the element 12 and 23")
    else:
        print("List not contain both the element")

if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyContainer(pyList)