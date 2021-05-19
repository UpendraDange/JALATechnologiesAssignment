"""
 Write a program to generate Arithmetic Exception

"""

def pyException():
    try:
        val1 = int(input("Enter first number:"))
        val2 = int(input("Enter second number:"))
        res = val1/val2
        print(res)
    except ZeroDivisionError:
        print("You should not divide a number by zero.")

if __name__ == "__main__":
    pyException()

