CREATE TABLE oltp.customers (
    customerid SERIAL PRIMARY KEY,
    cpf CHAR(14) UNIQUE NOT NULL,
    firstname VARCHAR(20) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F')) NOT NULL,
    birth DATE NOT NULL,
    emailaddress VARCHAR(50) UNIQUE NOT NULL,
    phone VARCHAR(30) NOT NULL,
    created DATE NOT NULL
);

CREATE TABLE oltp.addresses (
    addressid SERIAL PRIMARY KEY,
    customerid INTEGER NOT NULL,
    street VARCHAR(50) NOT NULL,
    streetnumber VARCHAR(5) NOT NULL,
    neighborhood VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    code CHAR(15) NOT NULL,
    CONSTRAINT fk_addresses_customer FOREIGN KEY (customerid) REFERENCES oltp.customers(customerid) ON DELETE CASCADE
);

CREATE TABLE oltp.products (
    productid INTEGER PRIMARY KEY,
    categoryid INTEGER NOT NULL,
    productname VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    CONSTRAINT fk_products_category FOREIGN KEY (categoryid) REFERENCES oltp.category_products(categoryid)
);

CREATE TABLE oltp.category_products (
    categoryid INTEGER PRIMARY KEY,
    categoryname VARCHAR(100) UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE oltp.orders (
    orderid SERIAL PRIMARY KEY,
    customerid INTEGER NOT NULL,
    addressid INTEGER NOT NULL,
    payment VARCHAR(20) NOT NULL,
    installments INTEGER CHECK (installments > 0) NOT NULL,
    date DATE NOT NULL,
    CONSTRAINT fk_orders_customer FOREIGN KEY (customerid) REFERENCES oltp.customers(customerid),
    CONSTRAINT fk_orders_address FOREIGN KEY (addressid) REFERENCES oltp.addresses(addressid)
);

CREATE TABLE oltp.order_items (
    itemid SERIAL PRIMARY KEY,
    orderid INTEGER NOT NULL,
    productid INTEGER NOT NULL,
    quantity INTEGER CHECK (quantity > 0) NOT NULL,
    CONSTRAINT fk_order_items_order FOREIGN KEY (orderid) REFERENCES oltp.orders(orderid) ON DELETE CASCADE,
    CONSTRAINT fk_order_items_product FOREIGN KEY (productid) REFERENCES oltp.products(productid)
);

CREATE TABLE oltp.product_review (
    reviewid SERIAL PRIMARY KEY,
    itemid INTEGER NOT NULL UNIQUE,
    score INTEGER CHECK (score BETWEEN 1 AND 5) NOT NULL,
    reviewcomment TEXT,
    CONSTRAINT fk_product_review_item FOREIGN KEY (itemid) REFERENCES oltp.order_items(itemid) ON DELETE CASCADE
);

CREATE TABLE oltp.product_price (
    priceid SERIAL PRIMARY KEY,
    productid INTEGER NOT NULL,
    startdate DATE NOT NULL,
    enddate DATE NOT NULL,
    price DECIMAL CHECK (price > 0) NOT NULL,
    CONSTRAINT fk_product_price FOREIGN KEY (productid) REFERENCES oltp.products(productid),
    CONSTRAINT check_price_date CHECK (enddate > startdate)
);
