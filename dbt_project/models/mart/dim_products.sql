WITH source as (
SELECT 
	p.id_product, 
	p.name_product,
	c.name_category,
	p.description_product,
	c.description_category
FROM {{ ref ('stg_products') }} p
JOIN {{ ref ('stg_category_products') }} c ON p.id_category = c.id_category
)

SELECT * FROM source