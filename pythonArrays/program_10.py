"""
Write a functioin to find the duplicate values of an array.
"""

def pyDuplicate(pyList):
    pySet=set()
    for i in pyList:
        pycount=pyList.count(i)
        if pycount >=2:
            pySet.add(i)
    print("Duplicate Values in List",pySet)


if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyDuplicate(pyList)