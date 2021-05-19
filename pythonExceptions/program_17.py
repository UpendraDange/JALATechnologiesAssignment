"""
17. Write a program to generate StringIndexOutOfBoundsException
"""


def pyException():
    try:
        pyStr = "Python Programming"
        print(pyStr[2])
        print(pyStr[120])
    except IndexError as ie:
        print("Error:",ie)
if __name__ == "__main__":
    pyException()
