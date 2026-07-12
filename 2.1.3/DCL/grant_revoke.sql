-- Exemplo conceitual de concessão e revogação de acessos
GRANT SELECT, INSERT ON clientes TO usuario_app;
REVOKE UPDATE ON clientes FROM usuario_antigo;
