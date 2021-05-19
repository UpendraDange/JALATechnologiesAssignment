"""
Write a function to get the difference of largest and smallest value.
"""
def pyDifference(pyList):
    print("The difference of largest and smallest value:",max(pyList)-min(pyList))


if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyDifference(pyList)
