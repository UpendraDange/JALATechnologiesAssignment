"""
 Apply private, public, protected and default access modifiers to the constructor

 Note : default access modifier not present in python
"""

class Car():
    def __init__(self):
        self.name = "Ferrari"
        self._color = "Red"
        self.__Model = "Ferrari F8"

    def show(self):
        print("Car Name:", self.name)
        print("Car color:", self._color)
        print("Car Model:", self._Car__Model)

cc = Car()
cc.show()