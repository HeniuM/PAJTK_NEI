from easyAI import AI_Player, Negamax, Human_Player
from Knights import Knights


def start_game(choice):
    """Function to start the game"""
    from Menu import choose_board_size

    board_size = choose_board_size()  # Pobiera rozmiar planszy

    if choice == "2":  # Poprawione porównanie do stringa
        ai_algo = Negamax(11)  # AI vs AI
        game = Knights([AI_Player(ai_algo), AI_Player(ai_algo)], board_size)
        game.play()
    elif choice == "3":  # Gracz vs AI
        ai_algo = Negamax(11)
        game = Knights([Human_Player(), AI_Player(ai_algo)], board_size)
        game.play()
    else:
        print("Nieprawidłowy wybór!")
