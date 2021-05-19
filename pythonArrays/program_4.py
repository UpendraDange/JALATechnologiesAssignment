"""
Write a function to test if array contain a specific value
"""

def test(pyList):
    val=int(input("Enter value you want to check in list:"))
    if val in pyList:
        print("Value present in list")
    else:
        print("Value not present in list")

if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    test(pyList)