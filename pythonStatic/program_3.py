"""
Print static variables in Instance methods.
"""

class Area():
    PI=3.14
    def cal(self,rad):
        self.rad=rad
        res = Area.PI * (rad**2)
        print("Value of PI",Area.PI)
        print("Area of circle:",res)

rad=int(input("Enter radius of circle:"))
obj=Area()
obj.cal(rad)