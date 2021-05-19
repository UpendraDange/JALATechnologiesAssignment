"""
 Write a class with 2 static variables, 2 Instance variables, 2 static methods, 2 instance
 methods and a main method.
"""

class pySatic():
    loc = "Hyderabad"
    cName = "Google"
    @staticmethod
    def cDtails():
        print("Company name:",pySatic.cName)
        print("Company location:",pySatic.loc)
    @staticmethod
    def extra():
        print("Welcome the Employee Details")


    def empData(self,name,eid):
        self.name = name
        self.eid = eid

    def empShow(self):
        pySatic.extra()
        print("Employee id:",self.eid)
        print("Employee name:",self.name)
        pySatic.cDtails()


if __name__ == "__main__":
    EE = pySatic()
    EE.empData("Ramesh",101)
    EE.empShow()

    EE2 = pySatic()
    EE2.empData("Samesh",102)
    EE2.empShow()

