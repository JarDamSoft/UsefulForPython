class Employee:
    def employeeDetails(self):  # Instance method
        self.name = "Damian"

    @staticmethod   # Decorator
    def welcomeMessage():   # Static method
        print("Welcome!")


employee = Employee()
employee.employeeDetails()  # Invoking method 
print(employee.name)
employee.welcomeMessage()
