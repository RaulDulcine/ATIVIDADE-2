class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def to_dict(self):
        return {"nome": self.nome, "quantidade": self.quantidade}

from models.produtos import Produto 

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade):
        novo = Produto(nome, quantidade)
        self.produtos.append(novo)
        return "Adicionado"

    def listar(self):
        return [p.to_dict() for p in self.produtos]

servico_estoque = Estoque() 

from services.estoque import servico_estoque

def executar_rota(rota, metodo, dados=None):
    dados = dados or {}
    if rota == "/produtos" and metodo == "GET":
        return servico_estoque.listar()
    
    if rota == "/produtos" and metodo == "POST":
        return servico_estoque.adicionar_produto(dados.get("nome"), dados.get("quantidade"))
    
    return "Rota não encontrada"

print(executar_rota("/produtos", "POST", {"nome": "Pizza", "quantidade": 10}))
print(executar_rota("/produtos", "GET"))


def executar_rota(rota, metodo, dados=None):
    dados = dados or {}

    if rota == "/produtos" and metodo == "GET":
        return get_produtos()

    if rota == "/produtos" and metodo == "POST":
        nome = dados.get("nome")
        quantidade = dados.get("quantidade")
        
        if not nome or quantidade is None:
            return {"erro": "Dados incompletos. 'nome' e 'quantidade' são obrigatórios."}, 400
        
        return post_produto(nome, quantidade)

    if rota == "/produtos/buscar" and metodo == "GET":
        nome = dados.get("nome")
        
        if not nome:
            return {"erro": "O parâmetro 'nome' é obrigatório para a busca."}, 400
            
        return get_produto_por_nome(nome)

    return {"erro": f"Rota '{rota}' com método '{metodo}' não encontrada."}, 404