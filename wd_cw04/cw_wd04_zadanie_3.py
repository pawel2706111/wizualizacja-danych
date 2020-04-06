# zadanie 3
# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku
# a następnie wyświetl je na ekranie.
with open('zadanie_3.txt', 'w') as plik:
    for i in range(1, 6, 1):
        plik.write(str(i)+'\n')
with open('zadanie_3.txt', 'r') as plik:
    for linia in plik:
        print(linia.split('\n')[0], end=' ')