class Event():

    events = []
    mentors = ["Mateusz Steliga", "Mateusz Ostafil", "Agnieszka Koszany"]

    def __init__(self, date, creator="None"):

        self.date = date
        self.creator = creator

    def get_date(self):

        return self.date

    def reschedule_event(self, date):

        self.date = date

    @classmethod
    def sort_events(cls):

        cls.events.sort(key=lambda event: event.date)

    @classmethod
    def add_event(cls, event):

        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls, name=""):

        if name:
            return [event for event in cls.events if name == event.creator]
        return cls.events

    @classmethod
    def get_mentors(cls):

        return cls.mentors

    @classmethod
    def cancel_event(cls, event):

        cls.events.remove(event)


class Checkpoint(Event):

    def __init__(self, date, creator="None"):

        super().__init__(date, creator)
        self.add_event(self)

    def __str__(self):

        return "{} checkpoint of {}".format(self.date, self.creator)

    @classmethod
    def get_checkpoints(cls):

        return [event for event in cls.events if isinstance(event, Checkpoint)]


class PrivateMentoring(Event):

    def __init__(self, date, creator="None", goal="None", preffered_mentor="None"):

        super().__init__(date, creator)
        self.goal = goal
        self.preffered_mentor = preffered_mentor
        self.add_event(self)

    def __str__(self):

        return '{} private mentoring of {} with {} about {}'.format(self.date, self.creator,
                                                                 self.preffered_mentor, self.goal)

    def set_goal(self, goal):

        self.goal = goal

    def set_preffered_mentor(self, preffered_mentor):

        self.preffered_mentor = preffered_mentor

    @classmethod
    def get_private_mentorings(cls):

        return [event for event in cls.events if isinstance(event, PrivateMentoring)]
