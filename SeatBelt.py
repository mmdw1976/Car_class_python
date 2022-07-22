class SeatBelt:
    def __init__(self):
        self.seat_belts = {
            'front_left': False,
            'front_right': False,
            'back_left': False,
            'back_right': False
        }

    def use_seat_belt(self, **kwargs):
        for k, v in kwargs.items():
            self.seat_belts[k] = v

    def show_seat_belt_info(self):
        print(f"Seatbelt info")
        for k, v in self.seat_belts.items():
            print(f"{k}: {v}")




