WITH source as (
    SELECT 
        productid,
	    categoryid,
	    productname,
	    description
    FROM {{ source ('postgres', 'products') }}
),

renamed AS (
    SELECT
        CAST(productid AS INTEGER) AS id_product,  
        CAST(categoryid AS INTEGER) AS id_category,
        CAST(productname AS VARCHAR) AS name_product,  
        CAST(description AS TEXT) AS description_product
    FROM source
)

SELECT * FROM renamed