WITH source as (
SELECT 
	id_address, 
	id_customer,
	street,
	num_street,
    neighborhood,
	city,
    state,
    zip_code
FROM {{ ref ('stg_addresses')}}
)

SELECT * FROM source