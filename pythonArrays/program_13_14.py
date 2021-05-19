"""
Write a method to find the second largest number in an array.
"""
def pySecondMax(pyList):
    pySet=set(pyList)
    pyMax=max(pySet)
    pySet.remove(pyMax)
    print("Second largest number in an list:",max(pySet))


if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pySecondMax(pyList)

