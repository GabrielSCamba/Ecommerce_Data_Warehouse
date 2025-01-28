import pandas as pd

def gera_dados_categoria_produtos():
    
    """
    Gera um DataFrame com dados de categorias de produtos através de um arquivo csv.
    
    Args:
        caminho_arquivo (str): caminho do arquivo csv com os produtos e categorias.
    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.
    """
    
    arq_produtos = pd.read_csv(r"files/input/lista_produtos.csv", sep = ",")
    df_categoria_produtos = arq_produtos[["id_categoria", "categoria", "descricao_categoria"]]
    df_categoria_produtos.to_csv(r"files/output/categoria_produtos.csv", index=False, sep=";")

gera_dados_categoria_produtos()
