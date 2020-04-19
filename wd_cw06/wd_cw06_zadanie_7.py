# zadanie 7
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
# Przy założeniach: funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n
# i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.
import numpy as np

def funkcja(n):
    macierz = np.empty((n, n), dtype='int')
    for i in range(0, n, 1):
        macierz[i, i] = 2
        for j in range(0, n, 1):
            if(j < i):
                macierz[i, j] = 2*(i-j+1)
            if(j > i):
                macierz[i, j] = 2*(j-i+1)
    return macierz

macierz = funkcja(5)
print(macierz)