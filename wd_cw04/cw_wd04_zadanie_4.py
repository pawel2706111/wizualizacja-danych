# zadanie 4
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
#     ■ nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
#     ■ konstruktor – który nadaje wartości
#     ■ wyświetl_produkt() – drukuje informacje o produkcie na ekranie
#     ■ ile_produktu() – informacje ile danego produktu ma być 
#       czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
#     ■ ile_kosztuje() – oblicza ile kosztuje dana ilość produktu
#       np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = float(ilosc)
        self.jednostka_miary = jednostka_miary
        self.cena_jed = float(cena_jed)
    def wyswietl_produkt(self):
        print('nazwa produktu: '+str(self.nazwa_produktu))
        print('ilość produktu: '+str(self.ilosc))
        print('jednostka miary: '+str(self.jednostka_miary))
        print('cena jednostkowa: '+str(self.cena_jed))
    def ile_produktu(self):
        return str(self.ilosc)+' '+str(self.jednostka_miary)
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

obiekt = NaZakupy('Pieczarka z Mozabiku', 2.5, 'kg', 250)
obiekt.wyswietl_produkt()
print('ile powinno być produktu: '+obiekt.ile_produktu())
print('ile kosztuje produkt: '+str(obiekt.ile_kosztuje())+' PLN')
