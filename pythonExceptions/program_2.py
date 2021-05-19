"""
 Handle the Arithmetic exception using try-catch block


"""

def pyException():
    try:
        val1 = int(input("Enter first number:"))
        val2 = int(input("Enter second number:"))
        res = val1/val2
        print(res)
    except ZeroDivisionError as zde:
        print(zde)

if __name__ == "__main__":
    pyException()

