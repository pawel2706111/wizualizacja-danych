# zadanie 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź
# najniższe wartości dla każdej kolumny i każdego rzędu.
import numpy as np
import random
from datetime import datetime

A = np.empty((3,3), dtype=int)
B = np.empty((4,4), dtype=int)

random.seed(datetime.now())

for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        A[i, j] = random.random()*11
for i in range(0, 4, 1):
    for j in range(0, 4, 1):
        B[i, j] = random.random()*11

print('macierz A:')
print(A)
print()
print('macierz A min z 1 kolumny:', A.min(axis=0)[0])
print('macierz A min z 2 kolumny:', A.min(axis=0)[1])
print('macierz A min z 3 kolumny:', A.min(axis=0)[2])
print()
print('macierz A min z 1 wiersza:', A.min(axis=1)[0])
print('macierz A min z 2 wiersza:', A.min(axis=1)[1])
print('macierz A min z 3 wiersza:', A.min(axis=1)[2])
print()
print('macierz B:')
print(B)
print()
print('macierz B min z 1 kolumny:', B.min(axis=0)[0])
print('macierz B min z 2 kolumny:', B.min(axis=0)[1])
print('macierz B min z 3 kolumny:', B.min(axis=0)[2])
print('macierz B min z 4 kolumny:', B.min(axis=0)[3])
print()
print('macierz B min z 1 wiersza:', B.min(axis=1)[0])
print('macierz B min z 2 wiersza:', B.min(axis=1)[1])
print('macierz B min z 3 wiersza:', B.min(axis=1)[2])
print('macierz B min z 4 wiersza:', B.min(axis=1)[3])