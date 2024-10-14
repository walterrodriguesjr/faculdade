class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome 
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro 
        
    def capacidade_assento(self, capacidade):
        print(f'A capacidade máxima de assentos do veículo é {self.nome} é {capacidade}.')
        
    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'velocidade_max = {self.velocidade_max}')
        print(f'quilometros percorridos por litro = {self.quilometro_litro}')
        
class Onibus(Veiculo):
    def capacidade_assento(self, capacidade):
        return super().capacidade_assento(capacidade)

modeloCarro = str(input('Qual modelo do carro? '))
velocidadeCarro = int(input('Qual a velocidade máxima? '))
litrosCarro = int(input('Quantos kilômetros ele faz por litro? '))
modeloOnibus = str(input('Qual modelo do Onibus? '))
velocidadeOnibus = int(input('Qual a velocidade máxima? '))
litrosOnibus = int(input('Quantos kilômetros ele faz por litro? '))
assentosOnibus = int(input('Quantos assentos? '))
modelo_carro = Veiculo(modeloCarro, velocidadeCarro, litrosCarro)
modelo_onibus = Veiculo(modeloOnibus, litrosOnibus, litrosOnibus)
modelo_carro.toStr()
modelo_onibus.toStr()
modelo_onibus.capacidade_assento(assentosOnibus)
        
        
        