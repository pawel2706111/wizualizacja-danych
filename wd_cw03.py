# zadanie 1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A={1/x: x należy do <1,10>}
# B={1, 2, 4, 8,..., 2^10}
# C={x: x należy do B i x jest liczbą podzielną przez 4}
def zadanie_1():
    A = [1/x for x in range (1, 11, 1)]
    B = [2**x for x in range(0, 11, 1)]
    C = [x for x in B if(x % 4 == 0)]
    print(A)
    print(B)
    print(C)

# zadanie 2
# Wygeneruj losowo macierz 4x4 i wykorzystując Python Comprehension
# zdefiniuj listę, która będzie zawierała tylko elementy
# znajdujące się na przekątnej.
import random

def zadanie_2():
    macierz = [[random.randint(0, 9) for j in range (0, 4, 1)] for i in range (0, 4, 1)]
    przekatna = [macierz[i][j] for i in range (0, 4, 1) for j in range (0, 4, 1) if i == j]
    print('Macierz:')
    print(macierz[0])
    print(macierz[1])
    print(macierz[2])
    print(macierz[3])
    print('Przekątna: ',przekatna)

# zadanie 3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie 
# nazwa produktu a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy,
# gdzie będą produkty, których wartość to sztuki.
def zadanie_3():
    produkt_jednostka = {
        'mięso': 'kg',
        'papierosy': 'opakowanie',
        'wódka': 'flaszka',
    }
    jednostka_produkt = {value: key for key, value in produkt_jednostka.items()}
    print('Oryginalny słownik:')
    print(produkt_jednostka)
    print('Odwrócony słownik:')
    print(jednostka_produkt)

# zadanie 4
# Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej:
# y = a x + b
# Funkcja jest rosnąca gdy a>0
# malejąca jeżeli a<0
# stała gdy a=0
# i w zależności od tego będzie wyświetlać odpowiedni komunikat
def monotonicznosc(a):
    if(a>0):
        return 'rosnąca'
    if(a<0):
        return 'malejąca'
    if(a==0):
        return 'stała'

def zadanie_4():
    print('y = ax + b')
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    print('Funkcja y = '+str(a)+'x + '+str(b)+' jest '+str(monotonicznosc(a)))

# zadanie 5
# Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe:
# Proste dane równaniami y= a1x + b1, y= a2x + b2, są
# równolegle gdy a1 = a2
# prostopadłe gdy a1 * a2 = -1
def proste_czy_rownolegle(a1, a2):
    if(a1 == a2):
        return 'równoległe'
    if(a1*a2 == -1):
        return 'prostopadłe'
    else:
        return 'ani równoległe ani prostopadłe'

def zadanie_5():
    print('y = ax + b')
    a1 = float(input('Podaj a1: '))
    b1 = float(input('Podaj b1: '))
    a2 = float(input('Podaj a2: '))
    b2 = float(input('Podaj b2: '))
    print('y1 = '+str(a1)+'x + '+str(b1))
    print('y2 = '+str(a2)+'x + '+str(b2))
    print('Proste y1 i y2 są '+str(proste_czy_rownolegle(a1, a2)))

# zadanie 6
# Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość promienia.
# Funkcja ma przyjmować argumenty domyślne:
# Równanie okręgu dane jest wzorem:
# (x-a)^2 + (y-b)^2 = r^2
# gdzie (a,b) to środek okręgu a r to promień okręgu.
def okrag(a = 0, b = 0, x = 0, y = 0):
    return ((x-a)**2 + (y-b)**2)**0.5

def zadanie_6():
    print('Współrzędne środka okręgu to (a,b)')
    a = input('Podaj współrzędną a: ')
    b = input('Podaj współrzędną b: ')
    print('Do okręgu należy punkt o współrzędnych (x,y)')
    x = input('Podaj współrzędną x: ')
    y = input('Podaj współrzędną y: ')
    print('Promień okręgu ma długość równą:',okrag(float(a), float(b), float(x), float(y)))

# zadanie 7
# Zdefiniuj funkcję, któraoblicza długość przeciwprostokątnej,
# wykorzystując twierdzenie pitagorasa.
# Proszę podać wartości domyślne dla funkcji
def pitagoras(a = 0, b = 0):
    return (a**2 + b**2)**0.5

def zadanie_7():
    a = float(input('Podaj dłguość pierwszej przyprostokątnej: '))
    b = float(input('Podaj dłguość drugiej przyprostokątnej: '))
    print('Długość przeciwprostokątnej wynosi: '+str(pitagoras(a,b)))
    
# zadanie 8
# Zdefiniuj funkcję, która zwraca sumę dowolnego ciągu arytmetycznego.
# Funkcja niech przyjmuje jako parametry: 
# a1 (wartość początkowa),
# r (wielkość o ile rosną kolejne elementy)
# i ile_elementów (ile elementów ma sumować). 
# Ponadto funkcja niech przyjmuje wartości domyślne: a1= 1, r=1, ile=10.
def ciag_suma(a1 = 1, r = 1, ile = 10):
    return ile * ((2*a1) + (ile-1)*r) / 2

def zadanie_8():
    a1 = float(input('Podaj a1: '))
    r = float(input('Podaj r: '))
    ile = int(input('Podaj ile: '))
    print('suma = ',str(ciag_suma(a1, r, ile)))

# zadanie 9
# Wykorzystując poprzedni przykład zdefiniuj funkcję,
# która będzie liczyć iloczyn elementów ciągu.
def iloczyn_ciagu(* liczby):
    if(len(liczby) == 0):
        return 0.0
    else:
        iloczyn = 1.0
        for i in liczby:
            iloczyn = iloczyn * i
        return iloczyn

def zadanie_9():
    print('iloczyn dla ciągu bez elementów:', iloczyn_ciagu())
    print('iloczyn dla ciągu 1,2,3,4:', iloczyn_ciagu(1,2,3,4))
    print('iloczyn dla ciągu 1,2,3.2,4.23,5,6,7.51:', iloczyn_ciagu(1,2,3.2,4.23,5,6,7.51))

# zadanie 10
# Napisz funkcję, która wykorzystuje symbol **.
# Funkcja ma przyjmować listę zakupów  w postaci:
# klucz to nazwa produktu  a wartość to ilość. 
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać tę wartość.
def ilosc_produnktow(**lista_zakupow):
    suma = 0.0
    for i in lista_zakupow:
        suma = suma + float(lista_zakupow[i])
    return suma

def zadanie_10():
    print('liczba wszystkich produktów:', ilosc_produnktow(herbata_lipton=2,zeszyt_A4=5,
          woda_mineralna=6, sok_owocowy=3, coca_cola_1_5L=1, banany=7))

# zadanie 11
# Stwórz pakiet liczby zespolone z dwoma modułami.
# Jeden moduł ma zawierać dwie funkcje, które z podanej liczby zespolonej
# zwracają część rzeczywistą i część urojoną.
# Drugi moduł ma wykonywać dodawanie i odejmowanie dwóch liczb zespolonych.
# Przetestuj działanie tego pakietu.
from wd_cw03_liczby_zespolone import *

def zadanie_11():
    liczba = 1+1j
    print('Liczba: '+str(liczba))
    print('część rzeczywista: '+str(lz_postac.rzeczywista(liczba)))
    print('część urojona: '+str(lz_postac.urojona(liczba)))
    print('liczba1 = 1+2j, liczba2 = -23+1j')
    liczba1 = 1+2j
    liczba2 = -23+1j
    print('liczba 1 + liczba 2 = '+str(lz_operacje.lz_dodawanie(liczba1, liczba2)))
    print('liczba 1 - liczba 2 = '+str(lz_operacje.lz_odejmowanie(liczba1, liczba2)))

# zadanie 12
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań 
# i wzorów związanych z ciągami arytmetycznymi
# a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.
from wd_cw03_ciagi import *

def zadanie_12():
    print('ciąg arytmetyczny: a1 = 1, r = -1, n=21')
    print('a(21) = '+str(ciag_arytmetyczny.wyraz(1, -1, 21)))
    print('suma:'+str(ciag_arytmetyczny.suma(1, -1, 21)))
    print('ciąg geometryczny: a1 = 1, q = 0.22, n=5')
    print('a(5) = '+str(ciag_geometryczny.wyraz(1, 0.22, 5)))
    print('suma: '+str(ciag_geometryczny.suma(1, 0.22, 5)))