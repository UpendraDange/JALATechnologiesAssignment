"""
13. Write a program to generate NoSuchFieldException

"""


def sample():
    try:
        val1 = int(input("Enter first number:"))
        val2 = int(input("Enter second number:"))
        res = val1+val2
        print("sum:",Res)
    except NameError as ne:
        print(ne)

if __name__ == "__main__":
    sample()