import random
from faker import Faker

def gerar_pedido(data_atual, conn, cur):

    # Sorteia um cliente para fazer a compra
    cur.execute("SELECT id_cliente FROM oltp.clientes",)  
    lista_id_clientes = [id_cliente[0] for id_cliente in cur.fetchall()]
    
    if len(lista_id_clientes) > 0 :
        id_cliente = random.choice(lista_id_clientes)

        # Sorteia um endereço do cliente 
        cur.execute("SELECT id_endereco FROM oltp.clientes_enderecos WHERE id_cliente = %s;", (id_cliente,))  
        lista_id_enderecos = [id_enderecos[0] for id_enderecos in cur.fetchall()]
        id_endereco = random.choice(lista_id_enderecos)
        
        # Sorteia um método de pagamento. Se for cartão sorteia um número de parcelas de 1 a 10
        metodo_pagamento = random.choice(["PIX", "CARTÃO DE CRÉDITO", "CARTÃO DE DÉBITO"])
        if metodo_pagamento == "CARTÃO DE CRÉDITO" :
            num_parcelas = random.randint(1, 10)
        else :
            num_parcelas = 1 

        # Registra o pedido
        cur.execute(
            "INSERT INTO oltp.pedidos (id_cliente, id_endereco, metodo_pagamento, num_parcelas, data_pedido) VALUES (%s,%s, %s, %s, %s)RETURNING id_pedido;",
            (id_cliente, id_endereco, metodo_pagamento, num_parcelas, data_atual)
        )
        conn.commit()
        id_pedido = cur.fetchone()[0]

        # Sorteia de 1 a 5 itens para incluir no pedido
        cur.execute("SELECT id_produto FROM oltp.produtos",)  
        lista_id_produtos = [id_produto[0] for id_produto in cur.fetchall()]
        num_itens = random.randint(1, 5)
        id_produtos = random.sample(lista_id_produtos, num_itens)

        for id in id_produtos :
            # Sorteia uma quantidade de itens de 1 a 3 
            quantidade = random.randint(1, 3)

            # Registra os itens do pedido
            cur.execute(
                "INSERT INTO oltp.itens_pedido (id_pedido, id_produto, quantidade) VALUES (%s, %s,%s);",
                (id_pedido, id, quantidade)
            )
            conn.commit()

            # Sorteia uma chance de 25% do cliente avaliar o produto
            if random.random() < 0.25:
                # Sorteia uma nota e um comentário
                nota = random.randint(1,5)
                fake = Faker()
                comentario = fake.sentence(10,True)
                cur.execute(
                    "INSERT INTO oltp.avaliacao_produto (id_produto, nota, comentario) VALUES (%s, %s,%s);",
                    (id, nota, comentario)
                )
            conn.commit()