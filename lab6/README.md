# Rozpoznawanie Kolorów za Pomocą Kamerki Internetowej

## Opis projektu
Projekt ten wykorzystuje kamerę internetową do przechwytywania obrazu, a następnie analizuje kolory w obszarze wskazanym przez celownik na środku obrazu. Rozpoznawane są kolory z podstawowej palety RGB: czerwony, zielony i niebieski.

### Autorzy
- Henryk Mudlaff, s26071  
  GitHub: [HeniuM](https://github.com/HeniuM)

- Benedykt Borowski, s20685  
  GitHub: [BenedyktB](https://github.com/BenedyktB)

## Wymagania
Do uruchomienia projektu wymagane są:
- Python 3.7 lub nowszy
- Zainstalowana biblioteka OpenCV
- Zainstalowana biblioteka NumPy

## Instalacja
1. Upewnij się, że masz zainstalowanego Pythona oraz menedżera pakietów `pip`.
2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install opencv-python-headless numpy
   ```
3. Skopiuj pliki projektu do wybranego folderu.

## Uruchomienie
1. Uruchom plik `main.py`:
   ```bash
   python main.py
   ```
2. Po uruchomieniu programu otworzy się okno z obrazem z kamerki i celownikiem na środku.
3. Analizowany kolor będzie wyświetlany w lewym górnym rogu obrazu.
4. Aby zakończyć program, naciśnij klawisz `q`.

## Funkcjonalności
- **Rysowanie celownika:** Na środku obrazu rysowany jest żółty celownik.
- **Analiza koloru:** Rozpoznawanie koloru na podstawie wartości RGB pikseli w obszarze celownika.
- **Rozpoznawane kolory:** Czerwony, zielony, niebieski oraz brak dominującego koloru.

## Struktura projektu
- `main.py` - Główny plik programu zawierający kod realizujący funkcjonalność projektu.

## Przykład działania
1. Uruchomienie programu wczytuje obraz z kamerki w czasie rzeczywistym.
2. Celownik wskazuje piksel, którego kolor jest analizowany.
3. Na ekranie wyświetlana jest nazwa rozpoznanego koloru w czasie rzeczywistym.

## Uwagi
- Program działa poprawnie z większością kamer internetowych.
- W przypadku problemów z kamerą, upewnij się, że inne aplikacje jej nie wykorzystują.

## Licencja
Projekt jest udostępniony na licencji MIT. Możesz go dowolnie modyfikować i wykorzystywać.

---
Jeśli masz pytania lub sugestie dotyczące projektu, skontaktuj się z autorami.
