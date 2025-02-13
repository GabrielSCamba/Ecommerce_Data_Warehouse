WITH source as (
    SELECT 
        id_item, 
        id_pedido, 
        id_produto, 
        quantidade 
    FROM {{ source ('postgres', 'itens_pedido') }}
),

renamed AS (
    SELECT
        CAST(id_item AS VARCHAR) AS item_id, 
        CAST(id_pedido AS VARCHAR) AS order_id, 
        CAST(id_produto AS VARCHAR) AS product_id, 
        CAST(quantidade AS INTEGER) AS quantity
    FROM source
)

SELECT * FROM renamed