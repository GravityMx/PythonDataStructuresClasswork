
import math

class ParkedCar:

    def __init__(self, make="Ford", model="ModelT", color="Black", licenseNum="abc1234", timeParked=60):
        self.make = make
        self.model = model
        self.color = color
        self.licenseNum = licenseNum
        self._timeParked = timeParked

    @property
    def timeParked(self):
        return self._timeParked

    @timeParked.setter
    def timeParked(self, value):
        if (value < self._timeParked):
            print("You can't go back in time.")
        else:
            self._timeParked = value

    def __str__(self):
        return f"Make: {self.make} - Model: {self.model} - Color: {self.color} - license Number: {self.licenseNum} - Time Parked: {self._timeParked}"




class ParkingMeter:

    def __init__(self, timePaid=60):
        self._timePaid = timePaid

    @property
    def timePaid(self):
        return self._timePaid

    @timePaid.setter
    def timePaid(self, value):
        self._timePaid = value;

    def __str__(self):
        return f"(This meter has paid for {self.timePaid} minutes)"


class ParkingTicket:
    def __init__(self, car=None, officerName="No Name", officerBadgeNumber=000000, illegalMinutes=0):
        self.car = car
        self.officerName = officerName
        self.officerBadgeNumber = officerBadgeNumber
        self.illegalMinutes = illegalMinutes
        self.fine = (25 + (math.floor(self.illegalMinutes / 60) * 10))

    def easyPrint(self, printThis):
        return str(printThis).center(86, "-") + "\n"

    def __str__(self):
        return f"{self.easyPrint('PARKING TICKET')}{self.easyPrint('-')}{self.easyPrint(self.car)}{self.easyPrint('-')}{self.easyPrint(f'Officer Name: {self.officerName} -- Officer Badge Number:  {self.officerBadgeNumber}')}{self.easyPrint('-')}{self.easyPrint(f'Illegal Parking Minutes: {self.illegalMinutes} ---- Fine: ${self.fine}')}{self.easyPrint('-')}"



class Officer:
    def __init__(self, name="noName", badgeNum=123456):
        self.name = name
        self.badgeNum = badgeNum

    def AdministerParkingTicket(self, illegalParkedMinutes, car):
        print("(The ticket was printed)\n")
        return ParkingTicket(car, self.name, self.badgeNum, illegalParkedMinutes)

    def ExamineForParkingViolation(self, car, parkingMeter):

        line = f"(This {car.make} {car.model} is parked "

        if (car.timeParked > parkingMeter.timePaid):
            
            line += f"illegally!)"
            print(line)

            thisParkingTicket = self.AdministerParkingTicket((car.timeParked - parkingMeter.timePaid), car)

            print(thisParkingTicket)

        else:
            line += f"legally...)"
            print(line)



officer = Officer("Joe Knut", 5318008)

car1 = ParkedCar()

print(car1)

meter1 = ParkingMeter()

print(meter1)

officer.ExamineForParkingViolation(car1, meter1)

myCar = ParkedCar("Toyota", "Prius", "Red", "My 1234", 20)

myCar.timeParked = 10;

myCar.timeParked = 35;

print(myCar)

meter2 = ParkingMeter(10)

print(meter2)

officer.ExamineForParkingViolation(myCar, meter2)

homelessMansCar = ParkedCar("Chevrolet", "Sedan", "Gray", "EBT4311", 190)

meter3 = ParkingMeter(0)

officer.ExamineForParkingViolation(homelessMansCar, meter3)

car4 = ParkedCar("Toyota", "Camery", "White", "GPL0093", 90)

meter4 = ParkingMeter(120)

officer.ExamineForParkingViolation(car4, meter4)

car5 = ParkedCar("Honda", "Civic", "Silver", "HPE5621", 45)

meter5 = ParkingMeter(30)

officer.ExamineForParkingViolation(car5, meter5)


car6 = ParkedCar("Chevrolet", "Impala", "Blue", "BBL7719", 120)

meter6 = ParkingMeter(90)

officer.ExamineForParkingViolation(car6, meter6)


car7 = ParkedCar("Nissan", "Altima", "Red", "SLQ3348", 100)

meter7 = ParkingMeter(180)

officer.ExamineForParkingViolation(car7, meter7)
