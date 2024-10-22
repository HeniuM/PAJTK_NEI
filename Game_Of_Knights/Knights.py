import numpy as np
from easyAI import TwoPlayerGame

DIRECTIONS = list(map(np.array, [[1, 2], [-1, 2], [1, -2], [-1, -2],
                                 [2, 1], [2, -1], [-2, 1], [-2, -1]]))

pos2string = lambda ab: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ab[0]] + str(ab[1] + 1)
string2pos = lambda s: np.array(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(s[0]), int(s[1]) - 1])


class Knights(TwoPlayerGame):
    """
    Class representing the Knights game for two players. Players move knights on a chessboard
    in "L" shapes. The game ends when one player has no valid moves, and that player loses.
    """

    def __init__(self, players, board_size=(8, 8)):
        """

        Initialize the game with wo players and a chessboard of the specified size.

        Args:
            players (list): A list containing two players (either AI or human)
            board_size (touple): A tuple representing the siuze of the board (rows, columns)
        """

        print(f"Setting the board size to: {board_size}")
        self.players = players
        self.board_size = board_size
        self.board = np.zeros(board_size, dtype=int)
        self.board[0, 0] = 1
        self.board[board_size[0] - 1, board_size[1] - 1] = 2
        players[0].pos = np.array([0, 0])
        players[1].pos = np.array([board_size[0] - 1, board_size[1] - 1])
        self.nplayer = 1
        self.current_player = 1
        self.last_player = None  # Zmienna śledząca, kto wykonał ostatni ruch

    def possible_moves(self):
        """

        Returns a list of all valid moves for the current player.

        Returns:
            list: A list valid moves, each in string form (e.g., "A3", "B5")

        """
        endings = [self.player.pos + d for d in DIRECTIONS]
        return [pos2string(e) for e in endings
                if (e[0] >= 0) and (e[1] >= 0) and
                (e[0] < self.board_size[0]) and
                (e[1] < self.board_size[1]) and
                self.board[e[0], e[1]] == 0]

    def make_move(self, pos):
        """

        Making move of player based on input from console and decision made by AI

        Args:
            board (list): A list representing the board for the current player.
            player.pos (list): A list representing the current player's position.
            last_player: saving which player made last move.
        """
        pi, pj = self.player.pos  # Pobiera bieżącą pozycję gracza
        self.board[pi, pj] = 3  # Oznacza stare miejsce gracza jako zablokowane (3 = blokada)
        self.player.pos = string2pos(pos)  # Aktualizuje pozycję gracza
        pi, pj = self.player.pos  # Pobiera nową pozycję gracza
        self.board[pi, pj] = self.current_player  # Ustawia gracza na nowej pozycji na planszy
        self.last_player = self.nplayer  # Zapisz, który gracz wykonał ostatni ruch

    def ttentry(self):
        """

        Generates a tuple representing the current board state and the players' positions.

        Returns:
            tuple: A tuple that contains the board state and the players positions.
        """
        e = [tuple(row) for row in self.board]
        e.append(pos2string(self.players[0].pos))
        e.append(pos2string(self.players[1].pos))
        return tuple(e)

    def ttrestore(self, entry):
        """

        Restores the game state from a tuple.

        Args:
            entry (tuple): A tuple representing the saved game state.
        """
        for x, row in enumerate(entry[:self.board_size[0]]):
            for y, n in enumerate(row):
                self.board[x, y] = n
        self.players[0].pos = string2pos(entry[-2])
        self.players[1].pos = string2pos(entry[-1])

    def show(self):
        """

        Displays the current game board state.

        """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print('\n' + '    ' + '   '.join(str(i + 1) for i in range(self.board_size[1])))
        for k in range(self.board_size[0]):
            print(letters[k] + ' | ' + ' | '.join(
                [['.', '1', '2', 'X'][self.board[k, i]] for i in range(self.board_size[1])]))

    def lose(self):
        """
        Checks if the game is over(the player have no more options to move).

        Returns:
            bool: True if the current player has no valid moves.
        """
        return self.possible_moves() == []

    def is_over(self):
        """
        Determine if the game is over, i.e., if one of the players has lost

        Returns:
            bool: True if the game is over (a player has lost)
        """
        return self.lose()

    def winner(self):
        """
        Determine the winner of the game. The winner is the player who did the last possible move on the board.

        Returns:
            int: The number of the player who won (either 1 or 2)
        """
        return 3 - self.nplayer

    def scoring(self):
        """

        Score the game state for AI. A loss for the current player results in a negative score.

        Returns:
            int: A negative score if the current player loses, otherwise 0.

        """
        return -100 if self.lose() else 0

