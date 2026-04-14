class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def exibir_info(self):
        return f"[GERAL] {self.nome} - Estoque: {self.quantidade}"


class ProdutoPerecivel(Produto):
    def exibir_info(self):
        return f"[PERECÍVEL] {self.nome} - Quantidade: {self.quantidade} unidades (Verificar validade!)"


class ProdutoDigital(Produto):
    def exibir_info(self):
        return f"[DIGITAL] {self.nome} - Acesso imediato para {self.quantidade} usuário(s)"

produtos = [
    ProdutoPerecivel("Leite", 5),
    ProdutoDigital("Curso Python", 1),
    Produto("Parafuso", 100) 
]

for p in produtos:
    print(p.exibir_info())