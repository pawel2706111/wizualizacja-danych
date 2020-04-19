# zadanie 9
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpyi stwórz
# macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego.
import numpy as np

macierz = np.empty((5, 5), dtype='int')
a = 0
b = 1
for i in range(0, 5, 1):
    for j in range(0, 5, 1):
        macierz[i, j] = b
        b += a
        a = b-a

print(macierz)