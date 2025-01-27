from faker import Faker
import random
from datetime import datetime
from unidecode import unidecode
import pandas as pd
from dateutil.relativedelta import relativedelta

def gerar_dados_clientes(data_inicio: str,
                        data_fim: str,                                    
                        data_nasc_inicio: str,                
                        data_nasc_fim: str                    
                        ) -> pd.DataFrame:
    """
    Gera um DataFrame com dados fictícios de clientes.
    
    Args:
        num_clientes (int): Número de clientes a serem gerados.
        data_nasc_inicio (str): Data de início para nascimento dos clientes (formato 'YYYY-MM-DD').
        data_nasc_fim (str): Data de fim para nascimento dos clientes (formato 'YYYY-MM-DD').

    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.
    """
    fake = Faker('pt_BR')
    
    # Convertendo datas de string para objetos datetime.date
    data_nasc_inicio = datetime.strptime(data_nasc_inicio, '%Y-%m-%d')
    data_nasc_fim = datetime.strptime(data_nasc_fim, '%Y-%m-%d')
    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
    data_fim = datetime.strptime(data_fim, "%Y-%m-%d")

    data_atual = data_inicio

    clientes = []  # Lista para armazenar os dados dos clientes

    while data_atual <= data_fim:
        num_clientes_gerados = random.randint(0,5)

        if num_clientes_gerados > 0 :
            for i in range(num_clientes_gerados) :
                genero_aleatorio = random.choice(["male", "female"])
                if genero_aleatorio == "male":
                    first_name = fake.first_name_male()
                    genero = "M"
                else:
                    first_name = fake.first_name_female()
                    genero = "F"
                
                cpf = fake.cpf()
                last_name = fake.last_name()
                data_nascimento = fake.date_between(start_date=data_nasc_inicio, end_date=data_nasc_fim)
                email = unidecode(f"{first_name}.{last_name}@email.com").lower().replace(" ", "_")
                telefone = fake.cellphone_number()
                                
                # Dicionário com os dados do cliente
                clientes.append({
                    "CPF": cpf,
                    "PRIMEIRO_NOME": first_name,
                    "SOBRENOME": last_name,
                    "GENERO": genero,
                    "DATA_NASCIMENTO": data_nascimento,
                    "EMAIL": email,
                    "TELEFONE": telefone,
                    "CRIADO_EM": data_atual,
                    "MODIFICADO_EM": data_atual
                })
            
        data_atual += relativedelta(days=1)
   
    # Criando o DataFrame a partir da lista de clientes
    df_clientes = pd.DataFrame(clientes)
    df_clientes.to_csv(r"output/clientes.csv", index=False, sep=';')
    
    return df_clientes

data_nasc_inicio = '1944-01-01'
data_nasc_fim = '2007-12-31'
data_inicio = '2020-01-01'
data_fim = '2024-12-31'

gerar_dados_clientes(data_inicio = data_inicio,                
                    data_fim = data_fim,                                 
                    data_nasc_inicio = data_nasc_inicio,                
                    data_nasc_fim = data_nasc_fim                    
                    )