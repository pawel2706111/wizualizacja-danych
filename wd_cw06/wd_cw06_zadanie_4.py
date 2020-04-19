# zadanie 4
# Napisz funkcję, która będzie przyjmowała 2 parametry:
#     ■ liczbę, która będzie podstawą operacji potęgowania
#     ■ oraz ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową
# kolejnych potęg podanej liczby, np. generuj(2,4) -> [2 4 8 16]
import numpy as np

def funkcja(podstawa, n):
    return np.logspace(1, n, num=n, base=podstawa, dtype=type(podstawa))

tab1 = funkcja(2,4)
print(tab1)
tab2 = funkcja(0.25, 6)
print(tab2)