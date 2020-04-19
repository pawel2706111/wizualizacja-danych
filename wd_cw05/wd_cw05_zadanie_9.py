# zadanie 9
# Przepisz jeden z napisanych przez siebie iteratorów na generator.
#
# na potrzeby tego zadania przepisze iterator z zadania 7 na generator
def parzysty(dane):
    for i in range(0, len(dane), 1):
        yield dane[i]

liczby = parzysty([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby))