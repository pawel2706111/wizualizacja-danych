# zadanie 1
# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
plik = open('zadanie_1.txt', 'w')
for i in range(0, 1000, 1):
    plik.write(str(i*4)+'\n')
plik.close()