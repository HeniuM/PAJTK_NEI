import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


"""
System oceny personelu w firmie przy użyciu logiki rozmytej.

Autorzy: Henryk Mudlaff oraz Benedykt Borowski

Instrukcja: Ten kod wykorzystuje bibliotekę scikit-fuzzy do stworzenia systemu oceny pracowników
w firmie na podstawie trzech kryteriów: kompetencji, ilości wykonanych zadań (pull request),
oraz liczby zmian pracodawców. Wyjściem systemu jest dopasowanie do stanowiska oraz sugerowana wypłata.

Wymagania:
1. Zainstalowana biblioteka scikit-fuzzy: `pip install scikit-fuzzy`
"""


"""
Poniżej definiujemy zmienne wejściowe dla systemu oceny personelu:
- kompetencje: wyrażone jako wartość procentowa (0-100).
- pull_request: wskaźnik liczby wykonanej pracy wyrażony jako procent (0-100).
- liczba_pracodawców: liczba zmian pracodawców w przedziale od 1 do 10.
"""

kompetencje = ctrl.Antecedent(np.arange(0, 101, 1), 'kompetencje')
pull_request = ctrl.Antecedent(np.arange(0, 101, 1), 'pull_request')
liczba_pracodawcow = ctrl.Antecedent(np.arange(1, 11, 1), 'liczba_pracodawcow')

"""
Poniżej definiujemy zmienne wyjściowe, które będą obliczane przez system:
- dopasowanie: określa dopasowanie pracownika do stanowiska na skali od 0 do 100.
- wyplata: sugerowana wartość wynagrodzenia dla pracownika, od 5000 PLN do 20000 PLN.
"""

dopasowanie = ctrl.Consequent(np.arange(0, 101, 1), 'dopasowanie')
wyplata = ctrl.Consequent(np.arange(5000, 20001, 1), 'wyplata')

"""
Każda zmienna wejściowa i wyjściowa jest podzielona na poziomy (np. niskie, średnie, wysokie),
które określają zakresy wartości. Funkcje przynależności definiują, w jaki sposób dany poziom
jest reprezentowany dla każdej zmiennej.
"""

kompetencje['niskie'] = fuzz.trimf(kompetencje.universe, [0, 0, 50])
kompetencje['srednie'] = fuzz.trimf(kompetencje.universe, [25, 50, 75])
kompetencje['wysokie'] = fuzz.trimf(kompetencje.universe, [50, 100, 100])

pull_request['niskie'] = fuzz.trimf(pull_request.universe, [0, 0, 50])
pull_request['srednie'] = fuzz.trimf(pull_request.universe, [25, 50, 75])
pull_request['wysokie'] = fuzz.trimf(pull_request.universe, [50, 100, 100])

liczba_pracodawcow['malo'] = fuzz.trimf(liczba_pracodawcow.universe, [1, 1, 5])
liczba_pracodawcow['srednio'] = fuzz.trimf(liczba_pracodawcow.universe, [3, 5, 7])
liczba_pracodawcow['duzo'] = fuzz.trimf(liczba_pracodawcow.universe, [5, 10, 10])

"""
Poniżej definiujemy funkcje przynależności dla zmiennych wyjściowych:
- dopasowanie: niskie, średnie, wysokie.
- wyplata: niskie, średnie, wysokie.
"""

dopasowanie['niskie'] = fuzz.trimf(dopasowanie.universe, [0, 0, 50])
dopasowanie['srednie'] = fuzz.trimf(dopasowanie.universe, [25, 50, 75])
dopasowanie['wysokie'] = fuzz.trimf(dopasowanie.universe, [50, 100, 100])

wyplata['niskie'] = fuzz.trimf(wyplata.universe, [5000, 5000, 10000])
wyplata['srednie'] = fuzz.trimf(wyplata.universe, [7500, 12500, 17500])
wyplata['wysokie'] = fuzz.trimf(wyplata.universe, [15000, 20000, 20000])

"""
Reguły logiki rozmytej są podstawą systemu wnioskowania.
Każda reguła określa, jaki wpływ mają poszczególne poziomy zmiennych wejściowych na wynik.
Przykład:
- Jeśli kompetencje są wysokie, pull request jest wysoki, a liczba pracodawców mała,
  wtedy dopasowanie do stanowiska jest wysokie, a wypłata wysoka.
"""

# Reguła 1: Jeśli kompetencje są wysokie, pull request jest wysoki i liczba pracodawców jest mała,
# wtedy dopasowanie jest wysokie i wypłata jest wysoka
rule1 = ctrl.Rule(kompetencje['wysokie'] & pull_request['wysokie'] & liczba_pracodawcow['malo'],
                  (dopasowanie['wysokie'], wyplata['wysokie']))

# Reguła 2: Jeśli kompetencje są średnie, pull request jest średni i liczba pracodawców jest średnia,
# wtedy dopasowanie jest średnie i wypłata jest średnia
rule2 = ctrl.Rule(kompetencje['srednie'] & pull_request['srednie'] & liczba_pracodawcow['srednio'],
                  (dopasowanie['srednie'], wyplata['srednie']))

# Reguła 3: Jeśli kompetencje są niskie lub pull request jest niski lub liczba pracodawców jest duża,
# wtedy dopasowanie jest niskie i wypłata jest niska
rule3 = ctrl.Rule(kompetencje['niskie'] | pull_request['niskie'] | liczba_pracodawcow['duzo'],
                  (dopasowanie['niskie'], wyplata['niskie']))


"""
Tworzymy system kontrolny i symulację opartą na powyższych regułach.
System kontrolny jest konfiguracją, która obejmuje wszystkie zdefiniowane reguły
i pozwala na symulowanie różnych wartości wejściowych i ich wpływu na wynik.
"""

ocena_personelu_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
ocena_personelu = ctrl.ControlSystemSimulation(ocena_personelu_ctrl)


"""
Przykładowe dane wejściowe:
- kompetencje: 80 (wysokie)
- pull_request: 70 (wysokie)
- liczba_pracodawcow: 2 (mała liczba zmian pracodawców)

System przetworzy te dane i wygeneruje sugerowane wartości wyjściowe dla
dopasowania do stanowiska oraz wypłaty.
"""


ocena_personelu.input['kompetencje'] = 80
ocena_personelu.input['pull_request'] = 70
ocena_personelu.input['liczba_pracodawcow'] = 2

ocena_personelu.compute()

print("Dopasowanie do stanowiska:", ocena_personelu.output['dopasowanie'])
print("Wypłata:", ocena_personelu.output['wyplata'])
