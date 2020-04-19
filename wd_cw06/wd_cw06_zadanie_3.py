# zadanie 3
# Napisz funkcję, która będzie:
#   ■ przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
#   ■ zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
# Istnieją sposoby na szybkie stworzenie bardziej rozbudowanych tablic/macierzy.
import numpy as np

def funkcja(n):
    if type(n) != type(1):
        print(type(n))
        raise TypeError('Podany parametr nie jest liczbą całkowitą')
    tablica = np.empty((n, n), dtype='int')
    liczba = 1
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            tablica[i, j] = liczba
            liczba += 1
    return tablica

tab = funkcja(5)
print(tab)