"""
Create a class with PUBLIC fields and methods.
Access the public methods and fields from any class in the same package or different
package.
"""
from  subProgram_4 import help
class pySum():
    def printStr(self,pp):
        str2 = "Python "
        pp.pyHelp()
        print(str2+pp.pyStr)

if __name__ == "__main__":
    pp = help()
    SS = pySum()
    SS.printStr(pp)
