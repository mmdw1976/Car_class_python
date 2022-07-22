class Person:
    def __init__(self):
        self.persons = {
            'front_left': False,
            'front_right': False,
            'back_left': False,
            'back_right': False
        }

    def use_seat(self, **kwargs):
        """Check used seats in car"""
        for k, v in kwargs.items():
            self.persons[k] = v

    def show_person_info(self):
        for k, v in self.persons.items():
            print(f"{k}: {v}")

