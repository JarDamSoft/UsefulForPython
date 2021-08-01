class Car():
    def carStartEngine(self):
        print('Engine is working...')


car1 = Car()
car1.carStartEngine()

print()

class Employee():
    def employeeDetails(self):
        self.name = 'Damian'
        print("Name: ", self.name)
        age = 100   # It's not visible by external methods
        print("Age: ", age)

    def printEmplyeeDetails(self):
        print("Other method")
        print("Name: ", self.name)
        print("Age: ", age)


employee = Employee()
employee.employeeDetails()
employee.name = "Patryk"

print()

employee.printEmplyeeDetails()

