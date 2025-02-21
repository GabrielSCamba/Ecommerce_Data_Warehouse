WITH source as (
    SELECT 
        customerid,
	    cpf,
	    firstname,
	    lastname,
	    gender,
	    birth,
	    emailaddress,
	    phone,
	    created
    FROM {{ source ('postgres', 'customers') }}
),

renamed AS (
    SELECT
        CAST(customerid AS INTEGER) AS id_customer,  
        CAST(REGEXP_REPLACE(cpf, '[^0-9]', '', 'g') AS VARCHAR) AS cpf_customer,  
        CAST(firstname AS VARCHAR) AS first_name, 
        CAST(lastname AS VARCHAR) AS last_name,
        CAST(gender AS CHAR),
        CAST(birth AS DATE) AS date_birth,
        CAST(emailaddress AS VARCHAR) AS email_address,
        CAST(phone AS VARCHAR) AS phone_number,
        CAST(created AS DATE) AS created_at
    FROM source
)

SELECT * FROM renamed