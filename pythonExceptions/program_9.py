"""
 Write a program to generate ArrayIndexOutOfBoundException
"""



def pyException():
    try:
        pyList = [10,20,40,30]
        print(pyList[2])
        print(pyList[6])
    except IndexError as ie:
        print("Error:",ie)
if __name__ == "__main__":
    pyException()
