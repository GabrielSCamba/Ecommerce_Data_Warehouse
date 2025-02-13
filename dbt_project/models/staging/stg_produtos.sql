WITH source as (
    SELECT 
        id_produto, 
        id_categoria, 
        nome_produto, 
        descricao_produto
    FROM {{ source ('postgres', 'produtos') }}
),

renamed AS (
    SELECT
        CAST(id_produto AS VARCHAR) AS product_id,  
        id_categoria AS category_id,  
        nome_produto AS name_product, 
        descricao_produto AS product_description
    FROM source
)

SELECT * FROM renamed