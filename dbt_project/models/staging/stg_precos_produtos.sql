WITH source as (
    SELECT 
        id_preco, 
        id_produto, 
        data_inicio, 
        data_fim,
        preco 
    FROM {{ source ('postgres', 'precos_produtos') }}
),

renamed AS (
    SELECT
        CAST(id_preco AS VARCHAR) AS price_id, 
        CAST(id_produto AS VARCHAR) AS product_id, 
        CAST(data_inicio AS DATE) AS date_start, 
        CAST(data_fim AS DATE) AS date_end, 
        CAST(preco AS DECIMAL) AS price
    FROM source
)

SELECT * FROM renamed