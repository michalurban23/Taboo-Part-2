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
        raise ValueError("That option is not available!")


def is_data(input_):

    try:
        day, month, year = input_.split("-")

    except IndexError:
        raise IndexError("That is not a correct format")

    else:
        pass
