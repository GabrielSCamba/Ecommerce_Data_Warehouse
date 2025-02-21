WITH source as (
    SELECT 
        categoryid,
	    categoryname,
	    description 
    FROM {{ source ('postgres', 'category_products') }}
),

renamed AS (
    SELECT
        CAST(categoryid AS INTEGER) AS id_category,
        CAST(categoryname AS VARCHAR) AS name_category, 
        CAST(description AS TEXT) AS description_category
    FROM source
)

SELECT * FROM renamed