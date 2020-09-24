CREATE DATABASE Lorenzini;

USE Lorenzini;

CREATE TABLE Chat ( 
	id int NOT NULL PRIMARY KEY,
	tipo varchar(50),
	titolo varchar(50)      
);

CREATE TABLE Circolare ( 
	id int NOT NULL PRIMARY KEY,
	nome varchar(300),
	data date,
	link varchar(500)      
);
