"""
4. Call argument constructor of current class using this()
"""

class Demo:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print("Addition of two number:",self.num1+self.num2)
    def show(self):
        self.__init__(10,50)

DD = Demo(20,10)
DD.show()