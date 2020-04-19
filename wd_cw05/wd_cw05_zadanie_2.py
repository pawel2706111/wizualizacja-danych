# Przeciąż metodę __add__() dla klasy Kwadrat,
# która będzie zwracała instancje klasy Kwadrat o nowym boku,
# będącym sumą boków dodawanych do siebie kwadratów.

class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x
    
    def __add__(self, other):
        return self.x + other.x

kw1 = Kwadrat(5)
kw2 = Kwadrat(6)
kw3 = Kwadrat(kw1 + kw2)
kw4 = Kwadrat(kw1 + kw3)
print('kw1 ma wymiary:', kw1.x,'x', kw1.y)
print('kw2 ma wymiary:', kw2.x,'x', kw2.y)
print('kw3 ma wymiary:', kw3.x,'x', kw3.y)
print('kw4 ma wymiary:', kw4.x,'x', kw4.y)