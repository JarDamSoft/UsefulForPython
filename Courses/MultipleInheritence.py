class OperationSystem:
    multitasking = True
    name = "Windows 95"


class Microsoft:
    manufacturer = "Microsoft Inc."
    website = "www.microsoft.com"
    name = "Windows XP"

    def contactDetails(self):
        print("For contact, please check our website: {}" .format(self.website))


class Windows(Microsoft, OperationSystem):
    def __init__(self):
        self.yearOfManufacture = '1995'
        if self.multitasking is True:
            print("This is a multitasking system")

    def manufactureDetails(self):
        print("Year of manufacture is {} and manufacturer is {}" .format(self.yearOfManufacture, self.manufacturer))
        print("Name: {}".format(self.name))


windows = Windows()
windows.manufactureDetails()
