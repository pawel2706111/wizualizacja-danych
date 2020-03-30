def urojona(liczba):
    liczba = complex(liczba)
    jednostka_urojona = False
    czesc_urojona = []
    for i in range(-1, -len(str(liczba))-1, -1):
        if(jednostka_urojona == True):
            czesc_urojona.append(str(liczba)[i])
            if(str(liczba)[i] == '-' or str(liczba)[i] == '+'):
                jednostka_urojona = False
        if(str(liczba)[i] == 'j'):
            jednostka_urojona = True
    del jednostka_urojona
    for i in range(0, len(czesc_urojona)//2, 1):
        temp = czesc_urojona[len(czesc_urojona)-1-i]
        czesc_urojona[len(czesc_urojona)-1-i] = czesc_urojona[i]
        czesc_urojona[i] = temp
    x = ''.join(czesc_urojona)
    del czesc_urojona
    return float(x)

def rzeczywista(liczba):
    liczba = complex(liczba)
    jednostka_urojona = False
    koniec_urojonej = False
    for i in range (-1, -len(str(liczba)) - 1, -1):
        if((str(liczba))[i] == 'j'):
            jednostka_urojona = True
        if(jednostka_urojona == True and i != -len(str(liczba)) and (str(liczba)[i] == '+' or str(liczba)[i] == '-')):
            koniec_urojonej = True
        if(koniec_urojonej == False and i == -len(str(liczba))):
            return 0.0
    czesc_rzeczywista = []
    i = 1
    while(i == 1 or ((str(liczba))[i] != '+' and (str(liczba))[i] != '-')):
        czesc_rzeczywista.append(str(liczba)[i])
        i = i + 1
    x = ''.join(czesc_rzeczywista)
    del czesc_rzeczywista
    return float(x)