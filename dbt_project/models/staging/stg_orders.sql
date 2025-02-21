WITH source as (
    SELECT 
        orderid,
	    customerid, 
	    addressid, 
	    payment, 
	    installments,
	    date DATE
    FROM {{ source ('postgres', 'orders') }}
),

renamed AS (
    SELECT
        CAST(orderid AS INTEGER) AS id_order, 
        CAST(customerid AS INTEGER) AS id_customer, 
        CAST(addressid AS INTEGER) AS id_address,
        CAST(payment AS VARCHAR) AS payment_method,
        CAST(installments AS INTEGER) AS num_installments,
        CAST(date AS DATE) AS date_order
    FROM source
)

SELECT * FROM renamed