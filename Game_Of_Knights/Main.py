from Menu import show_menu, show_rules, choose_board_size
from Game import start_game


def main():
    while True:
        choice = show_menu()
        print(f"Wybrałeś opcję: {choice}")  # Dodaj to, aby sprawdzić, co zwraca input

        if choice == "1":
            show_rules()
        elif choice == "2" or choice == "3":
            print(f"Przekazuje do start_game: {choice}")  # Sprawdź, co jest przekazywane
            start_game(choice)
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


# TODO: poprawić zapis wygranych
# TODO: usunąć kod do debugowania
# TODO: zoptymalizować Knights.py


if __name__ == '__main__':
    main()
