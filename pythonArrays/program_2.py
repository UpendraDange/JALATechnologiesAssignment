"""
Write a function to calculate the average value of an array of integers

"""

def pyAvg(pyList):
    addTotal = sum(pyList)
    print("Average of a list:",addTotal/len(pyList))

if __name__ == "__main__":
    print("Enter element in list:")
    pyList=list(map(int,input().split()))
    pyAvg(pyList)



