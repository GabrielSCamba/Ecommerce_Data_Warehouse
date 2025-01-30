import pandas as pd

def cadastrar_produtos(cur, conn):
    
    """
    Gera um DataFrame com dados de produtos através de um arquivo csv.
    
    Args:
        caminho_arquivo (str): caminho do arquivo csv com os produtos e categorias.
    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.
    """
    
    arq_produtos = pd.read_csv(r"files/input/lista_produtos.csv", sep = ",")

    # Gerar categoria dos produtos
    df_categorias = arq_produtos[["nome_categoria", "descricao_categoria"]]

    cur.executemany(
    "INSERT INTO oltp.categorias_produtos (nome_categoria, descricao_categoria) VALUES (%s, %s);",
    df_categorias.values.tolist()
    )
    conn.commit()
    
    # Gerar produtos
    df_produtos = arq_produtos[["id_categoria", "nome_produto", "descricao_produto"]]

    cur.executemany(
    "INSERT INTO oltp.produtos (id_categoria, nome_produto, descricao_produto) VALUES (%s, %s, %s);",
    df_produtos.values.tolist()
    )
    conn.commit()