class Person:
    def __init__(self,first,last):
        self.last = last
        self.first = first

    def Name(self):
        return self.first + " " + self.last
    
class Employee(Person):
    def __init__(self, first, last,employeeId):
        self.employeeId = employeeId
        super().__init__(first, last);
    def GetEmployee(self):
        return self.Name() + ", "+self.employeeId;

x = Person("Mike","Lima");
y = Employee("Nataly","Marques","9")
print(x.Name());
print(y.GetEmployee());
    
class Vehicle:
    def __init__(self,types):
        self.types = types;
    def __str__(self):
        return self.types;
class Car(Vehicle):
    def __init__(self, automaker, model,gas):
         super().__init__("car")
         self.automaker = automaker;
         self.model = model;
         self.gas = gas;
    def __str__(self):
        return super().__str__() + ", "+self.automaker +", "+self.model +", "+self.gas;
class Truck(Vehicle):
      def __init__(self, automaker, model):
            super().__init__("Truck")
            self.automaker = automaker;
            self.model = model;
            self.gas = "gas";
      def __str__(self):
         return super().__str__()+ ", "+self.automaker +", "+self.model +", "+self.gas;
myCar = Car("Fiat","Uno","Gas");
myTruck = Truck("Volvo","D1000");
print(myCar);
print(myTruck);