"""
Write a function to remove a specific element from an array.
"""
def pyRemove(pyList):
    val = int(input("Enter value you want to remove from list:"))
    pyList.remove(val)
    return pyList


if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyList=pyRemove(pyList)
    print("List after removeng value",pyList)