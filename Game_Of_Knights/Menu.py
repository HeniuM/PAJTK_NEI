def show_rules():
    try:
        with open("zasady.txt", "r") as file:
            rules = file.read()
            print(rules)

    except FileNotFoundError:
        print("Nie można zaleźć pliku z zasadami!!")


def show_menu():
    print("Wybierz opcje: ")
    print("1) Zasady gry ")
    print("2) Prezentacja rozgrywki automatycznej (AI vs AI)")
    print("3) Rozgrywka normalna (Gracz vs AI)")

    choice = input("Wybierz numer opcji: ")
    return choice  # Upewnij się, że zwracana wartość to string


def choose_board_size():
    print("Wybierz rozmiar planszy")
    print("1) 5x5")
    print("2) 8x8")
    print("3) 10x10")

    choice = input("Wybierz numer opcji: ")

    if choice == "1":
        return (5, 5)
    elif choice == "2":
        return (8, 8)
    elif choice == "3":
        return (10, 10)
    else:
        print("Nieprawidłowy wybór, domyślnie ustawiamy planszę 8x8. ")
        return (8, 8)
