# zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie
# wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
import numpy as np

katy = np.array([[0, 30, 45], [90, 75, 25]])
b = np.empty((2, 3))
b = np.cos(katy*np.pi/180)
print('katy:')
print(katy)
print('b:')
print(b)
for i in range(0, 2, 1):
    for j in range(0, 3, 1):
        print('cos('+str(katy[i, j])+') =', b[i, j])