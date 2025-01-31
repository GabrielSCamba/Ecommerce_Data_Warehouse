DROP TABLE oltp.clientes;
DROP TABLE oltp.enderecos;
DROP TABLE oltp.clientes_enderecos;
DROP TABLE oltp.categorias_produtos;
DROP TABLE oltp.produtos;
DROP TABLE oltp.precos_produtos;
DROP TABLE oltp.pedidos;
DROP TABLE oltp.itens_pedido;
DROP TABLE oltp.avaliacao_produto;

CREATE TABLE oltp.clientes(
	id_cliente SERIAL PRIMARY KEY,
	cpf CHAR(14),
	primeiro_nome VARCHAR(20),
	sobrenome VARCHAR(50),
	genero CHAR(1),
	data_nascimento DATE,
	email VARCHAR(50),
	num_telefone VARCHAR(30),
	criado_em DATE,
	modificado_em DATE
);

CREATE TABLE oltp.enderecos(
	id_endereco SERIAL PRIMARY KEY,
	rua VARCHAR(50),
	numero VARCHAR(5),
	bairro VARCHAR(50),
	complemento VARCHAR(50),
	cidade VARCHAR(50),
	estado VARCHAR(50),
	cep CHAR(15),
	criado_em DATE,
	modificado_em DATE
);

CREATE TABLE oltp.clientes_enderecos(
	id_clientes_enderecos SERIAL PRIMARY KEY,
	id_cliente INTEGER,
	id_endereco INTEGER,
	criado_em DATE,
	modificado_em DATE
);

CREATE TABLE oltp.produtos(
	id_produto SERIAL,
	id_categoria INTEGER,
	nome_produto VARCHAR(100),
	descricao_produto TEXT
);

CREATE TABLE oltp.categorias_produtos(
	id_categoria SERIAL,
	nome_categoria VARCHAR(100),
	descricao_categoria TEXT
);

CREATE TABLE oltp.pedidos(
	id_pedido SERIAL PRIMARY KEY,
	id_cliente INTEGER, 
	id_endereco INTEGER, 
	metodo_pagamento VARCHAR(20), 
	num_parcelas INTEGER,
	data_pedido DATE
);

CREATE TABLE oltp.itens_pedido(
	id_item SERIAL,
	id_pedido INTEGER, 
	id_produto INTEGER,
	quantidade INTEGER
);

CREATE TABLE oltp.avaliacao_produto(
	id_avaliacao SERIAL,
	id_produto INTEGER, 
	nota INTEGER, 
	comentario TEXT
);

CREATE TABLE oltp.precos_produtos(
	id_preco SERIAL PRIMARY KEY,
	id_produto INTEGER,
	data_inicio DATE,
	data_fim DATE,
	preco DECIMAL
);


SELECT * FROM oltp.clientes;
SELECT * FROM oltp.enderecos;
SELECT * FROM oltp.clientes_enderecos;
SELECT * FROM oltp.produtos;
SELECT * FROM oltp.precos_produtos;
SELECT * FROM oltp.pedidos;
SELECT * FROM oltp.itens_pedido;
SELECT * FROM oltp.avaliacao_produto;

DELETE FROM oltp.precos_produtos
