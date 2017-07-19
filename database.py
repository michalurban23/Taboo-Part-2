from events import Checkpoint, PrivateMentoring
from random import choice
from string import printable
from datetime import date


def save_events_to_file(filename):

    checkpoints = Checkpoint.get_checkpoints()
    private_mentorings = PrivateMentoring.get_private_mentorings()

    save_checkpoints(filename, checkpoints)
    save_mentorings(filename, private_mentorings)


def save_checkpoints(filename, checkpoints):

    with open(filename, "w") as f:
        for event in checkpoints:
            f.write("CP{},".format(get_id()))
            f.write(",".join([str(event.date), event.creator]))
            f.write("\n")


def save_mentorings(filename, private_mentorings):

    with open(filename, "a") as f:
        for event in private_mentorings:
            f.write("PM{},".format(get_id()))
            f.write(",".join([str(event.date), event.creator, event.goal, event.preffered_mentor]))
            f.write("\n")


def load_events_from_file(filename):

    with open(filename, "r") as f:
        for line in f:
            data = line.rstrip("\n").split(",")
            if line.startswith("CP"):
                Checkpoint(convert_date_from_string(data[1]), data[2])
            elif line.startswith("PM"):
                PrivateMentoring(convert_date_from_string(data[1]), data[2], data[3], data[4])


def convert_date_from_string(date_str):

    return date(*map(int, date_str.split("-")))


def get_id():

    return "".join([choice(printable[:73]) for i in range(4)])
