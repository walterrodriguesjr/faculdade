

while True:
    try:
        x = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('Entre com um número válido!')
print(f'Você digitou o número {x}')