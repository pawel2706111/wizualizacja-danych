# zadanie 11
# Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.
def bonifacy():
    a = 0
    b = 1
    while a > -1:
        b += a
        a = b-a
        yield b-a

ciag = bonifacy()
for i in range(0, 5, 1):
    print('ciag('+str(i)+') =', next(ciag))