import pandas as pd
from dateutil.relativedelta import relativedelta
import random


def product_price_data(current_date, conn, cur):
    file_products = pd.read_csv(r"files/input/list_products.csv", sep = ",")
    df_products_prices = file_products[["product_id", "price"]]

    price_list = []

    for i, price in zip(df_products_prices["product_id"], df_products_prices["price"]):
        price_variance = price * random.uniform(0.9, 1.1)
        
        price_list.append({
            "product_id": i,
            "start": current_date,
            "end": current_date + relativedelta(months=1),
            "price": round(price_variance, 2)  
        })

    df_prices = pd.DataFrame(price_list)
    
    cur.executemany(
        "INSERT INTO oltp.product_price (productid, startdate, enddate, price) VALUES (%s, %s, %s, %s);",
        df_prices.values.tolist()
    )
    conn.commit()
