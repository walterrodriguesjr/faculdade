nota = float(input('Digite a nota do aluno: '))

if nota >= 7:
    print('Sua nota foi: {:.1f} . Parabéns, você foi APROVADO!'.format(nota))
elif nota < 7 and nota >= 5:
    print('Sua nota foi: {:.1f} . Você ficou de RECUPERAÇÃO.'.format(nota))
else:
    print('Sua nota foi {:.1f} . Você foi REPROVADO.'.format(nota))
