# This python file is created to practice super and sub-classes
# Also to learn how private, protected, and public works in python

# Class vehicle
# A super class for all vehicles
class Vehicle(object):
    #Constructor
    def __init__(self, brand, creationDate, numSeats, vehicleType):
        self._brand = brand
        self._creationDate = creationDate
        self._numSeats = numSeats
        self._vehicleType = vehicleType

    #Getters
    def _getBrand(self):
        return self._brand

    def _getCreationDate(self):
        return self._creationDate

    def _getNumSeats(self):
        return self._numSeats

    def _getVehicleType(self):
        return self._vehicleType

    #Setters
    def _setBrand(self, brand):
        self._brand = brand

    def _setCreationDate(self, creationDate):
        self._creationDate = creationDate

    def _setNumSeats(self, numSeats):
        self._numSeats = numSeats

    def _setVehicleType(self, vehicleType):
        self._vehicleType = vehicleType

# Class car
# A subclass of vehicle
class Car(Vehicle):
    #Contructor
    def __init__(self, brand, creationDate, numSeats):
        super().__init__(brand, creationDate, numSeats, 'car')

    #Getters
    def getBrand(self):
        return Vehicle._getBrand(self)

    def getCreationDate(self):
        return Vehicle._getCreationDate(self)

    def getNumSeats(self):
        return Vehicle._getNumSeats(self)

    def getVehicleType(self):
        return Vehicle._getVehicleType(self)

    #Setters
    def setBrand(self, brand):
        Vehicle._setBrand(self, brand)

    def setCreationDate(self, creationDate):
        Vehicle._setCreationDate(self, creationDate)

    def setNumSeats(self, numSeats):
        Vehicle._setNumSeats(self, numSeats)

    def setVehicleType(self, vehicleType):
        Vehicle._setVehicleType(self, vehicleType)

#Main function
def main():
    c = Car('Toyota', 1998, 6)
    print("Car 1")
    print(c.getBrand());
    print(c.getCreationDate());
    print(c.getNumSeats());
    print(c.getVehicleType() + "\n");

    print("Car 1 edit")
    c.setBrand('Honda')
    c.setCreationDate(1996)
    c.setNumSeats(4)
    
    print(c.getBrand());
    print(c.getCreationDate());
    print(c.getNumSeats());
    print(c.getVehicleType() + "\n");

#run program
main()
