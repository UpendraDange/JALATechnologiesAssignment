"""
2. Write a program to write text to .txt file using OutputStream

4. Write text to a .txt file using BufferedOutputStream

6. Write a program to write text to .txt file using FileWriter
"""


try:
    with open("MyFile2",mode="w",encoding="utf-8") as MyFile :
        MyFile.write("Python is an easy to learn, powerful programming language.")
except IOError:
    print("file not exist")
finally:
    MyFile.close()
