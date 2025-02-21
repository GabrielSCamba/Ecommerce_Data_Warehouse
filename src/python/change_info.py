from faker import Faker
import random

from customers import address_data

fake = Faker()

def change_phone_number(conn, cur) :
    cur.execute("SELECT customerid FROM oltp.customers")  
    list_customers_id = [customer_id[0] for customer_id in cur.fetchall()]
    drawn_customer = random.choice(list_customers_id)
    phone = fake.phone_number()
    cur.execute(
        "UPDATE oltp.customers SET phone = %s WHERE customerid = %s",
        (phone, drawn_customer)
    )
    conn.commit()

def new_address(current_date, conn, cur) :
    cur.execute("SELECT customerid FROM oltp.customers")  
    list_customers_id = [customer_id[0] for customer_id in cur.fetchall()]
    drawn_customer = random.choice(list_customers_id)

    address = address_data()

    cur.execute(
    "INSERT INTO oltp.addresses (customerid, street, streetnumber, neighborhood, city, state, code, created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
    (drawn_customer, address["street"], address["number"], address["neighborhood"], address["city"], address["state"], address["code"], current_date)
    )
    conn.commit()