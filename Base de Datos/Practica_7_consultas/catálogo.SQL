
-- consultas al catalogo  -----------

-- mostrar bd actual
SELECT current_database();

-- usuarios conectados
SELECT usename, application_name, client_addr, backend_start, state
FROM pg_stat_activity
WHERE state = 'active';

-- Mostrar todas las tablas en la base de datos actual:
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

-- Mostrar las columnas de una tabla específica:
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'curso';

-- Mostrar los índices de una tabla específica:
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'curso';

-- Mostrar las restricciones de integridad de una tabla específica:
SELECT conname, contype
FROM pg_constraint
WHERE conrelid = curso;

-- bases de datos dentro del servidor
select * from pg_database 

-- tamano de una tabla
SELECT pg_size_pretty(pg_total_relation_size('persona')) AS tamaño_conindices,
       pg_size_pretty(pg_relation_size('persona')) AS tamaño_sinindices
