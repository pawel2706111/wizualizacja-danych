def wyraz(a1, q, n):
    return a1 * q**(n-1)

def suma(a1, q, n):
    if(a1 != 1 ):
        return (a1*(1-q**n))/(1-q)
    else:
        return n*a1
    