from datetime import date
from dateutil.relativedelta import relativedelta
import psycopg2
import random
from dotenv import load_dotenv
import os

from customers import new_customer
from products import product_data
from orders import order_data
from product_prices import product_price_data
from change_info import change_phone_number, new_address

start_date = date(2020,1,1)
end_date = date(2025,12,31)
current_date = start_date

env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
load_dotenv(env_path)

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cur = conn.cursor()

product_data(conn, cur)

while current_date <= end_date : 
    
    if current_date.day == 1:
        print(f"Starting Month-Year: {current_date.month}-{current_date.year}")
        product_price_data(current_date, conn, cur)
    
    num_customers = random.randint(0,5)
    if num_customers > 0 :
        for _ in range(num_customers) :
            new_customer(current_date, conn, cur)
    
    num_orders = random.randint(0, 10)
    if num_orders > 0 :
        for _ in range(num_orders) :
            order_data(current_date, conn, cur)

    if random.random() < 0.01 :
        if random.choice(["phone", "address"]) == "phone" :
            change_phone_number(conn, cur)
        else :
            new_address(current_date, conn, cur)   
    
    current_date += relativedelta(days=1)

print("Insertion finished.")

cur.close()
conn.close()
