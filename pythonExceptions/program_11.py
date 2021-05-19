"""
11. Write a program to generate FileNotFoundException
"""
try:
    def demoException():
        fi = open("MyFile1", mode='r', encoding = 'utf-8')
        print(fi.read(10))
        fi.close()

    demoException()
except FileNotFoundError as fnf:
        print(fnf)



