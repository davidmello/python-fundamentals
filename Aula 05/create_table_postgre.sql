CREATE TABLE posts (
	id serial primary key,
	titulo VARCHAR(255),
	conteudo TEXT
);


CREATE TABLE users (
	id serial primary key,
	usuario VARCHAR(255),
	senha VARCHAR(255)
);