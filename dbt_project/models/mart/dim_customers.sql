WITH source as (
SELECT 
	id_customer, 
	cpf_customer,
	first_name,
	last_name,
    CONCAT(first_name, ' ', last_name) AS full_name,
	gender,
    date_birth,
    email_address,
    phone_number,
    created_at
FROM {{ ref ('stg_customers')}}
)

SELECT * FROM source

