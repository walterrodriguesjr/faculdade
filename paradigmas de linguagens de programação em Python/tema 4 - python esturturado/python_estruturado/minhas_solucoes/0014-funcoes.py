def calculaImc(peso, altura):
    result = peso / (altura* altura)
    print('O seu peso atual é: {:.2f}'.format(peso))
    print('A sua altura atual é: {:.2f}'.format(altura))
    print('O seu IMC atual é: {:.2f}'.format(result))

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

print('entrou na função')
resultado = calculaImc(peso, altura)
print('saiu da função')

