from aula28_C_Employee import Employee;
employee1 = Employee("Mike Lima",1100)
employee2 = Employee("Natali Lima",820)
employee3 = Employee("Otavio Lima",150)

employee1.showEmployee();
employee2.showEmployee();
employee3.showEmployee();


employee1.showCount();

print("\n\nEmployee. __name__: ",Employee.__name__);
print("\n\nEmployee. __modulo__: ",Employee.__module__);
print("\n\nEmployee. __bases__: ",Employee.__bases__);
print("\n\nEmployee. __dict__: ",Employee.__dict__);
print("\n\nEmployee. __doc__: ",Employee.__doc__);