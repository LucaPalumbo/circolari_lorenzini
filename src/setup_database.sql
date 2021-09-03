CREATE DATABASE Lorenzini;

USE Lorenzini;

CREATE TABLE IF NOT EXISTS Chat (
	id int NOT NULL PRIMARY KEY,
	tipo varchar(50),
	titolo varchar(50)
);

CREATE TABLE IF NOT EXISTS Circolare (
	id int NOT NULL PRIMARY KEY,
	nome varchar(300),
	data date,
	link varchar(500)
);
