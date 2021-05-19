"""
 Call static methods and instance methods in main method.
"""

class pyShow():
    @staticmethod
    def staticMethod():
        print("This is static method.")

    def InstMethod(self):
        print("This is instance method")

if __name__ == "__main__":
    II = pyShow()
    II.InstMethod()
    pyShow.staticMethod()