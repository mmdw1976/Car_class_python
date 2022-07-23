from datetime import date

# import classes from other files
from ElectricWindow import ElectricWindow
from StartEngine import StartEngine
from Person import Person
from SeatBelt import SeatBelt


# order of class imports are important
# in StartEngine the sequence is SeatBelt => Person

# MRO explanation
# StartEngine class inherit SeatBelt and Person in that order!
# we must obtain the order that is specified in the parent class that will execute the function
# Order is therefore SeatBelt => SeatBelt => Person
# ElectricWindow is not depending on other classes therefore placement is not that important
class Car(ElectricWindow, StartEngine, SeatBelt, Person):
    def __init__(self, brand, model, production_year, seats):
        ElectricWindow.__init__(self)  # get attributes from ElectricWindow class
        StartEngine.__init__(self)
        SeatBelt.__init__(self)  # get attributes from SeatBelt class
        Person.__init__(self)  # get attributes from Person class

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


car1.move_window('front_left', 40)

print(Car.__mro__)




