"""
Call static methods in instance methods.
"""
class pyAdd():
    @staticmethod
    def show(res):
        print("Addtion of two number:",res)
    def add(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        res=self.num1+self.num2
        pyAdd.show(res)
        
num1=int(input("Enter a value of num1:"))
num2=int(input("Enter a value of num2:"))
obj = pyAdd()
obj.add(num1,num2)
