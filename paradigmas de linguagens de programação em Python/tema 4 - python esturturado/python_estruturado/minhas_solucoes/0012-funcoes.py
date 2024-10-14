from math import factorial


def calcFatorial(numDigitado):
    s = factorial(numDigitado)
    print('O fatorial de {} é igual a {}'.format(numDigitado, s))

numDigitado = int(input('Digite um número: '))
n = calcFatorial(numDigitado)
