from SeatBelt import SeatBelt
from Person import Person


class StartEngine(SeatBelt, Person):
    def __init__(self):
        SeatBelt.__init__(self)
        Person.__init__(self)


    def start_engine(self):
        """
                1. Check persons in car
                2. Check used seat belts
                3. compare if seat and seat_belt are same
                4. if True start car
                5. if False give Warning
                """
        check_person = {}
        check_seat_belt = {}
        person_count = 0
        # check persons in car
        for k, v in self.persons.items():
            # if person is in car store in check person
            if self.persons[k]:
                check_person[k] = v
            else:
                person_count += 1
        # check for used seat belts in car
        for k, v in self.seat_belts.items():
            # if seat belt is used and person is in that seat
            # than store in check_seat_belt
            if self.seat_belts[k] and self.persons[k]:
                check_seat_belt[k] = v
        if person_count == 4:
            print(f"No persons in the car not allowed to start!")
        else:
            # check if check_person and check_seat_belt are same
            # if so that means that the passengers also have used seat belt
            if check_person == check_seat_belt:
                print("Starting the car!")
                print("Have a nice trip.")
            else:
                print("Warning all passengers have to use the seat belt!")






