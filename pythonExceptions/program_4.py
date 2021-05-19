"""
Write a program with multiple catch blocks.
"""

def pyException():
    try:
        val1 = int(input("Enter first number:"))
        val2 = int(input("Enter second number:"))
        res = val1/val2
        print(res)
    except ZeroDivisionError as zd:
        print(zd)
    except ValueError as ve:
       print(ve)


if __name__ == "__main__":
    pyException()
