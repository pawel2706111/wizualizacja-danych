# zadanie 2
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.
plik = open('zadanie_1.txt', 'r')
liczby = plik.readlines()
plik.close()
for i in range (0, len(liczby), 1):
    print((liczby[i].split('\n'))[0], end=' ')