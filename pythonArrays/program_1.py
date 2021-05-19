"""
Note : Python does not have built-in support for Arrays, but Python Lists can be used instead.

1. Write a function to add integer values of an array

"""

def addElements(pyList,val):
    pyList.append(val)
    return pyList

if __name__ == "__main__":
    pylist=list()
    num=int(input("how many element you want to add:"))
    for i in range(num):
        val=int(input("Enter element to add in list: "))
        reslist=addElements(pylist,val)
    print("List after inserting elements:",reslist)