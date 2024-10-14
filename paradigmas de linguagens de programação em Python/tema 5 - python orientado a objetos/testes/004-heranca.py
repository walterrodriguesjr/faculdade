class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 
        
    def somar(self):
        return self.a + self.b
    
    def multiplicar(self): 
        return self.a * self.b 
    
class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a - self.b
    
    def dividir(self):
        return self.a / self.b 

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
objeto = Derivada(num1 , num2)

print(f'A soma entre num1 + num2 é: {objeto.somar()}')
print(f'A subtração entre num1 - num2 é: {objeto.subtrair()}')
print(f'A multiplicação entre num1 * num2 é: {objeto.multiplicar()}')
print(f'A divisão entre num1 / num2 é: {objeto.dividir()}')


    
    
    
        