"""
Write a program to find the common values between two arrays
"""

def pyCommon(pyList1,pyList2):
    pySet1=set(pyList1)
    pySet2=set(pyList2)
    if pySet1.intersection(pySet2):
        print("Common values between two List:",pySet1.intersection(pySet2))
    else:
        print("There is no common element in two list")

if __name__ == "__main__":
    print("Enter element in list one:")
    pyList1 = list(map(int, input().split()))
    print("Enter element in list two:")
    pyList2 = list(map(int, input().split()))
    pyCommon(pyList1,pyList2)