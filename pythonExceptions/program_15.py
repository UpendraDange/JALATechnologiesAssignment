"""
15. Write a program to generate NullPointerException
"""


try:
    pylist = None
    print(pylist[6])

except TypeError as te:
    print(te)
