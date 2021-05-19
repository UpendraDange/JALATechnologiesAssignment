"""
write a method to remove duplicate elements from an array
"""
def pyDuplicate(pyList):
    pySet=set(pyList)
    pyList=list(pySet)
    print("List after removing duplicate value:",pyList)

if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyDuplicate(pyList)

