"""
. Write a function to find the missing number of sorted array of 1 to 100
"""
def pyMissingNo(pyList):
    pyList.sort()
    count=len(pyList)
    total=(pyList[-1]*(pyList[-1]+1))/2
    sumList=sum(pyList)
    temp = total - sumList
    resList = list()
    for i in range(1,pyList[-1]):
        if i not in pyList:
            resList.append(i)
            temp -= i
    print("the missing number of sorted List: ",resList)
if __name__ == "__main__":
    print("Enter element in list:")
    pyList = list(map(int, input().split()))
    pyMissingNo(pyList)
