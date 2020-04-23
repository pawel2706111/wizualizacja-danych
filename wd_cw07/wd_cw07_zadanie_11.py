# zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4.
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
import numpy as np

a = np.arange(12)
print('płaski wektor:')
print(a)
print('macierz 3x4:')
print(a.reshape(3, 4))
print('macierz 4x3:')
print(a.reshape(4, 3))
print('macierz 2x6:')
print(a.reshape(2, 6))
print('macierz 3x4 spłaszczona:')
b = a.reshape(3, 4).ravel()
print(b)
print('macierz 4x3 spłaszczona:')
c = a.reshape(4, 3).ravel()
print(c)
print('macierz 2x6 spłaszczona:')
d = a.reshape(2, 6).ravel()
print(d)
if(a.all() == b.all() and b.all() == c.all() and c.all() == b.all()):
    print('wszystkie trzy spłaszczone macierze są identyczne')