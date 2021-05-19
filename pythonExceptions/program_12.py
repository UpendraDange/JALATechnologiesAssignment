"""
Write a program to generate IOException
"""
def demoException():
    try:
        fi = open("MyFile", mode='w', encoding = 'utf-8')
        print(fi.read())
    except IOError as ioe:
        print("Error:",ioe)


demoException()