def calcPrimo(numDigitado):
    cont = 0
    for n in range(1, numDigitado+1):
        if numDigitado % n == 0:
            cont += 1 
    if cont == 2: 
        print('O número {} é primo.'.format(numDigitado))
    else: 
        print('O número {} NÃO é primo.'.format(numDigitado))
        


numDigitado = int(input('Digite um número: '))
n = calcPrimo(numDigitado)