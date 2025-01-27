import pandas as pd

def gerar_dados_produtos():
    
    """
    Gera um DataFrame com dados de produtos através de um arquivo csv.
    
    Args:
        caminho_arquivo (str): caminho do arquivo csv com os produtos e categorias.
    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.
    """
    arq_produtos = pd.read_csv(r"input/lista_produtos.csv", sep = ",")
    df_produtos= arq_produtos[["nome_produto", "descricao", "id_categoria"]]
    df_produtos.to_csv(r"produtos.csv", index=False, sep=';')

