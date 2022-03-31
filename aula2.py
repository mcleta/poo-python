class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.idade = idade
        self.nome = nome
        self.endereco = endereco

    def exibir_dados(self):
        print('Nome', self.nome)
        print('Idade', self.idade)
        print('Endereco', self.endereco)


class Endereco:
    def __init__(self, rua, num, cep):
        self.rua = rua
        self.num = num
        self.cep = cep

    def exibir_dados(self):
        print('Rua', self.rua)
        print('Nº', self.num)
        print('CEP', self.cep)


endereco1 = Endereco('Rua Lasvegan', 123, '1234-5556')
pessoa1 = Pessoa('Lavander Townwood', 20, endereco1)

pessoa1.exibir_dados()