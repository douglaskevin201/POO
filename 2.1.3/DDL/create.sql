-- Criação de tabela estruturada com chaves e restrições
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TTEXT UNIQUE,
    telefone TEXT
);
