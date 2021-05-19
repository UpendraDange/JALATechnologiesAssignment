"""
. Create a class with PROTECTED fields and methods. Access these fields and methods
from any other class in the same package.
Also, Access the PROTECTED fields and methods from child class located in a different
package
Access the PROTECTED fields and methods from any class in different package
"""
import subProgram_3
from pythonHelp import accessModifiers_3
class pyOperation():
    def pyAdd(self,ex):
        self.ex = ex
        self.ex._pyInit()
        num2 = 30
        print("Addition:", num2+ self.ex._val)

    def pyMul(self, objAM):
        self.objAM = objAM
        self.objAM._pyAM()
        num3 = 23
        print("Multiplication", num3*self.objAM._num7)




if __name__ == "__main__":
    ex = subProgram_3.example()
    op = pyOperation( )
    op.pyAdd(ex)

    objAM = accessModifiers_3.subAM()
    op.pyMul(objAM)