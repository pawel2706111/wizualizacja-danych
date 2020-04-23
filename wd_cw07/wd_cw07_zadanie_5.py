# zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie
# wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.
import numpy as np

katy = np.array([[0, 30, 45], [90, 75, 25]])
a = np.empty((2, 3))
a = np.sin(katy*np.pi/180)
print('katy:')
print(katy)
print('a:')
print(a)
for i in range(0, 2, 1):
    for j in range(0, 3, 1):
        print('sin('+str(katy[i, j])+') =', a[i, j])