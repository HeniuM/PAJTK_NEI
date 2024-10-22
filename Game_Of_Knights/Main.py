from Menu import show_menu, show_rules, choose_board_size
from Game import start_game


def main():
    """
    Main function to handle the game loop, displaying the menu and handling user input.

    Args:
        None

    Returns:
        None
    """
    while True:
        choice = show_menu()

        if choice == "1":
            show_rules()
        elif choice == "2" or choice == "3":
            start_game(choice)
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


if __name__ == '__main__':
    main()
