class Event():

    events = []

    def __init__(self, date, creator="None"):

        self.date = date
        self.creator = creator

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

    def __init__(self, date, creator="None"):

        super().__init__(date, creator)
        self.add_event(self)

    def __str__(self):

        return "{} checkpoint".format(self.date)

    @classmethod
    def get_checkpoints(cls):

        return [event for event in cls.events if isinstance(event, Checkpoint)]


class PrivateMentoring(Event):

    def __init__(self, date, creator="None", preffered_mentor="None", goal="None"):

        super().__init__(date, creator)
        self.preffered_mentor = preffered_mentor
        self.goal = goal
        self.add_event(self)

    def __str__(self):

        return '{} private mentoring with {} about {}'.format(self.date, self.preffered_mentor, self.goal)

    def set_goal(self, goal):

        self.goal = goal

    def set_preffered_mentor(self, preffered_mentor):

        self.preffered_mentor = preffered_mentor

    @classmethod
    def get_private_mentorings(cls):

        return [event for event in cls.events if isinstance(event, PrivateMentoring)]
