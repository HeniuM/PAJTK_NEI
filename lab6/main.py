"""
Projekt: Rozpoznawanie kolorów za pomocą kamerki internetowej
Autorzy: Henryk Mudlaff, Benedykt Borowski

Opis projektu:
Ten projekt korzysta z bibliotek OpenCV w Pythonie do przechwytywania obrazu z kamerki internetowej. Na środku obrazu
znajduje się celownik, który wskazuje obszar, w którym analizowany jest kolor. Program rozpoznaje podstawowe kolory z
palety RGB (czerwony, zielony, niebieski) oraz wyświetla nazwę rozpoznanego koloru na ekranie.

Wykorzystane biblioteki:
- OpenCV: do obsługi kamerki i manipulacji obrazem
- NumPy: do pracy z macierzami obrazu
"""

import cv2
import numpy as np


def get_dominant_color(b, g, r):
    """
    Funkcja rozpoznaje dominujący kolor na podstawie wartości kanałów RGB.

    Args:
        b (int): wartość kanału niebieskiego (Blue)
        g (int): wartość kanału zielonego (Green)
        r (int): wartość kanału czerwonego (Red)

    Returns:
        str: nazwa dominującego koloru (czerwony, zielony, niebieski lub brak dominującego koloru)
    """
    if r > g and r > b:
        return "Czerwony"
    elif g > r and g > b:
        return "Zielony"
    elif b > r and b > g:
        return "Niebieski"
    else:
        return "Brak dominujacego koloru"


def draw_crosshair(frame, x, y):
    """
    Funkcja rysuje celownik na środku obrazu.

    Args:
        frame (np.ndarray): ramka obrazu z kamerki
        x (int): współrzędna x środka obrazu
        y (int): współrzędna y środka obrazu
    """
    color = (0, 255, 255)  # Kolor celownika (żółty)
    thickness = 2  # Grubość linii celownika

    # Linie pozioma i pionowa celownika
    cv2.line(frame, (x - 20, y), (x + 20, y), color, thickness)
    cv2.line(frame, (x, y - 20), (x, y + 20), color, thickness)


def main():
    """
    Główna funkcja programu. Obsługuje kamerę, analizuje kolor w środku obrazu i wyświetla wynik.
    """
    # Uruchomienie kamerki
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Nie można uzyskać dostępu do kamerki.")
        return

    while True:
        ret, frame = cap.read()  # Pobranie ramki z kamerki
        if not ret:
            print("Nie udało się odczytać obrazu z kamerki.")
            break

        height, width, _ = frame.shape
        center_x, center_y = width // 2, height // 2

        # Pobranie wartości RGB z punktu na środku obrazu
        b, g, r = frame[center_y, center_x]
        color_name = get_dominant_color(b, g, r)

        # Wyświetlenie informacji o rozpoznanym kolorze
        cv2.putText(
            frame,
            f"Kolor: {color_name}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )

        # Rysowanie celownika
        draw_crosshair(frame, center_x, center_y)

        # Wyświetlenie obrazu
        cv2.imshow("Rozpoznawanie Kolorow", frame)

        # Wyjście z programu po wciśnięciu klawisza 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Zwolnienie zasobów
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
