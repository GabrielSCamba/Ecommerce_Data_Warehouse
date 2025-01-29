from faker import Faker
import pandas as pd
from datetime import date

def gerar_dados_enderecos(data_atual: date) :
    """
    Gera um DataFrame com dados fictícios de endereços.
    
    Args:
        num_enderecos (int): Número de enderecos a serem gerados.
    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.
    """
    fake = Faker('pt_BR')
    enderecos = []

    # Quando modificar para pegar do banco de dados, dentro do loop, também alimentar a tabela associativa com o id_cliente e id_endereco.
    # Substituir o for _ in range(num_clientes): por for _ in id_cliente ou algo assim (para percorrer os valores de id_cliente)
    clientes = pd.read_csv(r"files/output/clientes.csv")
    num_clientes = clientes.shape[0]

    for _ in range(num_clientes):
        rua = fake.street_name()
        num_rua = fake.building_number()
        bairro = fake.bairro()
        cidade = fake.city()
        estado = fake.estado_sigla()
        cep = fake.postcode()

        # Dicionário com os dados do endereço
        dados_enderecos = {
            "RUA": rua,
            "NUMERO": num_rua,
            "BAIRRO": bairro,
            "CIDADE": cidade,
            "ESTADO": estado,
            "CEP": cep,
            "CRIADO_EM": data_atual,
            "MODIFICADO_EM": data_atual
        }

        enderecos.append(dados_enderecos)
    
    # Criando o DataFrame a partir da lista de enderecos
    df_enderecos = pd.DataFrame(enderecos)
    df_enderecos.to_csv(r"files/output/enderecos.csv", index=False, sep=';')

