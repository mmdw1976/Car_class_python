from datetime import date

# import classes from other files
from StartEngine import StartEngine
from ElectricWindow import ElectricWindow
from Person import Person
from SeatBelt import SeatBelt


# order of class imports are important
# in start engine the sequence is SeatBelt => Person
class Car(StartEngine, SeatBelt, Person):
    def __init__(self, brand, model, production_year, seats):
        StartEngine.__init__(self)
        ElectricWindow.__init__(self)  # get attributes from ElectricWindow class
        Person.__init__(self)  # get attributes from Person class
        SeatBelt.__init__(self)  # get attributes from SeatBelt class

        self.brand = brand
        self.model = model
        self.production_year = production_year
        self.seats = seats

    def car_age(self):
        """Calculate age and show it to user"""
        age_car = date.today().year - self.production_year
        return f"The {self.brand} {self.model} production year is {self.production_year}, and is {age_car} years old."


car1 = Car('opel', 'astra', 2018, 5)
car1.use_seat(front_left=True)
car1.use_seat_belt(front_left=True)

car1.start_engine()




