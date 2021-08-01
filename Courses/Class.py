class Employee:
    numberOfWorkingHours = 40


employeeOne = Employee()
employeeTwo = Employee()

print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

# Changing the value of class attribute
Employee.numberOfWorkingHours = 50

print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

# Creating instance attribute
employeeOne.name = "Damian"
employeeTwo.name = "Patryk"

print(employeeOne.name)
print(employeeTwo.name)

# Changing value of class attribute for specific object
employeeOne.numberOfWorkingHours = 40

print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)
