"""
3. Call constructor of the current class using this()

"""

class Demo:
    num1 = 40
    def __init__(self):
        Demo.num1 +=10
        print("Value of Number:",Demo.num1)
    def show(self):
        self.__init__()

DD = Demo()
DD.show()
