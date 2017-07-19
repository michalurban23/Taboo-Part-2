from datetime import date
from events import Event, Checkpoint, PrivateMentoring
from database import save_events_to_file, load_events_from_file
from foolproof import is_number, is_data, is_in_range
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

    def display_all_events(self):

        view.print_all_events(Event.get_events())

    def book_event(self):

        pass

    def book_checkpoint(self):

        date = view.get_event_date()
        date = self.convert_date(date)
        Checkpoint(date)

    def book_private_mentoring(self):

        date = view.get_event_date()
        date = self.convert_date(date)
        PrivateMentoring(date)

    def cancel_event(self):
        pass

    def reschedule_event(self):
        pass

    def start_mentor_panel(self):
        pass

    def say_goodbye(self):

        view.print_goodbye()

    @staticmethod
    def convert_date(date_str):

        date_list = date_str.split("-")
        return date(int(date_list[2]), int(date_list[1]), int(date_list[0]))

    @staticmethod
    def fill_with_data(filename):

        load_events_from_file(filename)
