WITH source as (
    SELECT 
        id_pedido, 
        id_cliente, 
        id_endereco, 
        metodo_pagamento,
        num_parcelas,
        data_pedido 
    FROM {{ source ('postgres', 'pedidos') }}
),

renamed AS (
    SELECT
        CAST(id_pedido AS VARCHAR) AS order_id, 
        CAST(id_cliente AS VARCHAR) AS customer_id, 
        CAST(id_endereco AS VARCHAR) AS address_id, 
        metodo_pagamento AS payment_method,
        num_parcelas AS num_installments,
        data_pedido AS order_date 
    FROM source
)

SELECT * FROM renamed