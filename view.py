from os import system


def clear():

    system("clear")


def pause():

    input("\nPress enter to continue\n")


def print_error(err_msg):

    print("\033[1;31m" + "\n{}\n".format(err_msg) + "\033[0;0m")


def print_message(message):

    print("\033[1;33m" + "\n{}\n".format(message) + "\033[0;0m")


def print_list(events):

    if events:
        print()
        for index, event in enumerate(events):
            print("\t{}) {}".format(index+1, event))
    else:
        print("\nNothing to show :(")


def print_title(message):

    clear()
    print("* * {} * *".format(message))


def print_main_menu():

    clear()
    print("* * Event Manager * *\n")
    print("1 - Book private mentoring")
    print("2 - Book checkpoint")
    print("3 - Show all my events")
    print("4 - Cancel event")
    print("5 - Reschedule event")
    print("\n6 - Mentor Panel")
    print("\n0 - Exit\n")


def print_goodbye():

    clear()
    print("Bye bye\n")


def get_choice():

    user_choice = input("\nChoose option: ")
    return user_choice


def get_name():

    user_choice = input("\nEnter your fullname: ")
    return user_choice


def get_goal():

    user_choice = input("\nWhat's the goal of the mentoring? ")
    return user_choice


def get_password():

    clear()
    user_choice = input("What's the super secret mentor password?\nHINT: it's coffee ")
    return user_choice


def get_mentor(mentors):

    print("\nAvailable Mentors:")
    print_list(mentors)
    user_choice = input("\nWho is your preffered mentor for this event? ")
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
