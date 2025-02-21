WITH source as (
    SELECT 
    addressid,
	customerid,
	street,
	streetnumber,
	neighborhood,
	city,
	state,
	code
    FROM {{ source ('postgres', 'addresses') }}
),

renamed AS (
    SELECT
        CAST(addressid AS INTEGER) AS id_address,
        CAST(customerid AS INTEGER) AS id_customer,
        CAST(street AS VARCHAR) AS street,
        CAST(streetnumber AS VARCHAR) AS num_street,
        CAST(neighborhood AS VARCHAR),
        CAST(city AS VARCHAR),
        CAST(state AS VARCHAR),
        CAST(REPLACE(code, '-', '') AS VARCHAR) AS zip_code
    FROM source
)

SELECT * FROM renamed