
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome 
        self.idade = idade 
        self.endereco = endereco
        
class Endereco: 
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado 
        
        
nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
cidade = str(input('Digite a cidade: '))
estado = str(input('Digite o estado: '))

endereco = Endereco(cidade, estado)
p = Pessoa(nome, idade, endereco)

print(f'Meu nome é {p.nome}, tenho {p.idade} anos de idade, moro na cidade de {p.endereco.cidade} no estado {p.endereco.estado}')

    
    