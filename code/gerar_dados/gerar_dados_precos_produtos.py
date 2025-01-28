import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random


def gera_dados_preco_produtos(data_inicio, data_fim):
    
    """
    Gera um DataFrame com dados de preco de produtos através de um arquivo csv.
    
    Args:
        caminho_arquivo (str): caminho do arquivo csv com os produtos e categorias.
    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.

    """

    arq_produtos = pd.read_csv(r"files/input/lista_produtos.csv", sep=",")
    print(arq_produtos.head())  # Exibe as primeiras linhas
    print(arq_produtos.columns)  # Exibe os nomes das colunas
    

    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
    data_fim = datetime.strptime(data_fim, "%Y-%m-%d")    

    arq_produtos = pd.read_csv(r"files/input/lista_produtos.csv", sep = ",")
    df_preco_produtos = arq_produtos[["id_produto", "preco"]]

    # Datas de início e fim
    
    data_atual = data_inicio

    # Lista para armazenar os resultados
    lista_precos = []

    # Percorrendo mês a mês
    while data_atual <= data_fim:
        for i, preco in zip(df_preco_produtos["id_produto"], df_preco_produtos["preco"]):
            # Aplicando uma variação de 10% para cima ou para baixo
            variacao_preco = preco * random.uniform(0.9, 1.1)
            
            # Adicionando os dados à lista
            lista_precos.append({
                "ID_PRODUTO": i,
                "DATA_INICIO": data_atual,
                "DATA_FIM": data_atual + relativedelta(months=1),
                "PRECO": round(variacao_preco, 2)  # Arredondando para 2 casas decimais
            })
        # Avançando para o próximo mês
        data_atual += relativedelta(months=1)

    # Criando um DataFrame com os resultados
    df_precos = pd.DataFrame(lista_precos)
    df_precos.to_csv(r"files/output/precos_produtos.csv",index=False, sep= ";")
    print(df_precos)

    return df_precos

data_inicio = "2020-1-1"  # Data inicial
data_fim = "2024-12-31" # Data final

gera_dados_preco_produtos(data_inicio=data_inicio,data_fim=data_fim)