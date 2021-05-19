"""
Try to call the constructor multiple times with the same object.

ans : Every time you call constructor with same object.
        The new object created with the same name.
"""

class pyShow():
    def __init__(self):
        self.i = 0
        self.i += 1
        print("I am in the constructor.",self.i)

obj = pyShow()
obj = pyShow()
obj = pyShow()

