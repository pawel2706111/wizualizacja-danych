# zadanie 1
# Stwórz 3 klasy: Material, Ubrania, Sweter.
# |-------------------|----------------------------|------------------------|
# |Klasa: Material    |Klasa: Ubrania              |Klasa: Sweter           |
# |-------------------|----------------------------|------------------------|
# |Atrybuty:          |Atrybuty:                   |Atrybuty:               |
# |■ rodzaj,          |■ rozmiar                   |■ rodzaj_swetra – np.   |
# |■ długość          |■ kolor                     |Rozpinany, z golfem itd.|
# |■ szerokość        |■ dla_kogo                  |Metody:                 |
# |Metody:            |Metody:                     |■ wyświetl_dane         |
# |■ konstruktor      |■ wyświetl_dane – do wyświe-|                        |
# |■ wyświetl_nazwę   |tlania informacji o ubraniu |                        |
# |-------------------|----------------------------|------------------------|
# Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania.
# Stwórz kilka instancji obiektów i sprawdź, które metody można wykorzystać.
class material:

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print('nazwa materiału:', self.rodzaj)

class ubrania(material):

    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print('rozmiar:', self.rozmiar)
        print('kolor:', self.kolor)
        print('dla kogo:', self.dla_kogo)

class sweter(ubrania):

    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print('rodzaj swetra:', self.rodzaj_swetra)

bawelna = material('bawełna', 1, 1)
jedwab = material('jedwab', 0.5, 0.5)
welna = material('wełna', 5, 5)

bawelna.wyswietl_nazwe()
jedwab.wyswietl_nazwe()
welna.wyswietl_nazwe()

ubranko = ubrania('XL', 'niebieski', 'Tomek')
ubranko.wyswietl_dane()
# ubranko.wyswietl_nazwe() <= Nie można wywołać tej metody

golf = sweter('Wieśwagen Golf GTI')
golf.wyswietl_dane()
# golf.wyswietl_nazwe() <= Też nie można wywołać tej metody