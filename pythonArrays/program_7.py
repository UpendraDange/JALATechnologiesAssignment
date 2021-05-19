"""
Write a function to insert an element at a specific positioin
in the array.
"""


def pyInsert(pyList):
    idx=int(input("enter the index where  element inserted:"))
    num=int(input("enter the element you want to insert:"))
    pyList.insert(idx,num)
    return pyList


if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyList=pyInsert(pyList)
    print("list after inserting element:",pyList)