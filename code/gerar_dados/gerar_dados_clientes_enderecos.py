import random
import pandas as pd

def gera_dados_clientes_enderecos(num_clientes: int, num_enderecos: int):
    
    """
    Gera dados da tabela associativa clientes e endereços.

    Args:
        num_clientes (int): numero de clientes gerados.
        num_enderecos (int): numero de enderecos gerados.
    """
    dados_cliente_endereco = []

    for cliente_id in range(1, num_clientes + 1): # Percorre o número de clientes
        enderecos_cliente = random.sample(range(1, num_enderecos + 1), random.randint(1, num_enderecos)) # Escolher aleatoriamente quantos e quais endereços um cliente terá
        for endereco_id in enderecos_cliente:
            dados_cliente_endereco.append({ 
                "ID_CLIENTE": cliente_id,
                "ID_ENDERECO": endereco_id
            })
            

    df_cliente_endereco = pd.DataFrame(dados_cliente_endereco)
    df_cliente_endereco.to_csv(r"files/output/cliente_endereco.csv", index=False, sep=';')


gera_dados_clientes_enderecos(num_clientes=5, num_enderecos= 8)