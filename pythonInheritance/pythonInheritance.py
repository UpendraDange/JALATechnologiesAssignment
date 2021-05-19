"""
A, B and C are classes

A is a super class. B is a sub class of A. C is a sub class of B.

Create three methods in each class, 2 methods are specific to each class and third
method (override method) should be in all three Classes A, B and C

Create a class with main method. Create an object for each class A, B and C in main
method and call every method of each class using its own object/instance.

Call an overridden method with super class reference to B and C class’s objects

Runtime Polymorphism with Data Members/Instance variables, Repeat the above
process only for data members
"""
class A():
    def methodA1(self):
        print("I am in methodA1.")
    def methodA2(self):
        print("I am in methodA2.")
    def pyAdd(self,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        print("Addition of Numbers:",a+b+c)


class B(A):
    def methodB1(self):
        print("I am in methodB1.")

    def methodB2(self):
        print("I am in methodB2.")

    def pyAdd(self,a=0,b=0,c=0):
        self.a=a
        self.b=b
        self.c=c
        print("Addition of Numbers:",self.a+self.b+self.c)
        super().pyAdd(self.a,b=8)


class C(B):
    def methodC1(self):
        print("I am in methodC1")

    def methodC2(self):
        print("I am in methodC2")

    def pyAdd(self,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        print("Addition fo numbers:",self.a+self.b+self.c)
        super().pyAdd(self.a,self.b,c=12)


if __name__ == "__main__":
    objA = A()
    objA.methodA1()
    objA.methodA2()
    objA.pyAdd(4, 7, 8)

    objB = B()
    objB.methodB1()
    objB.methodB2()
    objB.pyAdd(3, 10, 9)

    objC = C()
    objC.methodC1()
    objC.methodC2()
    objC.pyAdd(2, 6, 9)
