class Employee:
    employeeCount = 0
    def __init__(self, name,salario):
        self.name = name
        self.salario = salario
        Employee.employeeCount +=1
        

    def showEmployee(self):
        print("\nNome: ",self.name," salario: ",self.salario)


    def showCount(self):
        print("\n A quantidade de employees e %d" % Employee.employeeCount);


