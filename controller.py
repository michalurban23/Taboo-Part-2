from datetime import date
from events import Event, Checkpoint, PrivateMentoring
from database import save_events_to_file, load_events_from_file
from foolproof import is_number, is_date, is_in_range
import view


class Controller:

    def start(self):

        while True:

            view.print_main_menu()
            try:
                choice = view.get_choice()
                is_in_range(choice, [str(i) for i in range(7)])

            except ValueError as err_msg:
                view.print_error(err_msg)

            else:
                self.handle_menu(choice)

            view.pause()

    def handle_menu(self, choice):

        if choice == "1":
            self.book_private_mentoring()

        elif choice == "2":
            self.book_checkpoint()

        elif choice == "3":
            self.display_all_events()

        elif choice == "4":
            self.cancel_event()

        elif choice == "5":
            self.reschedule_event()

        elif choice == "6":
            self.start_mentor_panel()

        elif choice == "0":
            self.say_goodbye()
            save_events_to_file("data/events.csv")
            exit()

    def display_all_events(self, name=""):

        if name:
            name = ""
        else:
            name = view.get_name()
        view.print_list(Event.get_events(name))
        return Event.get_events(name)

    def book_checkpoint(self):

        date = self.get_correct_date()

        if date:
            name = view.get_name()
            Checkpoint(self.convert_date(date), name)
            view.print_message("Event created!")

        else:
            view.print_error("Could not create an event")

    def book_private_mentoring(self):

        date = self.get_correct_date()

        if date:
            name = view.get_name()
            new_event = PrivateMentoring(self.convert_date(date), name)
            view.print_message("Event created!")

            goal = view.get_goal(self)
            new_event.set_goal(goal)

            mentor = view.get_mentor(new_event.get_mentors())
            new_event.set_preffered_mentor(mentor)

        else:
            view.print_error("Could not create an event")

    def cancel_event(self):

        view.print_title("Event cancelation")
        events = self.display_all_events()

        if events:
            try:
                index = view.get_choice()
                is_number(index)
                is_in_range(int(index), range(1, len(events)+1))

            except ValueError as err_msg:
                view.print_error(err_msg)

            else:
                event = events[int(index)-1]
                event.cancel_event(event)

    def reschedule_event(self):

        view.print_title("Event reschedule")
        events = self.display_all_events()

        if events:
            try:
                index = view.get_choice()
                is_number(index)
                is_in_range(int(index), range(1, len(events)+1))

            except ValueError as err_msg:
                view.print_error(err_msg)

            else:
                date = self.get_correct_date()
                if date:
                    event = events[int(index)-1]
                    event.reschedule_event(self.convert_date(date))
                else:
                    view.print_error("Could not reschedule event")

    def start_mentor_panel(self):

        password = view.get_password()

        if password == "coffee":
            self.cancel_event_as_mentor()

        else:
            view.print_error("Nice try LOL")

    def cancel_event_as_mentor(self):

        view.print_title("Event cancelation")
        events = self.display_all_events("mentor")

        if events:
            try:
                index = view.get_choice()
                is_number(index)
                is_in_range(int(index), range(1, len(events)+1))

            except ValueError as err_msg:
                view.print_error(err_msg)

            else:
                event = events[int(index)-1]
                event.cancel_event(event)

    def say_goodbye(self):

        view.print_goodbye()

    @staticmethod
    def convert_date(date_str):

        date_list = date_str.split("-")
        return date(int(date_list[2]), int(date_list[1]), int(date_list[0]))

    @staticmethod
    def fill_with_data(filename):

        load_events_from_file(filename)

    @staticmethod
    def get_correct_date():

        date = view.get_event_date()

        try:
            is_date(date)

        except IndexError as err_msg:
            view.print_error(err_msg)

        else:
            return date
