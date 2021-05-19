"""
Create a sub class for an abstract class. Create an object in the child class for the
abstract class and access the non-abstract methods
"""

from abc import ABC,abstractmethod
class rectangle(ABC):
    def cal(self, l, w):
        return(l*w)

class pyShow(rectangle):
    def show(self):
        self.l = int(input("Enter length:"))
        self.w = int(input("Enter width:"))
        rect = rectangle()
        self.area = rect.cal(self.l,self.w)
        print("Area of rectangle:",self.area)



if __name__ == "__main__":
    sh = pyShow()
    sh.show()
    sh.res = sh.cal(12,6)
    print("length = 12 and width = 6 \nArea of rectangle:",sh.res)