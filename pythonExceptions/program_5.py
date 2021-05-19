"""
5. Write a program to throw exception with your own message
"""


def pyException():
    try:
        val1 = int(input("Enter first number:"))
        val2 = int(input("Enter second number:"))
        res = val1 / val2
        print(res)
    except ZeroDivisionError:
        print("Number can not divide by zero")


if __name__ == "__main__":
    pyException()
