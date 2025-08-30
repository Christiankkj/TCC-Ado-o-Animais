CREATE DATABASE IF NOT EXISTS animaisabandono;
USE animaisabandono;

-- Tabela usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(255),
    nome_dono VARCHAR(100)
);

-- Tabela denuncia_animais
CREATE TABLE denuncia_animais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_animal VARCHAR(50),
    quantidade INT,
    cordenada VARCHAR(100),
    id_usuario INT,
    criado_em DATETIME,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

-- Tabela ponto_adocao
CREATE TABLE ponto_adoacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_local VARCHAR(100),
    tipo_animal VARCHAR(50),
    quantidade_disponivel INT,
    id_usuario INT,
    responsavel_contato VARCHAR(100),
    cordenada VARCHAR(100),
    criado_em DATETIME,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);
