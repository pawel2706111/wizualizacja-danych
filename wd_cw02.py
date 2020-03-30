# zadanie 1
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje.
# Wynik wyświetla na ekranie (użyj instrukcji input)
import sys

def zadanie_1():
    print("Podaj zdanie byku: ")
    napis =  sys.stdin.readline()
    print('w podanym napisie spacja pojawia się:', napis.count(' '))

# zadanie 2
# Napisz skrypt, który pobiera od użytkownika dwie wartości i
# mnoży je przez siebie. Wynik wyświetla
# na ekranie (użyj instrukcji readline() i write()).
def zadanie_2():
    print('podaj pierwszą liczbe:')
    liczba_1 = sys.stdin.readline()
    print('podaj drugą liczbe:')
    liczba_2 = sys.stdin.readline()
    sys.stdout.write('wynik: '+str(float(liczba_1)*float(liczba_2)))

# zadanie 3
# Odszukaj w dokumentacji, jakie operatory można używać w instrukcjach warunkowych
# (np. równe, różne, mniejsze bądź równe itp.)
def zadanie_3():
    print('Lista operatorów w instrukcjach warunkowych')
    print('Równe: a == b')
    print('Różne: a != b')
    print('Mniejsze: a < b')
    print('Mniejsze bądź równe: a <= b')
    print('Większe: a > b')
    print('Większe bądź równe: a >= b')

# zadanie 4
# Napisz skrypt, który pobiera od użytkownika liczbę 
# i wypisuje na ekran wartość bezwzględną tej liczby
def zadanie_4():
    liczba = int(input('podaj liczbe calkowitą: '))
    if liczba >= 0:
        print('|', liczba, '| = ', liczba, sep='')
    else:
        print('|', liczba, '| = ', liczba*(-1), sep='')

# zadanie 5
# Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:
# czy a zawiera się w przedziale (0,10> oraz czy jednocześnie a>b lub b>c. 
# Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.
def zadanie_5():
    a = int(input('Podaj liczbę całkowitą a: '))
    b = int(input('Podaj liczbę całkowitą b: '))
    c = int(input('Podaj liczbę całkowitą c: '))
    if a > 0 and a <= 10:
        print('warunek a należy do (0,10> - spełniony')
    else:
        print('warunek a należy do (0,10> - NIE spełniony')
    if a > b or b > c:
        print('warunek a > b lub b > c - spełniony')
    else:
        print('warunek a > b lub b > c - NIE spełniony')

# zadanie 6
# Napisz pętlę, która wyświetla liczby podzielne przez 5
def zadanie_6():
    print('liczby podzielne przez 5: ')
    for licznik in range (0, 1001, 5):
        print(str(licznik), end=' ')

# zadanie 7
# Napisz pętle, która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie.
def zadanie_7():
    lista = []
    for licznik in range(1, 6, 1):
        liczba = input('podaj '+str(licznik)+' liczbe: ')
        lista.append(int(liczba))
    for licznik in range(0, 5, 1):
        print(str(lista[licznik])+'^2 = '+str(lista[licznik]**2))
        
# zadnie 8
# Napisz skrypt, który odczytuje liczby od użytkownika 
# i umieszcza je na liście. Wykorzystaj pętle while.
def zadanie_8():
    lista = []
    i = 0
    while i < 5:
        liczba = input('podaj liczbę całkowitą: ')
        lista.append(int(liczba))
        i += 1
    print(lista)

# zadanie 9
# Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry. 
# Wynik wyświetla na ekranie. Wykorzystaj pętle while.
def zadanie_9():
    liczba = int(input('Podaj liczbę całkowitą wielocyfrową: '))
    suma = 0
    while(liczba != 0):
        suma = suma + liczba % 10
        liczba = liczba // 10
    print('suma cyfr podanej liczby = '+str(suma))

# zadanie 10
# Napisz skrypt, który rysuje wieżę z literek. Użytkownik podaje wysokość wieży ale nie więcej jak 10.
# A
# AA
# AAA
# AAAA
# AAAAA
# AAAAAA
def zadanie_10():
    for i in range(0, 6, 1):
        for j in range(0, i+1, 1):
            print('A', end='')
        print()

# zadanie 11
# Napisz skrypt, który rysuje diament. Użytkownikpodaje wysokość nie mniej jak 3 i nie więcej jak 9
# np. wysokość = 3
#  o
# ooo
#  o
# wysokość równa 5
#   o
#  ooo
# ooooo
#  ooo
#   o
# itd.
def zadanie_11():
    h = 0
    while(h < 3 or h > 9):
        print('!!! wysokość musi być nie mniejsza niż 3 i nie większa od 9 !!!')
        h = int(input('podaj wysokość: '))
    h_parzysta = False
    if(h % 2 == 0):
        h_parzysta = True
        h = h - 1
    spacje = h // 2
    kule = 1
    for i in range (0, h // 2, 1):
        for j in range (0, spacje, 1):
            print(' ',end='')
        spacje = spacje - 1
        for j in range (0, kule, 1):
            print('O',end='')
        kule = kule + 2
        print()
    ###################################
    for i in range (0, h, 1):
        print('O', end='')
    print()
    if(h_parzysta == True):
        for i in range (0, h, 1):
            print('O', end='')
        print()
    ###################################
    spacje = 1
    kule = h - 2
    for i in range (0, h // 2, 1):
        for j in range (0, spacje, 1):
            print(' ',end='')
        spacje = spacje + 1
        for j in range (kule, 0, -1):
            print('O',end='')
        kule = kule - 2
        print()

# zadanie 12
# Napisz skrypt, który wyświetla i oblicza tabliczkę mnożenia od 1 do 100
def zadanie_12():
    print('|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|')
    print('|  *  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |')
    print('|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|')
    for i in range (1, 11, 1):
        if(len(str(i)) == 1):
            print('|  '+str(i)+'  |',end='')
        else:
            print('|  '+str(i)+' |',end='')
        for j in range (1, 11, 1):
            liczba = int(i)*int(j)
            #######
            if len(str(liczba)) == 1:
                print('  '+str(liczba)+'  |', end='')
            elif len(str(liczba)) == 2:
                print('  '+str(liczba)+' |', end='')
            else:
                print(' '+str(liczba)+' |', end='')
            #######
        print()
        print('|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|')

# zadanie 13
# Przestudiuj inne błędy jakie mogą się pojawić w trakcie działania programu

# zadanie 14
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika
# jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd
import math

def zadanie_14():
    liczba = float(input('podaj liczbę rzeczywistą nieujemną: '))
    try:
        wynik = math.sqrt(liczba)
        print('2  ',end='')
        for i in range (0, len(str(liczba)), 1):
            print('_',end='')
        print()
        print(' \/'+str(liczba)+' = '+str(wynik))
    except ValueError:
        print('Nie można obliczyć pierwiastka kwadratowego z liczby rzeczywistej ujemnej!')

# zadanie 15
# Napisz skrypt, w którym użytkownik ma podać liczbę 
# i który będzie wyłapywał błąd gdy użytkownik poda literę zamiast cyfry.
def zadanie_15():
    try:
        liczba = float(input('podaj liczbę: '))
        print('Gratuluję! Udało Ci się wprowadzić bezbłędnie liczbę')
    except:
        print('Nie udało Ci się wprowadzić poprawnie liczby')