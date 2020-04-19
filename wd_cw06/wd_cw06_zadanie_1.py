# zadanie 1
# Za pomocą funkcji arange stwórz tablicę Numpy
# składającą się 20 kolejnych wielokrotności liczby 2.
import numpy as np

tablica = np.arange(20)
for i in range (0, 20, 1):
    tablica[i] = 2*(i+1)
print(tablica)
