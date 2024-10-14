qnt = int(input('Informe quantos itens irá comprar: '))
cont = 0
valorUnitario = 10

for item in range(1, qnt + 1):
    cont += 1
    print(cont)
if cont > 20:
    print('Você comprou a quantidade de {} produtos.'.format(cont))
    total = valorUnitario * qnt
    desc = 0.2 * total
    final = total - desc
    print('O valor total com desconto foi de: R${:.2f}'.format(final))
    print('O seu desconto é de: 20%.')
elif cont <= 20 and cont >= 11:
    print('Você comprou a quantidade de {} produtos.'.format(cont))
    total = valorUnitario * qnt
    desc = 0.1 * total
    final = total - desc
    print('O valor total com desconto foi de: R${:.2f}'.format(final))
    print('O seu desconto é de: 10%.')
else:
    print('Você comprou a quantidade de {} produtos.'.format(cont))
    total = valorUnitario * qnt
    print('O valor total foi de: R${:.2f}'.format(total))
    print('Você não teve desconto por que comprou 10 produtos ou menos')
