import random
import pandas as pd



def gerar_dados_pedidos():
    num_pedidos_gerados = random.randint(0,10)
    pedidos = []
    itens_pedido =[]

    produtos = pd.read_csv(r"files/output/produtos.csv")
    produtos = produtos.iloc[:, 0].tolist()

    clientes = pd.read_csv(r"files/output/clientes.csv")
    clientes = clientes.iloc[:, 0].tolist()

    enderecos = pd.read_csv(r"files/output/enderecos.csv")
    enderecos = produtos.iloc[:, 0].tolist()


    for i in range(1, num_pedidos_gerados+1):
        if num_pedidos_gerados > 0 :
            num_itens_pedidos = random.randint(0,5)
            lista_itens_pedido = random.sample(produtos, num_itens_pedidos)
            
            pedidos.append({
                "ID_CLIENTE" :
                "ID_PRODUTO" :
                "METODO_PAGAMENTO" :
                "NUM_PARCELAS" :
                "DATA_PEDIDO" :
            })


            for j in (lista_itens_pedido):
                itens_pedido.append({
                    "ID_PEDIDO": i, # Alterar para buscar no banco
                    "ID_PRODUTO": j,
                    "QUANTIDADE": random.randint(1,3)
                })