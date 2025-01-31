from faker import Faker
import random

from gerar_dados_clientes import gerar_endereco, vincular_cliente_endereco

fake = Faker('pt_BR')

def alteracao_cadastro_telefone(data_atual, conn, cur) :
    cur.execute("SELECT id_cliente FROM oltp.clientes",)  
    lista_id_clientes = [id_cliente[0] for id_cliente in cur.fetchall()]
    id_cliente = random.choice(lista_id_clientes)
    num_telefone = fake.cellphone_number()
    cur.execute(
        "UPDATE oltp.clientes SET num_telefone = %s, modificado_em = %s WHERE id_cliente = %s",
        (num_telefone, data_atual, id_cliente)
    )
    conn.commit()

def cadastro_novo_endereco(data_atual, conn, cur) :
    cur.execute("SELECT id_cliente FROM oltp.clientes",)  
    lista_id_clientes = [id_cliente[0] for id_cliente in cur.fetchall()]
    id_cliente = random.choice(lista_id_clientes)
    novo_endereco = gerar_endereco(data_atual, conn, cur)

    vincular_cliente_endereco(id_cliente, novo_endereco, data_atual, conn, cur)
    conn.commit()