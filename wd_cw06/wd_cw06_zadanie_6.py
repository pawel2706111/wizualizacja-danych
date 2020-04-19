# zadanie 6
# Stwórz skrypt który na wyjściu wyświetli macierz numpy
# (tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie,
# jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.
import numpy as np

n = 7
poziom = 'poziom'
pion = 'pion'
skos = 'skos'

macierz = np.empty((n, n), dtype='U1')
for i in range(0, n, 1):
    for j in range(0, n, 1):
        macierz[i, j] = ' '

for i in range(0, len(pion), 1):
    macierz[i+1, 0] = pion[i]
for i in range(0, len(poziom), 1):
    macierz[0, i+1] = poziom[i]
for i in range(0, len(skos), 1):
    macierz[i, i] = skos[i]

for i in range(0, n, 1):
    for j in range(0, n, 1):
        print(macierz[i, j],'', end='')
    print()