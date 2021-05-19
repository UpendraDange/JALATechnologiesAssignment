"""
 Create an abstract class with abstract and non-abstract methods.
"""

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    def live(self):
        print("I live on earth")

class Human(Animal):
    def move(self):
        print("I can walk and run")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")

if __name__ == "__main__":
    HH = Human()
    HH.move()
    HH.live()

    DD = Dog()
    DD.move()
    DD.live()

    LL = Lion()
    LL.move()
    LL.live()