class Employee:
    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)


employee1 = Employee("Damian")
employee2 = Employee("Anna")

employee1.displayEmployeeDetails()
employee2.displayEmployeeDetails()
