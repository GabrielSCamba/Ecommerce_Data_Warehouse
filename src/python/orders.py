import random
from faker import Faker

def order_data(current_data, conn, cur):

    cur.execute("SELECT customerid FROM oltp.customers")  
    list_customers_id = [customer_id[0] for customer_id in cur.fetchall()]
    
    if len(list_customers_id) > 0 :
        customer_id = random.choice(list_customers_id)

        cur.execute("SELECT addressid FROM oltp.addresses WHERE customerid = %s;", (customer_id,))  
        list_addresses_id =  [address_id[0] for address_id in cur.fetchall()]
        address_id = random.choice(list_addresses_id)
    
        payment = random.choice(["WALLET CREDIT", "CREDIT CARD", "DEBIT CARD"])
        if payment == "CREDIT CARD" :
            installments = random.randint(1, 10)
        else :
            installments = 1 

        cur.execute(
            "INSERT INTO oltp.orders (customerid, addressid, payment, installments, date) VALUES (%s,%s, %s, %s, %s)RETURNING orderid;",
            (customer_id, address_id, payment, installments, current_data)
        )
        conn.commit()
        order_id = cur.fetchone()[0]

        cur.execute("SELECT productid FROM oltp.products",)  
        list_products_id = [product_id[0] for product_id in cur.fetchall()]
        num_items = random.randint(1, 5)
        products_id = random.sample(list_products_id, num_items)

        for id in products_id :
            quantity = random.randint(1, 3)

            cur.execute(
                "INSERT INTO oltp.order_items (orderid, productid, quantity) VALUES (%s, %s, %s)RETURNING itemid;",
                (order_id, id, quantity)
            )
            conn.commit()
            item_id = cur.fetchone()[0]

            if random.random() < 0.25:
                score = random.randint(1,5)
                fake = Faker()
                comment = fake.sentence(10,True)
                cur.execute(
                    "INSERT INTO oltp.product_review (itemid, score, reviewcomment) VALUES (%s, %s, %s);",
                    (item_id, score, comment)
                )
            conn.commit()