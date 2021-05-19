"""
Write a function to find the minimum and maximum value of an array
"""
def pyMinMax(pyList):
   print("Minimum value of an list:",min(pyList))
   print("Maximum value of an list:",max(pyList))


if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyMinMax(pyList)
