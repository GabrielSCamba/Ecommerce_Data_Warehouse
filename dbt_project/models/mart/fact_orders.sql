WITH source as (
SELECT
	p.id_order, 
	p.id_customer,
	p.id_address,
	p.payment_method,
    p.num_installments,
	p.date_order,
    SUM(ip.itens_price) AS order_price
FROM {{ ref ('stg_orders') }} p
JOIN {{ ref ('fact_order_items') }} ip ON p.id_order = ip.id_order
GROUP BY 1, 2, 3, 4, 5, 6
)

SELECT * FROM source