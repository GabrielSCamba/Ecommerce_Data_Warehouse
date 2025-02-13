WITH source as (
    SELECT 
        id_avaliacao, 
        id_produto, 
        nota,
        comentario 
    FROM {{ source ('postgres', 'avaliacao_produto') }}
),

renamed AS (
    SELECT
        CAST(id_avaliacao AS VARCHAR) AS rating_id,   
        id_produto AS product_id,
        CAST(nota AS INTEGER) AS score,
        comentario AS comment
    FROM source
)

SELECT * FROM renamed