import pandas as pd

def product_data(conn, cur):
    file_products = pd.read_csv(r"files/input/list_products.csv", sep = ",")

    df_categories = file_products[["category_id", "category_name", "category_description"]]

    cur.executemany(
    "INSERT INTO oltp.category_products (categoryid, categoryname, description) VALUES (%s, %s, %s);",
    df_categories.values.tolist()
    )
    conn.commit()
    
    # Gerar produtos
    df_products = file_products[["product_id", "category_id", "product_name", "product_description"]]

    cur.executemany(
    "INSERT INTO oltp.products (productid, categoryid, productname, description) VALUES (%s, %s, %s, %s);",
    df_products.values.tolist()
    )
    conn.commit()