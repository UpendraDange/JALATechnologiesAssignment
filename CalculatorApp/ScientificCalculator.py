import math
from Calculate import Calsi


class SciOperation(Calsi):
    def SciCalculation(self):
        print("Select Operation\n1. sine \n2. cosine \n3. tangent \n4. log \n5. n for exit")
        self.operator = input("Enter Choice (1\\2\\3\\4\\n):")

        while self.operator != "n":
            if self.operator!="1" and self.operator!="2" and self.operator!="3" and self.operator!="4":
                print("Please enter valid input.")
                self.operator = input("Enter Choice (1\\2\\3\\4\\n):")

            else:
                try:
                    self.fNum = int(input("Enter first number to calculated:"))
                    self.doCalculation2(self.fNum, self.operator)
                    self.sgetResult()

                except ValueError:
                    print("please enter only numeric value")



                self.operator = input("Enter Choice (1\\2\\3\\4\\n):")

    def sgetResult(self):
        self.res=self.getResult()
        print("the Calculation Result is:",self.res)
        self.res = None