
class Conta: 
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero 
        self.cpf = cpf 
        self.nomeTitular = nomeTitular 
        self.saldo = saldo 
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor 
        
    def gerarSaldo(self):
        print('+='*30)
        print(f'Número da Conta: {self.numero}')
        print(f'CPF: {self.cpf}')
        print(f'Nome do Titular: {self.nomeTitular}')
        print(f'Saldo Atual: {self.saldo}')
        print('+='*30)

numero = int(input('Digite o número da conta: '))
cpf = int(input('Digite o número do CPF: '))
nomeTitular = str(input('Digite o nome do titular da conta: '))
saldo = float(input('Digite o saldo inicial: '))

usuario = Conta(numero, cpf, nomeTitular, saldo)
resposta = ''

def repetir():
    repetir = str(input(f'Deseja fazer outra operação? [S/N]')).upper()
    if repetir == 'S':
        operacoes()

def operacoes():
    while True:
        resposta = int(input('Digite: 1 para depositar / 2 para sacar / 3 para ver o saldo / 4 para sair'))
        if resposta == 1:
            valor = int(input('Qual o valor do depósito? '))
            usuario.depositar(valor)
            print('+='*30)
            print(f'Você depositou a quantia de R${valor} com sucesso!')
            print('+='*30)
            repetir()
            break
        elif resposta == 2:
            valor = int(input('Qual o valor do saque? '))
            usuario.sacar(valor)
            print('+='*30)
            print(f'Você sacou a quantia de R${valor} com sucesso!')
            print('+='*30)
            repetir()
            break
        elif resposta == 3: 
            print('Seu saldo atual é de: ')
            usuario.gerarSaldo()
            repetir()
            break
        elif resposta == 4: 
            print('OPERAÇÃO FINALIZADA, VOLTE SEMPRE!')
            break
operacoes()


print('Seu saldo atualizado é de...')
usuario.gerarSaldo()

        