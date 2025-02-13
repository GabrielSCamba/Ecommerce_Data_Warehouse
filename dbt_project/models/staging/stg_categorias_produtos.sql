WITH source as (
    SELECT 
        id_categoria, 
        nome_categoria, 
        descricao_categoria 
    FROM {{ source ('postgres', 'categorias_produtos') }}
),

renamed AS (
    SELECT
        CAST(id_categoria AS VARCHAR) AS category_id,  
        nome_categoria AS name_category, 
        descricao_categoria AS category_description
    FROM source
)

SELECT * FROM renamed