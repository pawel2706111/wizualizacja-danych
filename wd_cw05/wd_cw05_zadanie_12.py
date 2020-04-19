# zadanie 12
# Za pomocą wyrażenia generującego stwórz
# generator zwracający polskie nazwy miesięcy.
def miesiace():
    lista_miesiecy = ['styczeń', 'luty', 'marzec', 'kwiecień',
                     'maj', 'czerwiec', 'lipiec', 'sierpień',
                     'wrzesień', 'październik', 'listopad', 'grudzień']
    for i in range(0, 12, 1):
        yield lista_miesiecy[i]

gen = miesiace()
for i in range(0, 12, 1):
    print(next(gen))