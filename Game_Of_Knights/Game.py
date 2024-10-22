from easyAI import AI_Player, Negamax, Human_Player
from Knights import Knights


def start_game(choice):

    """
    Function to start the game based on the user's choice.

    Args:
        choice (str): User's choice of the game mode ("2" for AI vs AI, "3" for Player vs AI).

    Returns:
        None
    """

    from Menu import choose_board_size
    board_size = choose_board_size()

    if choice == "2":
        ai_algo = Negamax(11)
        game = Knights([AI_Player(ai_algo), AI_Player(ai_algo)], board_size)
        game.play()
    elif choice == "3":
        ai_algo = Negamax(11)
        game = Knights([Human_Player(), AI_Player(ai_algo)], board_size)
        game.play()
    else:
        print("Wrong choice!")
        return

    if game.is_over():
        winner = game.winner()
        loser = 3 - winner
        print(f"Player {winner} is the winner! Player {loser} loses!")
