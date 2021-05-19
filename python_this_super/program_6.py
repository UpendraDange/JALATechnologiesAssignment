"""
6. Use this() and super() in methods not in constructors
"""

class pyParent():
    def assign(self):
        self.name = "Suresh"
        self.age = 40

    def show(self):
        print("Details of Father")
        print("Name:",self.name)
        print("Age:",self.age)

class pyChild(pyParent):
    def assign(self):
        self.name = "Suresh"
        self.age = 15
    def show(self):
        super().assign()
        super().show()
        self.assign()
        print("Details of Child")
        print("Name:", self.name)
        print("Age:", self.age)

obj = pyChild()
obj.show()