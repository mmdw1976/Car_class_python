class ElectricWindow:
    def __init__(self):
        self.windows = {
            'front_left': 100,
            'front_right': 100,
            'back_left': 100,
            'back_right': 100
        }

    def move_window(self, position, open=0, close=0):
        if (self.windows[position] + close) <= 100 and (self.windows[position] - open) >= 0:
            if open > 0:
                self.windows[position] = self.windows[position] - open
                # show message over window position
                print(f"{position} window is set {100 - self.windows[position]}% open")
            elif close > 0:
                self.windows[position] = self.windows[position] + close
                # show message over window position
                print(f"{position} window is set {self.windows[position]}% closed")
        # stop motor if window is full open or close
        elif (self.windows[position] + close) > 100:
            self.windows[position] = 100
            print(f"Window {position} is fully clossed motor stopped at {self.windows[position]}%")
        elif (self.windows[position] - open) < 0:
            self.windows[position] = 0
            print(f"Window {position} is fully opened motor stopped at {self.windows[position]}%")

    def close_all_windows(self):
        """Close all window when activated"""
        for k, v in self.windows.items():
            self.windows[k] = 100

    def display_info_windows(self):
        """Give user information about current position of the windows"""
        for k, v in self.windows.items():
            print(f"{k}: {v}")