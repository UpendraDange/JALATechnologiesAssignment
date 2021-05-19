"""
1. Write a program to read text from .txt file using InputStream

3. Read text from a .txt file using BufferedInputStream

5. Write a program to read text from .txt file using FileReader
"""

try:
    with open("MyFile",mode="r",encoding="utf-8") as MyFile :
        print(MyFile.read())
except IOError:
    print("file not exist")
finally:
    MyFile.close()
