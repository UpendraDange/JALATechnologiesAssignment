"""
2. Call the constructors(both default and argument constructors) of super class from a child
    class
"""

class pySuper():
    def __init__(self):
        print("I am in Parent class")

class pyChild():
    def __init__(self):
        sObj = pySuper()
        print("I am in Child class")

obj = pyChild()