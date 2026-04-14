from services.estoque import servico_estoque

def get_produtos():
    return servico_estoque.listar_produtos()

def post_produto(dados):
    nome = dados.get("nome")
    quantidade = dados.get("quantidade")
    
    if nome is None or quantidade is None:
        return "Erro: Dados incompletos (nome e quantidade são obrigatórios)."
        
    return servico_estoque.adicionar_produto(nome, quantidade)

def executar_rota(rota, metodo, dados=None):
    if rota == "/produtos":
        if metodo == "GET":
            return get_produtos()
        elif metodo == "POST":
            return post_produto(dados)
            
    return "Rota não encontrada"

if __name__ == "__main__":
    print(executar_rota("/produtos", "POST", {"nome": "Pizza", "quantidade": 10}))
    
    print(executar_rota("/produtos", "POST", {"nome": "Coxinha", "quantidade": -2}))
    
    print(f"Lista de estoque: {executar_rota('/produtos', 'GET')}")