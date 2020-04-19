# zadanie 8
# Napisz własny iterator, który będzie zwracał tylko
# samogłoski z przekazanego ciągu tekstowego.
# Zaimplementuj sprawdzanie czy przekazany został string
# jako argument konstruktora tego iteratora (sprawdź funkcję isinstance()).
class samoglowski:
    
    def __init__(self, napis):
        if isinstance(napis, str):
            self.napis = napis
            self.indeks = 0
            self.lista_samogloski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
        else:
            raise ValueError('Przekazano typ inny niż string')

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks >= len(self.napis):
            raise StopIteration
        while self.indeks < len(self.napis):
            if self.napis[self.indeks] in self.lista_samogloski:
                self.indeks += 1
                return self.napis[self.indeks-1]
            self.indeks += 1

napis = samoglowski('napis')
print(next(napis))
print(next(napis))
if next(napis) == None:
    print('nie ma już więcej samogłosek w "'+napis.napis+'"')