WITH source as (
    SELECT 
        priceid,
	    productid,
	    startdate,
	    enddate,
	    price
    FROM {{ source ('postgres', 'product_price') }}
),

renamed AS (
    SELECT
        CAST(priceid AS INTEGER) AS id_price, 
        CAST(productid AS INTEGER) AS id_product, 
        CAST(startdate AS DATE) AS date_start, 
        CAST(enddate AS DATE) AS date_end, 
        CAST(price AS DECIMAL) AS unit_price
    FROM source
)

SELECT * FROM renamed