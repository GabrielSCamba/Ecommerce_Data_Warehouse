from datetime import date
from dateutil.relativedelta import relativedelta
import time
import psycopg2
import random

from gerar_dados_clientes import cadastrar_cliente

data_nasc_inicio = date(1944,1,1)
data_nasc_fim = date(2007,12,31)
data_inicio = date(2020,1,1)
data_fim = date(2020,1,5)
data_atual = data_inicio

# Criar conexão única
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

while data_atual <= data_fim :
    num_clientes_gerados = random.randint(0,5)

    for _ in range(num_clientes_gerados) :
        if num_clientes_gerados > 0 :
            cadastrar_cliente(data_atual=data_atual, cur=cur, conn=conn)
    
    data_atual += relativedelta(days=1)

# Fechar conexão após todas as inserções
cur.close()
conn.close()