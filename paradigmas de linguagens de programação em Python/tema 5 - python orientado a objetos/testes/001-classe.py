class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender
    
pessoa1 = Pessoa("Maria", "rua 01234")


print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
