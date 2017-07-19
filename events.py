class Event():

    events = []

    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @classmethod
    def sort_events(cls):
        cls.events.sort(key=lambda event: event.date)

    @classmethod
    def add_event(cls, event):
        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        return cls.events


class Checkpoint(Event):

    def __init__(self, date):
        super().__init__(date)
        self.add_event(self)

    def __str__(self):
        return "{} checkpoint".format(self.date)


class PrivateMentoring(Event):

    def __init__(self, date):
        super().__init__(date)
        self.preffered_mentor = None
        self.goal = None
        self.add_event(self)

    def set_goal(self, goal):
        self.goal = goal

    def set_preffered_mentor(self, preffered_mentor):
        self.preffered_mentor = preffered_mentor

    def __str__(self):
        return '{} private mentoring with {} about {}'.format(self.date, self.preffered_mentor, self.goal)
