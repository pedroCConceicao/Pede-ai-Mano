CREATE TABLE produtosham (
	cod_ham INT auto_increment PRIMARY KEY,
    nome VARCHAR(300) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE produtospiz (
	cod_piz INT auto_increment PRIMARY KEY,
    nome VARCHAR(300) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE usuario (
	cod_usuario INT auto_increment PRIMARY KEY,
    nome VARCHAR(600) NOT NULL,
    cpf VARCHAR(15) NOT NULL,
    endereco VARCHAR(800) NOT NULL,
    sigla_estado VARCHAR(10) NOT NULL,
    email VARCHAR(200) NOT NULL,
    senha VARCHAR(200) NOT NULL
);

CREATE TABLE carrinho(
	cod_usuario INT NOT NULL,
    cod_piz INT,
    cod_ham INT,
    finalizado BOOL,
	CONSTRAINT fk_usr FOREIGN KEY (cod_usuario) REFERENCES usuario(cod_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_ham FOREIGN KEY (cod_ham) REFERENCES produtosham(cod_ham) ON DELETE CASCADE,
    CONSTRAINT fk_piz FOREIGN KEY (cod_piz) REFERENCES produtosham(cod_piz) ON DELETE CASCADE
);