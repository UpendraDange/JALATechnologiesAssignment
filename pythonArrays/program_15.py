"""
Write a method to find number of even number and odd numbers
in an array
"""
def pyEvenOdd(pyList):
    pyEven = 0
    pyOdd = 0
    print(pyList)
    for i in pyList:
        if i%2 == 0:
            pyEven+=1
        elif i%2 == 1:
            pyOdd+=1
    print("Even numbers in list: %d and Odd numbers in list: %d"%(pyEven,pyOdd))
if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyEvenOdd(pyList)
