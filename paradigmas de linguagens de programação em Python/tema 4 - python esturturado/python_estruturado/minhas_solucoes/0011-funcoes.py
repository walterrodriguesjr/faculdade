def ehPar(n):
    r = n % 2 == 0
    return r


def pares(lista):
    soma = 0
    for l in lista: 
        if ehPar(l):
            soma += l
    return soma




lista = [10, 2, 5, 7, 6, 3] 
p = pares(lista)
print(p)