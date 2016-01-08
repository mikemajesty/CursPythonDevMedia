class PrivateTest:
    def __init__(self):
        self.publicData = "public";
        self.__privateData = "private";
class Retangle:
    resultAre = 0;
    def __init__(self,sideA = 1,sideB = 1):
        self.calcArea(sideA,sideB);

    def calcArea(self,sideA,sideB):
        self.resultAre = sideA * sideB;

    def __del__(self):      
       class_name = self.__class__.__name__
       print(class_name);