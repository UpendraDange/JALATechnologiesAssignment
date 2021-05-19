"""
Print instance variables in static methods.


"""


class pyNum():
    @staticmethod
    def show(obj):
        print("Value of num1:",obj.num1)
        print("Value of num2:",obj.num2)

    def InitNUmber(self, num1, num2):
        self.num1 = num1
        self.num2 = num2



num1 = int(input("Enter a value of num1:"))
num2 = int(input("Enter a value of num2:"))
obj = pyNum()
obj.InitNUmber(num1, num2)
pyNum.show(obj)