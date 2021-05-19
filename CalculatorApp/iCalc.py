from abc import ABC,abstractmethod
class iCalc(ABC):
    @abstractmethod
    def doCalculation(self):
        pass

    @abstractmethod
    def getResult(self):
        pass
