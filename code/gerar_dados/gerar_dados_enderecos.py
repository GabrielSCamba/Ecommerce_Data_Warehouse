from faker import Faker
import pandas as pd

def gerar_dados_enderecos(num_enderecos: int,
                        )-> pd.DataFrame:
    """
    Gera um DataFrame com dados fictícios de endereços.
    
    Args:
        num_enderecos (int): Número de enderecos a serem gerados.
    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.
    """
    fake = Faker('pt_BR')
    enderecos = []

    for i in range(num_enderecos):
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
        }

        enderecos.append(dados_enderecos)
    
    # Criando o DataFrame a partir da lista de enderecos
    df_enderecos = pd.DataFrame(enderecos)
    df_enderecos.to_csv(r"output\enderecos.csv", index=False, sep=';')

gerar_dados_enderecos(num_enderecos = 8)