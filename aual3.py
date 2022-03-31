class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def add_produtos(self, produto):
        self.produtos.append(produto)

    def list_produtos(self):
        for p in self.produtos:
            print(p.nome, p.preco)

    def calc_prod(self):
        soma = 0
        for p in self.produtos:
            soma += p.preco
        print("Total: ", soma)

cliente1 = Cliente("Jão")

produto1 = Produtos("Pen Drive", 30)
produto2 = Produtos("HD Externo", 500)
produto3= Produtos("Celular", 1400)

carrinho1 = Carrinho(cliente1)
carrinho1.add_produtos(produto1)
carrinho1.add_produtos(produto1)
carrinho1.add_produtos(produto3)

carrinho1.list_produtos()
carrinho1.calc_prod()