from faker import Faker
import random
from datetime import datetime
from unidecode import unidecode
import pandas as pd


arq_produtos = pd.read_csv(r"input/lista_produtos.csv", sep=",")
print(arq_produtos.head())  # Exibe as primeiras linhas
print(arq_produtos.columns)  # Exibe os nomes das colunas





'''
num_clientes = 5
num_enderecos = 7
num_cliente_endereco = 10
data_nasc_inicio = '1944-01-01'
data_nasc_fim = '2024-12-31'

print("-------------------------------INICIO DA GERAÇÃO DE DADOS DE CLIENTES-------------------------------------")
print(gerar_dados_clientes(num_clientes= num_clientes, 
                         data_ecommerce_inicio= data_ecommerce_inicio, 
                         data_ecommerce_fim= data_ecommerce_fim, 
                         data_nasc_inicio= '1945-01-01', 
                         data_nasc_fim= '2007-01-01'))
print("-------------------------------FIM DA GERAÇÃO DE DADOS DE CLIENTES-------------------------------------")
print("-------------------------------INÍCIO DA GERAÇÃO DE DADOS DE ENDEREÇOS-------------------------------------")
print(gera_dados_enderecos(num_enderecos= num_enderecos,
                        num_clientes= num_clientes,
                        data_ecommerce_inicio= data_ecommerce_inicio, 
                        data_ecommerce_fim= data_ecommerce_fim))
print("-------------------------------FIM DA GERAÇÃO DE DADOS DE ENDEREÇOS-------------------------------------")

def gerar_dados_avaliacoes(num_avaliacoes, clientes, produtos):
    """
    Gera dados fictícios de avaliações de produtos.
    
    Args:
        num_avaliacoes (int): Número de avaliações a serem geradas.
        clientes (list): Lista de IDs de clientes.
        produtos (list): Lista de IDs de produtos.
    
    Returns:
        pd.DataFrame: DataFrame com os dados das avaliações.
    """
    fake = Faker('pt_BR')
    avaliacoes = []

    for _ in range(num_avaliacoes):
        id_cliente = random.choice(clientes)
        id_produto = random.choice(produtos)
        nota = random.randint(1, 5)  # Notas de 1 a 5
        comentario = fake.sentence(nb_words=random.randint(5, 15)) if random.random() > 0.3 else None
        data_avaliacao = fake.date_between(start_date='-2y', end_date='today')

        avaliacoes.append({
            "id_cliente": id_cliente,
            "id_produto": id_produto,
            "nota": nota,
            "comentario": comentario,
            "data_avaliacao": data_avaliacao
        })
    
    return pd.DataFrame(avaliacoes)

# Exemplo de uso
num_avaliacoes = 1000
clientes = [f"C{i}" for i in range(1, 101)]  # IDs fictícios de clientes (C1, C2, ..., C100)
produtos = [f"P{i}" for i in range(1, 81)]  # IDs fictícios de produtos (P1, P2, ..., P80)

df_avaliacoes = gerar_dados_avaliacoes(num_avaliacoes, clientes, produtos)

# Salvar em CSV (opcional)
df_avaliacoes.to_csv('avaliacoes.csv', index=False, sep=';')

'''


