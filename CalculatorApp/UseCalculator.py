from Calculator import basicOperation
from ScientificCalculator import SciOperation

class choice():
    def call(self):
        print("Select Operation\n1. Basic Calculator  \n2. Scientific Calculator \n3. n for  Exit")
        num = input("Enter choice (1\\2\\n):")

        while num != "n":
            if num == "1":
                BO2 = basicOperation()
                BO2.basCalculation()
            elif num == "2":
                BO3 = SciOperation()
                BO3.SciCalculation()


            elif num!="1" and num!="2":
                print("please enter valid input")

            num = input("Enter choice (1\\2\\n):")

if __name__ == "__main__":
    ch = choice()
    ch.call()

