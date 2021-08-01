class Microsoft:
    manufacturer = "Microsoft Inc."
    website = "www.microsoft.com"

    def contactDetails(self):
        print("For contact, please check our website: {}" .format(self.website))


class Windows(Microsoft):
    def __init__(self):
        self.yearOfManufacture = '1995'

    def manufactureDetails(self):
        print("Year of manufacture is {} and manufacturer is {}" .format(self.yearOfManufacture, self.manufacturer))


windows = Windows()
windows.manufactureDetails()
