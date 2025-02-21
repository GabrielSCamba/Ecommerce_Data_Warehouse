WITH source as (
    SELECT 
        itemid,
	    orderid, 
	    productid,
	    quantity
    FROM {{ source ('postgres', 'order_items') }}
),

renamed AS (
    SELECT
        CAST(itemid AS INTEGER) AS id_item, 
        CAST(orderid AS INTEGER) AS id_order, 
        CAST(productid AS INTEGER) AS id_product, 
        CAST(quantity AS INTEGER) AS item_quantity
    FROM source
)

SELECT * FROM renamed