from models.produtos import Produto

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade):
        if quantidade < 0:
            return "Erro: A quantidade não pode ser negativa."
            
        novo_produto = Produto(nome, quantidade)
        self.produtos.append(novo_produto)
        return "Produto adicionado com sucesso!"

    def listar_produtos(self):
        return [p.to_dict() for p in self.produtos]

servico_estoque = Estoque()