CREATE TABLE oltp.customers(
	customerid SERIAL PRIMARY KEY,
	cpf CHAR(14),
	firstname VARCHAR(20),
	lastname VARCHAR(50),
	gender CHAR(1),
	birth DATE,
	emailaddress VARCHAR(50),
	phone VARCHAR(30),
	created DATE
);

CREATE TABLE oltp.addresses(
	addressid SERIAL PRIMARY KEY,
	customerid INTEGER,
	street VARCHAR(50),
	streetnumber VARCHAR(5),
	neighborhood VARCHAR(50),
	city VARCHAR(50),
	state VARCHAR(50),
	code CHAR(15)
);

CREATE TABLE oltp.products(
	productid INTEGER,
	categoryid INTEGER,
	productname VARCHAR(100),
	description TEXT
);

CREATE TABLE oltp.category_products(
	categoryid INTEGER,
	categoryname VARCHAR(100),
	description TEXT
);

CREATE TABLE oltp.orders(
	orderid SERIAL PRIMARY KEY,
	customerid INTEGER, 
	addressid INTEGER, 
	payment VARCHAR(20), 
	installments INTEGER,
	date DATE
);

CREATE TABLE oltp.order_items(
	itemid SERIAL PRIMARY KEY,
	orderid INTEGER, 
	productid INTEGER,
	quantity INTEGER
);

CREATE TABLE oltp.product_review(
	reviewid SERIAL,
	itemid INTEGER, 
	score INTEGER, 
	reviewcomment TEXT
);

CREATE TABLE oltp.product_price(
	priceid SERIAL PRIMARY KEY,
	productid INTEGER,
	startdate DATE,
	enddate DATE,
	price DECIMAL
);
