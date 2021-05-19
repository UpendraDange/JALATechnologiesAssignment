"""
1. Print the fields/instance members of the current class using this and without using object

Note : in python we use self keyword instead of this
"""


class demo():
    def __init__(self):
        self.val = 20

    def show(self):
        print("the value :",self.val)

DD = demo()
DD.show()