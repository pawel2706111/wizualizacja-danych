# zadanie 7
# Napisz własny iterator,
# który będzie zwracał tylko elementy 
# z parzystych indeksów przekazanej kolekcji.
class parzysty:
    
    def __init__(self, dane):
        self.dane = dane
        self.indeks = -2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indeks >= len(self.dane):
            raise StopIteration
        self.indeks += 2
        return self.dane[self.indeks]

liczby = parzysty([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby))