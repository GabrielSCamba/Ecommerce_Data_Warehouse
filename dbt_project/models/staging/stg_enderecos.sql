WITH source as (
    SELECT 
        id_endereco, 
        id_cliente, 
        rua,
        numero,
        bairro,
        cidade,
        estado,
        cep,
        criado_em,
        modificado_em
    FROM {{ source ('postgres', 'enderecos') }}
),

renamed AS (
    SELECT
        CAST(id_endereco AS VARCHAR) AS address_id,
        CAST(id_cliente AS VARCHAR) AS customer_id,
        CAST(rua AS VARCHAR) AS street,
        CAST(numero AS VARCHAR) AS street_num,
        bairro AS neighborhood,
        cidade AS city,
        estado AS "state",
        cep AS zip_code,
        CAST(criado_em AS TIME) AS created_at,
        CAST(modificado_em AS TIME) AS updated_at,
        
    FROM source
)

SELECT * FROM renamed