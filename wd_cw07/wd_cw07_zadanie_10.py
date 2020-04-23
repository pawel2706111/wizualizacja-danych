# zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt.
# Jakie mamy możliwości i dlaczego?
import numpy as np

a = np.arange(81).reshape(9, 9)
print('macierz 9x9:')
print(a)
print('możemy stworzyć z macierzy 9x9 następujące macierze:')
ilosc = 0
for i in range(1, 82, 1):
    if(81 % i == 0):
        print('macierz '+str(i)+'x'+str(81//i))
        print(a.reshape(i, 81//i))
print('każdą z tych macierzy można transponować lub spłaszczyć np.')
print('macierz 3x27:')
print(a.reshape(3, 27))
print('macierz 3x27 transponowana:')
print(a.reshape(3, 27).T)
print('macierz 3x27 spłaszczona:')
print(a.ravel())
