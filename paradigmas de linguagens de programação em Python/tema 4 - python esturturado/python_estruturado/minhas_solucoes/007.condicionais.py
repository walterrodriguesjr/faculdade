lista = [10, 2, 5, 7, 6, 3]
cont = 0
for num in lista: 
    if num % 2 == 0: 
        cont += num
print('A soma dos números pares da lista é: {}'.format(cont))