class Pet:
    def __init__(self, name,specie):
        self.name = name
        self.specie = specie
        
    def getName(self):
        return self.name
    def getSpecie(self):
        return self.specie;
    def __str__(self):
        return "%s e uma %s " % (self.name,self.specie);

myPet1 = Pet("Nina","Dog");
myPet2 = Pet("Mia","Cat");
myPet3 = Pet("Marley","fish");

print(myPet1);
print(myPet2);
print(myPet3);

print("O nome do animal 1 : ",str(myPet1.getName()));
print("A especie do animal 3 : ",str(myPet3.getSpecie()));
print("A especie do animal 2 : ",str(myPet2.getSpecie()));
