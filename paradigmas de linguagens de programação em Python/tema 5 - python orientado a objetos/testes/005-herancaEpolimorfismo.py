class Veiculo: 
    def rodar(self):
        print("Frase 1 da class Veículo.")
        
    def freiar(self):
        print('Frase 2 da class Veiculo.')
        
class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().freiar()
        print('Frase 1 da class VeiculoEletrico')
        
objeto = VeiculoEletrico()
objeto.rodar()