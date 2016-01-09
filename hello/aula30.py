class Car:
    def __init__(self, automaker,model):
        self.automaker = automaker
        self.model = model

    def __getattr__(self,name):
        return "Nao existe ";
    def __setattr__(self, name,value):
        if name == "automaker":
            if value == "GM":
                self.__dict__["automaker"] = "Chevolet"
            else:
                self.__dict__["automaker"] = value
        else:
            self.__dict__[name] = value;
    def __delattr__(self,name):
        print("Attr: ",name, " foi deletado")
        
myCar = Car("Ford","Focus");

print(myCar.automaker," - ",myCar.model);
print(myCar.Year);

myCar2 = Car("GM","Celta");
print(myCar2.automaker," - ",myCar2.model);

del myCar.model;

class Lenght:
    __metric = {"mm": 0.0001,"cm": 0.01,"m":1,"km":1000};

    def __init__(self,value,unit="m"):
                 self.value = value;
                 self.unit = unit;
    def convertToMeters(self):
        return self.value * Lenght.__metric[self.unit];
    def __add__(self,other):
        result = self.convertToMeters() + other.convertToMeters();
        return Lenght(result/Lenght.__metric[self.unit],self.unit);
    def __repr__(self):
        return "lengh("+str(self.value) + "," +self.unit + ")";
cl = Lenght(3,"km") + Lenght(200);
print(repr(cl));