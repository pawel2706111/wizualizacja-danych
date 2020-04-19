# zadanie 5
# Napisz funkcję, która:
#    ■ na wejściu przyjmuje jeden parametr określający długość wektora,
#    ■ na podstawie parametru generuje wektor, ale w kolejności odwróconej (czyli np. dla n=3 =>[3 2 1])
#    ■ generuje macierz diagonalną z w/w wektorem jako przekątną
import numpy as np

def funkcja(n):
    wektor = np.arange(n, 0, -1)
    return np.diag([a for a in wektor])

macierz = funkcja(5)
print(macierz)
