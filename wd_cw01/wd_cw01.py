# zadanie 1
# Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu
# a następnie wyświetl te zmienne
def zadanie_1():
    int_1 = 10
    int_2 = 123456789
    float_1, float_2 = 3.1415, -0.121
    complex_1 = 1 + 1j
    complex_2 = 2 - 3j
    string_1 = 'jakiś sobie łańcuch znaków'
    string_2 = 'xdddd'
    print('int:', int_1, int_2)
    print('float:', float_1, float_2)
    print('complex:', complex_1, complex_2)
    print('string:', string_1, string_2)

# zadanie 2
# Stwórz skrypt kalkulator, wktórym wykorzystać wszystkie 
# podstawowe działania arytmetyczne
def zadanie_2():
    a=20
    b=8
    print('dodawanie:', a, '+', b, '=', a+b)
    print('odejmowanie:', a, '-', b, '=', a-b)
    print('mnożenie:', a, '*', b, '=', a*b)
    print('dzielenie:', a, '/', b, '=', a/b)
    print('dzielenie calkowite:', a, '//', b, '=', a//b)
    print('reszta z dzielenia:', a, '%', b, '=', a%b)
    print('potegowanie:', a, 'do potegi', b, '=', a**b)
    print('potegowanie:', a, 'do potegi', b, '=', pow(a,b))

# zadanie 3
# Napisz skrypt, w którym stworzysz operatory przyrostkowe 
# dla operacji: +, -, *, /, **, %
def zadanie_3():
    print('a = 5')
    a = 5
    a += 7
    print('a += 7:', a)
    a = 5
    a -= 7
    print('a -= 7:', a)
    a = 5
    a *= 7
    print('a *= 7:', a)
    a = 5
    a /= 7
    print('a /= 7:', a)
    a = 5
    a **= 7
    print('a **= 7:', a)
    a = 5
    a %= 7
    print('a %= 7:', a)

# zadanie 4
# Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
from math import *

def zadanie_4():
    print('e do potegi 10 = ', pow(e, 10))
    print('(ln(5+sin^2(8)))^(1/6) = ', pow( log(5 + pow(sin(8), 2)), 1/6))
    print('⌊3,55⌋ = ', floor(3.55))
    print('⌈4,80⌉ = ', ceil(4.80))

# zadanie 5
# Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie 
# wielkimi literami. Użyj odpowiedniej metody by wyświetlić je 
# pisane tak, że pierwsza litera jest wielka a pozostałe małe.
# (trzeba użyć metody capitalize)
def zadanie_5():
    imie = 'Paweł'
    nazwisko = 'Tracz'
    print(str.capitalize(imie), str.capitalize(nazwisko))

# zadanie 6
# Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu 
# piosenki z powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji,
# która zliczy występowanie słowa „la”. (trzeba użyć metody count)
def zadanie_6():
    piosenka = 'la la la la la la la la la la'
    print('"la" powtarza sie', piosenka.count('la'), 'razy')

# zadanie 7
# Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
def zadanie_7():
    napis = 'jakiś tekst'
    print('napis =', napis)
    print('napis[1] =', napis[1])
    print('napis[1] =', napis[-1])

# zadanie 8
# Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6
# i spróbuj ją podzielić na poszczególne wyrazy.(trzeba użyć metody split)
def zadanie_8():
    piosenka = 'la la la la la la la la la la'
    print(str.split(piosenka))

# zadanie 9
# Napisz skrypt, w którym zadeklarujesz zmienne typu: 
# string, float i szestnastkowe. 
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.
def zadanie_9():
    z_string = 'tekst'
    z_float = 243
    z_hexdec = hex(255)
    print('string: %(zm)s' % {'zm': z_string})
    print('float: %(zm)f' % {'zm': z_float})
    print('szestnastkowe: %(zm)s' % {'zm': z_hexdec})

# zadanie 10
# Napisz skrypt, w którym tworzysz listę ulubionych filmów i posortuj ją.
def zadanie_10():
    filmy = [
        'Bułgarska libacja alkoholowa Pata i Mata',
        'O dwóch takich Czechosłowakach', 'Gone in 60 Pats',
        'Wejście Pata', 'Czechosłowacki Poker', 'Matlands'
    ]
    print('Lista filmów przed posortowaniem:\n', filmy)
    filmy.sort()
    print('Lista filmów po posortowaniu:\n', filmy)

# zadanie 11
# Napisz skrypt, który generuje tabelkę 
# z podstawowymi wartościami funkcji trygonometrycznych.
# Wskazówka -> wykorzystaj listy i funkcje matematyczne
def zadanie_11():
    tabelka = [
        ['kat', '0', '30', '45', '60', '90'],
        ['sin', sin(0), sin(30), sin(45), sin(60), sin(90)],
        ['cos', cos(0), cos(30), cos(45), cos(60), cos(90)],
        ['tan', tan(0), tan(30), tan(45), tan(60), tan(90)]
    ]
    print(tabelka[0])
    print(tabelka[1])
    print(tabelka[2])
    print(tabelka[3])

# zadanie 12
# Napisz skrypt, gdzie w jednej zmiennej zapiszesz 
# dowolnie długie zdanie (co najmniej 5 wyrazów) 
# a następnie podziel te zdanie na wyrazy tak by zostały zapisane w liście
def zadanie_12():
    napis = 'to jest jakieś głupie nic nie znaczące zdanie xdddddd'
    lista_slow = str.split(napis)
    print(napis)
    print(lista_slow)

# zadanie 13
# Stwórz słownik, gdzie zapiszesz imiona i nazwiska swoich znajomych 
# jako klucz proszę użyć ich przezwisk (10 elementów).
# Następnie wyświetl kilka danych odwołując się do elementów przez klucz.
def zadanie_13():
    znajomi = {
        'Pat': ['Pat', 'Czechosłowak'],
        'Mat': ['Mat', 'Czechosłowak'],
        'Czaro': ['Cezary', 'Psikuta'],
        'Czarek': ['Cezary', 'Cezary'],
        'Cdżdzej': ['Karol', 'Jankowski'],
        'Wielki Dym': ['Big', 'Smoke'],
        'Białek': ['Michael', 'Proteina'],
        'Chmielu': ['Piotr', 'Ryszardowy'],
        'Cousine': ['Niko', 'Belic'],
        'Mati': ['Matthew', 'McConaughey'],
    }
    print(znajomi['Pat'])
    print(znajomi['Mati'])
    print(znajomi['Cdżdzej'])

# zadanie 14
# Stwórz słownik skrótów powszechnie używanych w smsach.
# Jako klucz niech będzie skrót a jako wartość zdanie.
# Skopiuj słownik do innego słownika
def zadanie_14():
    slownik_skroty_sms = {
        'LOL': 'Laughing out loud',
        'b4': 'before',
        'AFAIK': 'As far as I know',
        'BTW': 'By the way',
        'IMO': 'In my opinion',
        'MD': 'Miłego dnia',
        'OMG': 'Oh my God',
        'THX': 'Thanks',
    }
    slownik = {
        'skróty sms': slownik_skroty_sms,
    }
    print(slownik['skróty sms']['LOL'])
    print(slownik['skróty sms']['AFAIK'])
    print(slownik['skróty sms']['MD'])

# zadanie 15
# Stwórz słownik, z cyframi rzymskimi. Wybierz klucz i wartość.
def zadanie_15():
    cyfry_rzymskie = {
        'I': 1, 'II': 2, 'III': 3,
        'IV': 4, 'V': 5, 'VI': 6,
        'VII': 7, 'VIII': 8, 'IX': 9,
        'X': 10, 'XI': 11, 'XII': 12,
        'XIII': 13, 'XIV': 14, 'XV': 15,
        'XVI': 16, 'XVII': 17, 'XVIII': 18,
        'IXX': 19, 'XX': 20, 'XXI': 21,
        'XXII': 22, 'XXIII': 23, 'XXIV': 24,
        'XXV': 25, 'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    print(cyfry_rzymskie)

# zadanie 16
# Stwórz słownik z ulubionymi grami komputerowymi.
# Pomyśl, co może być kluczem a co wartością w takim słowniku.
# Policz liczbę elementów w słowniku.
def zadanie_16():
    ulubione_gry = {
        'GTA SA': 'Grand Theft Auto: San Andreas',
        'GTA VC': 'Grand Theft Auto: Vice City',
        'GTA IV': 'Grand Theft Auto IV',
        'GTA V': 'Grand Theft Auto V',
        'COD': 'Call Of Duty',
        'COD2': 'Call Of Duty 2',
        'COD MW': 'Call Of Duty Modern Warfare',
        'COD BO': 'Call Of Duty Black Ops',
        'BF: BC2': 'Battlefield: Bad Company 2',
        'SC2': 'StarCraft 2',
        'TW3TWH' : 'The Witcher 3: Wild Hunt',
    }
    print('liczba moich ulubionych gier:', len(ulubione_gry))