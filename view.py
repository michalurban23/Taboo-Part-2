from os import system


def clear():

    system("clear")


def print_all_events(events):

    for event in events:
        print(event)


def print_main_menu():

    print("\nChoose option: ")
    print("1 - Book private mentoring")
    print("2 - Book checkpoint")
    print("3 - Show all my events\n")


def print_goodbye():

    print("\nBye bye\n")


def get_choice():

    user_choice = input("Choose option: ")
    return user_choice


def get_event_date():

    date = input("\nEnter date dd-mm-yyyy: ")
    return date


def get_preffered_mentor(self):

    mentor = input("\nEnter preffered mentor: ")
    return mentor


def get_goal(self):

    goal = input("Enter your goal: ")
    return goal
