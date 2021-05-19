"""
Create an instance for the child class in child class and call abstract methods
"""
import math
from abc import ABC,abstractmethod
class parentFact(ABC):
    @abstractmethod
    def cal(self):
        pass

class childFact(parentFact):
    def cal(self):
        num = int(input("Enter a number:"))
        print("Factorial of a number:",math.factorial(num))
    def create(self):
        cc = childFact()
        cc.cal()

if __name__ == "__main__":
    FF = childFact()
    FF.create()



