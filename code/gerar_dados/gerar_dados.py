from datetime import date
from dateutil.relativedelta import relativedelta
import psycopg2
import random

from gerar_dados_clientes import vincular_cliente_endereco, gerar_cliente, gerar_endereco
from gerar_dados_produtos import cadastrar_produtos
from gerar_dados_pedidos import gerar_pedido
from gerar_dados_precos_produtos import gera_dados_preco_produtos
from gerar_dados_alteracao_cadastro import alteracao_cadastro_telefone, cadastro_novo_endereco

data_inicio = date(2020,1,1)
data_fim = date(2020,12,31)
data_atual = data_inicio

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cadastrar_produtos(conn, cur)

while data_atual <= data_fim : 
    
    if data_atual.day == 1:
        gera_dados_preco_produtos(conn, cur, data_atual)
    
    num_clientes_gerados = random.randint(0,5)
    if num_clientes_gerados > 0 :
        for _ in range(num_clientes_gerados) :
            id_cliente = gerar_cliente(data_atual, conn, cur)
            id_endereco = gerar_endereco(data_atual, conn, cur)
            vincular_cliente_endereco(id_cliente, 
                                    id_endereco, 
                                    data_atual,
                                    conn, 
                                    cur)
    
    num_pedidos = random.randint(0, 10)
    if num_pedidos > 0 :
        for _ in range(num_pedidos) :
            gerar_pedido(data_atual, conn, cur)

    if random.random() < 0.01 :
        if random.choice(["telefone", "endereco"]) == "telefone" :
            alteracao_cadastro_telefone(data_atual, conn, cur)
        else :
            cadastro_novo_endereco(data_atual, conn, cur)   
    
    data_atual += relativedelta(days=1)

# Fechar conexão após todas as inserções
cur.close()
conn.close()
