import numpy as np
from easyAI import TwoPlayerGame

DIRECTIONS = list(map(np.array, [[1, 2], [-1, 2], [1, -2], [-1, -2],
                                 [2, 1], [2, -1], [-2, 1], [-2, -1]]))

pos2string = lambda ab: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[ab[0]] + str(ab[1] + 1)
string2pos = lambda s: np.array(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(s[0]), int(s[1]) - 1])


class Knights(TwoPlayerGame):
    """
    Gra dla dwóch graczy, w której każdy ma swojego skoczka na szachownicy.
    Skoczki poruszają się w kształcie "L", a każdy ruch musi być na nieodwiedzone pole.
    Przegrywa gracz, który nie ma możliwości ruchu.
    """

    def __init__(self, players, board_size=(8, 8)):
        print(f"Ustawiam planszę o rozmiarze: {board_size}")
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
        """Zwraca listę wszystkich możliwych ruchów dla bieżącego gracza."""
        endings = [self.player.pos + d for d in DIRECTIONS]
        return [pos2string(e) for e in endings
                if (e[0] >= 0) and (e[1] >= 0) and
                (e[0] < self.board_size[0]) and
                (e[1] < self.board_size[1]) and
                self.board[e[0], e[1]] == 0]

    def make_move(self, pos):
        pi, pj = self.player.pos  # Pobiera bieżącą pozycję gracza
        self.board[pi, pj] = 3  # Oznacza stare miejsce gracza jako zablokowane (3 = blokada)
        self.player.pos = string2pos(pos)  # Aktualizuje pozycję gracza
        pi, pj = self.player.pos  # Pobiera nową pozycję gracza
        self.board[pi, pj] = self.current_player  # Ustawia gracza na nowej pozycji na planszy
        self.last_player = self.nplayer  # Zapisz, który gracz wykonał ostatni ruch

    def ttentry(self):
        e = [tuple(row) for row in self.board]
        e.append(pos2string(self.players[0].pos))
        e.append(pos2string(self.players[1].pos))
        return tuple(e)

    def ttrestore(self, entry):
        for x, row in enumerate(entry[:self.board_size[0]]):
            for y, n in enumerate(row):
                self.board[x, y] = n
        self.players[0].pos = string2pos(entry[-2])
        self.players[1].pos = string2pos(entry[-1])

    def show(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print('\n' + '    ' + '   '.join(str(i + 1) for i in range(self.board_size[1])))
        for k in range(self.board_size[0]):
            print(letters[k] + ' | ' + ' | '.join(
                [['.', '1', '2', 'X'][self.board[k, i]] for i in range(self.board_size[1])]))

    def lose(self):
        """Sprawdza, czy bieżący gracz przegrał (czyli brak dostępnych ruchów)."""
        return self.possible_moves() == []

    def is_over(self):
        """Sprawdza, czy gra się zakończyła."""
        return self.lose()

    def winner(self):
        """Zwraca numer gracza, który wygrał, czyli tego, kto wykonał ostatni ruch."""
        return 3 - self.nplayer

    def scoring(self):
        """Metoda oceniająca stan gry dla AI"""
        return -100 if self.lose() else 0

