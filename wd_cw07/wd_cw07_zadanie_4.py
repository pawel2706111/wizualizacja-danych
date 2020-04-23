# zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich
# będzie zawierała liczby całkowite, a druga liczby rzeczywiste.
# Następnie wykonaj na nich operację mnożenia.
import numpy as np

A = np.array([1, 2, 3], dtype=int)
B = np.array([1.5, 2.6, 4.9], dtype=float)
print(A*B)
print('typ danych:', (A*B).dtype)