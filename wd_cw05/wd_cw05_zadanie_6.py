# zadanie 6
# Przetestuj powyższy iterator na kilku różnych kolekcjach.
class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

lista = Wspak([1, 2, 3, 4, 5])
print('lista:', end=' ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista))
krotka = Wspak((1, 2, 3, 4, 5))
print('krotka:', end=' ')
print(next(krotka), end=', ')
print(next(krotka), end=', ')
print(next(krotka), end=', ')
print(next(krotka), end=', ')
print(next(krotka))
napis = Wspak('12345')
print('napis:', end=' ')
print(next(napis), end=', ')
print(next(napis), end=', ')
print(next(napis), end=', ')
print(next(napis), end=', ')
print(next(napis))
# slownik = Wspak({'jeden': 1, 'dwa': 2, 'trzy': 3, 'cztery': 4, 'pięć': 5})
# zbior = Wspak({1, 2, 3, 4, 5})
# Powyższe Nie działają