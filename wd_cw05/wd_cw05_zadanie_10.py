# zadanie 10
# Zaimportuj pakiet itertools i znajdź w jego dokumentacji
# sposób na wygenerowanie kombinacji 3 elementowych
# bez powtórzeń na zbiorze 10 elementowym.
from itertools import *

kombinacje = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(kombinacje)
print('liczba kombinacji:', len(kombinacje))