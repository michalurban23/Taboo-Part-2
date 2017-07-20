from os import system


def clear():

    system("clear")


def pause():

    input("\nPress enter to continue\n")


def print_error(err_msg):

    print("\033[1;31m" + "\n{}\n".format(err_msg) + "\033[0;0m")


def print_message(message):

    print("\033[1;33m" + "\n{}\n".format(message) + "\033[0;0m")


def print_all_events(events):

    print("")
    for event in events:
        print(event)
    print("")


def print_main_menu():

    clear()
    print("* * Event Manager * *\n")
    print("1 - Book private mentoring")
    print("2 - Book checkpoint")
    print("3 - Show all my events")
    print("4 - Cancel event")
    print("5 - Reschedule event")
    print("\n6 - Mentor Panel\n")


def print_goodbye():

    print("\nBye bye\n")


def get_choice():

    user_choice = input("\nChoose option: ")
    return user_choice


def get_event_date():

    date = input("\nEnter date dd-mm-yyyy: ")
    return date


def get_preffered_mentor(self):

    mentor = input("\nEnter preffered mentor: ")
    return mentor


def get_goal(self):

    goal = input("\nEnter your goal: ")
    return goal
