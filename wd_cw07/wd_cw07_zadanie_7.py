# zadanie 7
# Wykonaj funkcję dodawania obu macierzy
# zapisanych wcześniej do zmiennych a i b.
import numpy as np

katy = np.array([[0, 30, 45], [90, 75, 25]])
a = np.empty((2, 3))
a = np.sin(katy*np.pi/180)
b = np.empty((2, 3))
b = np.cos(katy*np.pi/180)
print('a:')
print(a)
print('b:')
print(b)
print('a+b:')
print(a+b)
print('np.sum(a+b):')
print(np.sum(a+b))