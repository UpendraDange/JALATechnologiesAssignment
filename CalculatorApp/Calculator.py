from Calculate import Calsi

class basicOperation():


    def basCalculation(self):
        print("Select Operation \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division \n5.n for Exit")
        self.operator = input("Enter Choice (1\\2\\3\\4\\n):")

        while self.operator != "n":
            if self.operator!="1" and self.operator!="2" and self.operator!="3" and self.operator!="4":
                print("Please enter valid input.")
                self.operator = input("Enter Choice (1\\2\\3\\4\\n):")

            else:
                try:
                    self.fNum = int(input("Enter first number to calculated:"))
                    self.sNum = int(input("Enter second number to calculated:"))
                    obj = Calsi()
                    obj.doCalculation(self.fNum, self.operator, self.sNum)
                    self.bgetResult(obj)
                except ValueError:
                    print("please enter only numeric value")

                self.operator = input("Enter Choice (1\\2\\3\\4\\n):")


    def bgetResult(self,obj):
        self.res=obj.getResult()
        print("the Calculation Result is:",self.res)
        self.res = None

