WITH date_range AS (
    SELECT 
        MIN(date_order) AS date_start,
        MAX(date_order) AS date_end
    FROM {{ ref ('stg_orders') }}
), 

date_series AS (
    SELECT 
        generate_series(
            (SELECT date_start FROM date_range), 
            (SELECT date_end FROM date_range), 
            CAST('1 day' AS INTERVAL)
        )::DATE AS date_day
), 

date_attributes AS (
    SELECT 
        date_day,
        EXTRACT(YEAR FROM date_day) AS year,
        EXTRACT(QUARTER FROM date_day) AS quarter,
        EXTRACT(MONTH FROM date_day) AS month,
        TO_CHAR(date_day, 'Month') AS month_name,
        EXTRACT(DAY FROM date_day) AS day,
        EXTRACT(DOW FROM date_day) AS day_of_week,
        TO_CHAR(date_day, 'Day') AS day_name,
        CASE WHEN EXTRACT(DOW FROM date_day) IN (0, 6) THEN TRUE ELSE FALSE END AS is_weekend,
        EXTRACT(WEEK FROM date_day) AS week_of_year
    FROM date_series
)

SELECT * FROM date_attributes
