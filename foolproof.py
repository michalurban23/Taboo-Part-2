def is_number(input_):

    try:
        int(input_)

    except ValueError:
        raise ValueError("A number is required!")

    else:
        return True


def is_in_range(input_, range_):

    if input_ in range_:
        return True

    else:
        raise ValueError("Wrong input!")


def is_date(str_input):

    try:
        day, month, year = str_input.split("-")

    except ValueError:
        raise IndexError("That is not a correct format")

    else:
        try:
            if is_in_range(int(day), range(1, 32)) and \
               is_in_range(int(month), range(1, 13)) and \
               is_in_range(int(year), range(2000, 2100)):
                    return True
        except ValueError:
            raise IndexError("Parameters out of range!")
