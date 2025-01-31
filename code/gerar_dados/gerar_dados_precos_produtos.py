import pandas as pd
from dateutil.relativedelta import relativedelta
import random


def gera_dados_preco_produtos(conn, cur, data_atual):
    
    """
    Gera um DataFrame com dados de preco de produtos através de um arquivo csv.
    
    Args:
        caminho_arquivo (str): caminho do arquivo csv com os produtos e categorias.
    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.

    """  

    arq_produtos = pd.read_csv(r"files/input/lista_produtos.csv", sep = ",")
    df_preco_produtos = arq_produtos[["id_produto", "preco"]]

    # Lista para armazenar os resultados
    lista_precos = []

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

    # Criando um DataFrame com os resultados
    df_precos = pd.DataFrame(lista_precos)
    
    cur.executemany(
        "INSERT INTO oltp.precos_produtos (id_produto, data_inicio, data_fim, preco) VALUES (%s, %s, %s, %s);",
        df_precos.values.tolist()
    )
    conn.commit()
