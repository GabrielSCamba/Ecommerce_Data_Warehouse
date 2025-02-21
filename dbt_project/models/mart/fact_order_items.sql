WITH source as (
    SELECT
        ip.id_item, 
        p.id_order,
        pd.id_product, 
        ip.item_quantity,
        pp.unit_price,
        (pp.unit_price * ip.item_quantity) AS itens_price,
        ap.score
    FROM {{ ref ('stg_order_items') }} ip
    LEFT JOIN {{ ref ('stg_products') }} pd ON ip.id_product = pd.id_product 
    LEFT JOIN {{ ref ('stg_orders') }} p ON p.id_order = ip.id_order
    LEFT JOIN {{ ref ('stg_product_price') }} pp ON p.date_order BETWEEN pp.date_start AND pp.date_end AND pp.id_product = pd.id_product
    LEFT JOIN {{ ref ('stg_product_review') }} ap ON  ip.id_item = ap.id_item
)     

SELECT * FROM source