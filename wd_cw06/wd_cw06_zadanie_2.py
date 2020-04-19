# zadanie 2
# Stwórz listę składającą się zwartości zmiennoprzecinkowych
# a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64.
import numpy as np

tablica = np.arange(2, dtype='float')
print('tablica przed zmianą:', tablica)
tablica = tablica.astype('int64')
print('tablica po zmianie:', tablica)