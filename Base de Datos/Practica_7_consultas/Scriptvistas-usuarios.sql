Create view cursoscortos (nombre,cargahoraria)
as SELECT nom,ch
FROM curso
WHERE curso.ch < 40
WITH CHECK OPTION;

Select *
From cursoscortos1

Select *
From cursoscortos

INSERT INTO cursoscortos VALUES ('Base de Datos II', 50);

create USER usuario WITH PASSWORD 'alumno1';


alter  USER usuario WITH PASSWORD 'alumno';

grant SELECT,INSERT ON Cursos de Verano TO usuario;

--Algunos ejemplo--
-- mostrar privilegios de un usuario
SELECT table_name, privilege_type
FROM information_schema.table_privileges
WHERE grantee = 'usuariocomun';

------- USUARIOS--------	   
drop  USER usuariocomun 

create USER usuariocomun WITH PASSWORD 'usuariocomun';

alter  USER usuariocomun WITH PASSWORD 'usuariocomun';

-- concesion de privilegios
GRANT SELECT ON club TO usuariocomun;
GRANT INSERT ON club TO usuariocomun;

-- eliminar  privilegios
REVOKE select 
   ON club
   FROM usuariocomun;


