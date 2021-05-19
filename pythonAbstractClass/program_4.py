"""
 Create an instance for the child class in child class and call non-abstract methods.
"""

from abc import ABC, abstractmethod

class pyParent(ABC):
    def parentMethod(self):
        print("I am in parent method")

class pyChild(pyParent):
    def childMethod(self):
        print("I am in child method")
    def show(self):
        obj = pyChild()
        obj.parentMethod()
        obj.childMethod()

if __name__ == "__main__":
    pyC = pyChild()
    pyC.show()