import math
from iCalc import iCalc



class Calsi(iCalc):

    def doCalculation(self,iFirstNum,cOperator,iSecondNum):
        self.iFirstNum = iFirstNum
        self.cOperator = cOperator
        self.iSecondNum = iSecondNum
        if cOperator == "1":
            self.res = self.iFirstNum+self.iSecondNum
        if cOperator == "2":
            self.res = self.iFirstNum - self.iSecondNum
        if cOperator == "3":
            self.res = self.iFirstNum * self.iSecondNum
        if cOperator == "4":
            self.checkSecondNum()



    def doCalculation2(self,iFirstNum,cOperator):
        self.iFirstNum = iFirstNum
        self.cOperator = cOperator
        if cOperator == "1":
            self.res = math.sin(math.radians(float(self.iFirstNum)))
        if cOperator == "2":
            self.res = math.cos(math.radians(float(self.iFirstNum)))
        if cOperator == "3":
            self.res = math.tan(math.radians(float(self.iFirstNum)))
        if cOperator == "4":
            base = int(input("Enter base value of log:"))
            self.res = math.log(float(self.iFirstNum),base)




    def checkSecondNum(self):
        try:
            self.res = self.iFirstNum / self.iSecondNum
        except ZeroDivisionError:
            print("Number can not divide by zero")


    def getResult(self):
        return self.res