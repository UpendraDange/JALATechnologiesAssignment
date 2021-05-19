"""
 Write a program with finally block
"""
def demoException():
    try:
        fi = open("MyFile", mode='r', encoding = 'utf-8')
        print(fi.read(10))
    finally:
        fi.close()
        print("This Block Always get Executed")

demoException()
