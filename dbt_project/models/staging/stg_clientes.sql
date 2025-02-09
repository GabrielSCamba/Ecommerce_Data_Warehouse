WITH source as (
    SELECT 
        id_cliente, 
        cpf, 
        primeiro_nome, 
        sobrenome, 
        genero, 
        data_nascimento, 
        email, 
        num_telefone, 
        criado_em, 
        modificado_em
    FROM {{ source ('postgres', 'clientes') }}
),

renamed AS (
    SELECT
        CAST(id_cliente AS VARCHAR) AS customer_id,  
        cpf AS customer_cpf,  
        primeiro_nome AS first_name, 
        sobrenome AS last_name,  
        genero AS gender,  
        CAST(data_nascimento AS DATE) AS birth_date, 
        email AS email,  
        num_telefone AS phone_number,  
        CAST(criado_em AS TIMESTAMP) AS created_at,  
        CAST(modificado_em AS TIMESTAMP) AS updated_at  
    FROM source
)

SELECT * FROM renamed