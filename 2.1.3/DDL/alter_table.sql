-- Adicionando uma nova coluna com valor padrão automático
ALTER TABLE clientes
ADD COLUMN data_cadastro DATE DEFAULT CURRENT_DATE;
