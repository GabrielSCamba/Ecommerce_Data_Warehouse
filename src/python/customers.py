from faker import Faker
import random
from datetime import date
from unidecode import unidecode

def customer_data():

    fake = Faker('pt_BR')
    
    random_gender = random.choice(["M", "F"])
    if random_gender == "M":
        name = fake.first_name_male()
        gender = random_gender
    else:
        name = fake.first_name_female()
        gender = random_gender
    last_name = fake.last_name()

    customer ={
        "name" : name, 
        "gender" : gender,      
        "cpf" : fake.cpf(),
        "last_name" : last_name, 
        "birth_date" : fake.date_between(start_date= date(1920,1,1), end_date= date(2020,12,31)),
        "email" : unidecode(f"{name}.{last_name}@email.com").lower().replace(" ", "_"),
        "phone" : fake.cellphone_number()
    }
                        
    return customer

def address_data():
    fake = Faker('pt_BR')
    
    address = {
        "street": fake.street_name(),
        "number": fake.building_number(),
        "neighborhood": fake.neighborhood(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "code": fake.postcode()
    }
    
    return address

def new_customer(current_date, conn, cur):   
    customer = customer_data()

    cur.execute(
    "INSERT INTO oltp.customers (cpf, firstname, lastname, gender, birth, emailaddress, phone, created) VALUES (%s, %s, %s, %s, %s, %s,%s, %s) RETURNING customerid;",
    (customer["cpf"], customer["name"], customer["last_name"], customer["gender"], customer["birth_date"], 
     customer["email"], customer["phone"], current_date)
    )

    customer_id = cur.fetchone()[0]

    address = address_data()

    cur.execute(
    "INSERT INTO oltp.addresses (customerid, street, streetnumber, neighborhood, city, state, code, created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
    (customer_id, address["street"], address["number"], address["neighborhood"], address["city"], 
     address["state"], address["code"], current_date)
    )
    conn.commit()
