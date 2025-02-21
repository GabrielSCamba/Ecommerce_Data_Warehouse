WITH source as (
    SELECT 
        reviewid,
	    itemid, 
	    score, 
	    reviewcomment
    FROM {{ source ('postgres', 'product_review') }}
),

renamed AS (
    SELECT
        CAST(reviewid AS INTEGER) AS id_review,   
        CAST(itemid AS INTEGER) AS id_item,
        CAST(score AS INTEGER),
        CAST(reviewcomment AS TEXT) AS comment_review
    FROM source
)

SELECT * FROM renamed