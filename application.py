from controller import Controller


def main():
    controller = Controller()
    controller.fill_with_data("data/events.csv")
    controller.start()


if __name__ == '__main__':
    main()
