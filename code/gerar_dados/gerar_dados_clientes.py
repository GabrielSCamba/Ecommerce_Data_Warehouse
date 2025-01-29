from faker import Faker
import random
from datetime import date
from unidecode import unidecode
import pandas as pd
import os
import psycopg2

def cadastrar_cliente(data_atual: date,
                      cur, 
                      conn):
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
    
    genero_aleatorio = random.choice(["male", "female"])
    if genero_aleatorio == "male":
        primeiro_nome = fake.first_name_male()
        genero = "M"
    else:
        primeiro_nome = fake.first_name_female()
        genero = "F"
            
    cpf = fake.cpf()
    sobrenome = fake.last_name() 
    data_nascimento = fake.date_between(start_date= date(1920,1,1), end_date= date(2020,12,31))
    email = unidecode(f"{primeiro_nome}.{sobrenome}@email.com").lower().replace(" ", "_")
    num_telefone = fake.cellphone_number()
                    
    cur.execute(
    "INSERT INTO oltp.clientes (cpf, primeiro_nome, sobrenome, genero, data_nascimento, email, num_telefone, criado_em, modificado_em) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s)RETURNING id_cliente;",
    (cpf, primeiro_nome, sobrenome, genero, data_nascimento, email, num_telefone, data_atual, data_atual)
    )
    id_cliente = cur.fetchone()[0]
    conn.commit()

    rua = fake.street_name()
    num_rua = fake.building_number()
    bairro = fake.bairro()
    cidade = fake.city()
    estado = fake.estado_sigla()
    cep = fake.postcode()

    cur.execute(
    "INSERT INTO oltp.enderecos (rua, numero, bairro, cidade, estado, cep, criado_em, modificado_em) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)RETURNING id_endereco;",
    (rua, num_rua, bairro, cidade, estado, cep, data_atual, data_atual)
    )
    conn.commit()
    id_endereco = cur.fetchone()[0]

    cur.execute(
        "INSERT INTO oltp.clientes_enderecos (id_cliente, id_endereco, criado_em, modificado_em) VALUES (%s, %s, %s, %s);",
        (id_cliente, id_endereco, data_atual, data_atual)
    )
    conn.commit()

