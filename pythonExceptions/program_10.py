"""
 Write a program to generate ClassNotFoundException

"""


try:
    class pyException():
        def welcome(self):
            print("Welcome to Python programming")

    obj = PyException()
except NameError as ne:
    print(ne)