class LamportClock ():
    def __init__(self):
        self.clock = 0

    def increment(self):
        self.clock += 1

    def update(self, time):
        self.clock = max(self.clock, time) + 1

    def get_time(self): # send time
        return self.clock

    def set_time(self, time): # receive time
        self.clock = time

    def __str__(self):
        return str(self.clock)
    