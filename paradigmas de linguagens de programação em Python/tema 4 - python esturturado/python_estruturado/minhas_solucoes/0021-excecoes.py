def dividir(x, y):
    try:
        resultado = x / y 
        print(f'O resultado da divisão é: {resultado:.0f}')
    except ZeroDivisionError:
        print('Divisão por zero!')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
dividir(num1, num2)