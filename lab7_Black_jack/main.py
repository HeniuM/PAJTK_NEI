"""
Projekt: Blackjack AI Simulation

Opis:
Program symuluje rozgrywkę w Blackjacka między AI a AI oraz pozwala na interakcję użytkownika z AI.
Zawiera interfejs graficzny oraz system logowania decyzji podejmowanych przez AI.

Autorzy: Henryk Mudlaff, Benedykt Borowski
"""

import random
import numpy as np
import tkinter as tk
from tkinter import messagebox

class Blackjack:
    """
    Klasa reprezentująca grę w Blackjacka.
    Obsługuje rozdawanie kart, obliczanie wartości ręki oraz zasady gry.
    """
    def __init__(self):
        """Inicjalizuje nową grę w Blackjacka."""
        self.reset()

    def reset(self):
        """Resetuje stan gry, rozdając nowe karty dla gracza i krupiera."""
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]
        self.done = False
        return self.get_state()

    def draw_card(self):
        """Losuje jedną kartę, przy czym as ('A') jest reprezentowany jako wartość 1."""
        card = random.randint(1, 10)
        return 'A' if card == 1 else card

    def get_hand_value(self, hand):
        """Oblicza sumę wartości kart w ręce, traktując asy jako 11 lub 1, w zależności od sytuacji."""
        values = [11 if card == 'A' else card for card in hand]
        value = sum(values)
        while value > 21 and 11 in values:
            values[values.index(11)] = 1
            value = sum(values)
        return value

    def get_state(self):
        """Zwraca aktualny stan gry w postaci wartości ręki gracza i pierwszej karty krupiera."""
        return (self.get_hand_value(self.player_hand), self.dealer_hand[0])

    def step(self, action):
        """
        Wykonuje ruch gracza zgodnie z podaną akcją.
        Akcje:
        - 0: Stand (gracz nie dobiera kart)
        - 1: Hit (gracz dobiera kartę)
        """
        if action == 1:  # Hit
            self.player_hand.append(self.draw_card())
            if self.get_hand_value(self.player_hand) > 21:
                self.done = True
                return self.get_state(), -1, self.done  # Gracz przegrywa
        elif action == 0:  # Stand
            self.done = True
            while self.get_hand_value(self.dealer_hand) < 17:
                self.dealer_hand.append(self.draw_card())
            player_score = self.get_hand_value(self.player_hand)
            dealer_score = self.get_hand_value(self.dealer_hand)

            if dealer_score > 21 or player_score > dealer_score:
                return self.get_state(), 1, self.done  # Gracz wygrywa
            elif player_score == dealer_score:
                return self.get_state(), 0, self.done  # Remis
            else:
                return self.get_state(), -1, self.done  # Gracz przegrywa
        return self.get_state(), 0, self.done

class BlackjackGUI:
    """
    Klasa odpowiedzialna za interfejs graficzny gry.
    Obsługuje tryb AI vs AI oraz User vs AI.
    """
    def __init__(self):
        """Inicjalizuje interfejs graficzny gry."""
        self.window = tk.Tk()
        self.window.title("Blackjack Game")
        self.env = None

        self.mode_frame = tk.Frame(self.window)
        self.mode_frame.pack(pady=10)

        self.ai_vs_ai_button = tk.Button(self.mode_frame, text="AI vs AI", command=self.ai_vs_ai)
        self.ai_vs_ai_button.pack(side=tk.LEFT, padx=10)

        self.user_vs_ai_button = tk.Button(self.mode_frame, text="User vs AI", command=self.user_vs_ai)
        self.user_vs_ai_button.pack(side=tk.LEFT, padx=10)

        self.dealer_label = tk.Label(self.window, text="Dealer's Hand:")
        self.dealer_label.pack()
        self.dealer_cards = tk.Label(self.window, text="")
        self.dealer_cards.pack()

        self.player_label = tk.Label(self.window, text="Player's Hand:")
        self.player_label.pack()
        self.player_cards = tk.Label(self.window, text="")
        self.player_cards.pack()

        self.log_label = tk.Label(self.window, text="AI Action Log:")
        self.log_label.pack()
        self.log_text = tk.Text(self.window, height=20, width=60)
        self.log_text.pack()

        self.hit_button = tk.Button(self.window, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(self.window, text="Stand", command=self.stand)
        self.stand_button.pack()

        self.reset_game()

    def hit(self):
        """Obsługuje akcję 'Hit', dodając kartę do ręki gracza."""
        self.env.player_hand.append(self.env.draw_card())
        if self.env.get_hand_value(self.env.player_hand) > 21:
            self.end_game("Player busts! You lose.")
        self.update_display()

    def stand(self):
        """Obsługuje akcję 'Stand', kończąc turę gracza i przechodząc do krupiera."""
        self.env.done = True
        while self.env.get_hand_value(self.env.dealer_hand) < 17:
            self.env.dealer_hand.append(self.env.draw_card())
        self.update_display()
        self.evaluate_winner()

    def evaluate_winner(self):
        """Ocena końcowego wyniku gry po zakończeniu tury."""
        player_score = self.env.get_hand_value(self.env.player_hand)
        dealer_score = self.env.get_hand_value(self.env.dealer_hand)

        if dealer_score > 21 or player_score > dealer_score:
            self.end_game("You win!")
        elif player_score == dealer_score:
            self.end_game("It's a tie!")
        else:
            self.end_game("You lose!")

    def end_game(self, message):
        """Wyświetla komunikat końcowy i blokuje przyciski akcji."""
        self.update_display()
        messagebox.showinfo("Game Over", message)

    def run(self):
        """Uruchamia interfejs graficzny gry."""
        self.window.mainloop()

if __name__ == "__main__":
    app = BlackjackGUI()
    app.run()
