"""
Create a class with PRIVATE fields, private method and a main method. Print the fields
in main method. Call the private method in main method.
Create a sub class and try to access the private fields and methods from sub class.

"""
class access():
    def __assign(self):
        self.__val=10

class subAccess(access):
    def subMethod(self,obj):
        self.obj = obj
        self.obj._access__assign()
        print(self.obj._access__val)


if __name__ == "__main__":
    obj = access()
    obj._access__assign()
    print(obj._access__val)

    subObj = subAccess()
    subObj.subMethod(obj)
