"""
5. Call constructor of the parent class using super()
"""


class pyBase():
    def __init__(self,val):
        self.val = val
        self.num = 8
        print("Multiplication of Number:",self.num*self.val)

class pyDerived(pyBase):
    def __init__(self):
        super().__init__(20)

obj = pyDerived()
