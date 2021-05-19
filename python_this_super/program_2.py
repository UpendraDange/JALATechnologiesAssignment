"""
2. Print the fields/instance members of the parent class using super
"""

class pyBase():
    def show(self):
        self.num = 30
        print("Value of Number:",self.num)

class pyDerived(pyBase):
    def show(self):
        super().show()

obj = pyDerived()
obj.show()
