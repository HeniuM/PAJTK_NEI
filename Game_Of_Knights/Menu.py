def show_rules():

    """
    Function to display the game rules by reading them from a file.

    Args:
        None

    Returns:
        None
    """

    try:
        with open("rules.txt", "r") as file:
            rules = file.read()
            print(rules)

    except FileNotFoundError:
        print("Can not find the file with the game rules!!")


def show_menu():

    """
    Function to display the game menu and prompt the user to choose an option.

    Args:
        None

    Returns:
        str: The user's choice (1, 2, or 3).
    """

    print("Choose option: ")
    print("1) Game rules ")
    print("2) Presentation of the automatic gameplay (AI vs AI)")
    print("3) Normal Gameplay (Player vs AI)")

    choice = input("Choose option number: ")
    return choice


def choose_board_size():

    """
    Function to display options for board size and prompt the user to select one.

    Args:
        None

    Returns:
        tuple: The chosen board size (rows, columns) as a tuple.
    """

    print("Choose the board size")
    print("1) 8x8")
    print("2) 10x10")

    choice = input("Choose option number: ")

    if choice == "1":
        return (8, 8)
    elif choice == "2":
        return (10, 10)
    else:
        print("Wrong choice, setting the default board size to 8x8. ")
        return (8, 8)
