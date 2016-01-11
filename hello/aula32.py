class A():
    def __init__(self):
        print("Init A");
        super().__init__();
class B():
    def __init__(self):
        print("Init B");
        super().__init__()
class C(A,B):
    def __init__(self):
        print("Init C");
        super().__init__()

C();
       
class Animal:
    def __init__(self, name):
        self.name =name;
class Cat(Animal):
    def Talk(self):
        return "Miauuuuu";
class Dog(Animal):
    def Talk(self):
        return "Au au au au";

Dog("Marley").Talk();
Cat("Mia").Talk();
animals = [Cat("Michi"),Dog("Dilma"),Dog("Luna")];
for animal in animals:
    print(animal.name + ": "+animal.Talk());