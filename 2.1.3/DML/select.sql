-- Exemplo de consulta filtrada, ordenada e limitada

SELECT nome, email
FROM clientes
WHERE telefone LIKE '11%'
ORDER BY nome ASC
LIMIT 5;
