from faker import Faker
import random
from datetime import date
from unidecode import unidecode
import pandas as pd
import os

def gerar_dados_clientes(data_atual: date) -> pd.DataFrame:
    """
    Gera um DataFrame com dados fictícios de clientes.
    
    Args:
        data_atual (date): Data relativa a serem gerados os dados.
        data_nasc_inicio (date): Data de início para nascimento dos clientes (formato date(YYYY, MM, DD)).
        data_nasc_fim (date): Data de fim para nascimento dos clientes (formato date(YYYY, MM, DD)).

    Returns:
        pd.DataFrame: DataFrame contendo os dados gerados.
    """
    fake = Faker('pt_BR')

    clientes = []  # Lista para armazenar os dados dos clientes
    num_clientes_gerados = random.randint(0,5)

    for i in range(num_clientes_gerados) :
        if num_clientes_gerados > 0 :
            genero_aleatorio = random.choice(["male", "female"])
            if genero_aleatorio == "male":
                first_name = fake.first_name_male()
                genero = "M"
            else:
                first_name = fake.first_name_female()
                genero = "F"
            
            cpf = fake.cpf()
            last_name = fake.last_name() 
            data_nascimento = fake.date_between(start_date= date(1920,1,1), end_date= date(2020,12,31))
            email = unidecode(f"{first_name}.{last_name}@email.com").lower().replace(" ", "_")
            telefone = fake.cellphone_number()
                            
            # Dicionário com os dados do cliente
            clientes.append({
                "ID_CLIENTE": i #Alterar quando consultar do banco de dados
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
        
    # Criando o DataFrame a partir da lista de clientes
    df_clientes = pd.DataFrame(clientes)
    file_path = "files/output/clientes.csv"
    df_clientes.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False, sep=';')
    return df_clientes

'''
data_nasc_inicio = date(1944,1,1)
data_nasc_fim = date(2007,12,31)
data_inicio = date(2020,1,1)
data_fim = date(2020,1,5)
data_atual = data_inicio

gerar_dados_clientes(data_atual = data_atual,                                               
                    data_nasc_inicio = data_nasc_inicio,                
                    data_nasc_fim = data_nasc_fim                    
                    )
'''