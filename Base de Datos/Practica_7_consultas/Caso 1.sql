--A. Inserte nuevas Personas con los siguientes datos:
INSERT INTO persona VALUES ( 'kf@gmail.com', 'kf', 'Katerin Falcon');
INSERT INTO persona VALUES ( 'kmgh@gmail.com', 'mgh','Rosa González');
INSERT INTO persona VALUES ( 'rgh@gmail.com', 'rlh','Rosa López');

--B. Inserte el nuevo curso con los siguientes datos:
INSERT INTO curso VALUES ( 'Ruby', 40);

--C. Inserte los temas para el curso con los siguientes datos:
INSERT INTO tema VALUES ('Ruby', 'Estructuras de datos');
INSERT INTO tema VALUES ('Ruby', 'Estructuras de control');

--D. Inserte la nueva tupla para DICTA con los siguientes datos:
INSERT INTO dicta VALUES ('kf@gmail.com', 'Ruby');

--E. Modifique la carga horaria del curso Ruby con el valor 60.
Update curso SET ch=60 where nom='Ruby'

--F. Elimine el curso Ruby.
DELETE FROM curso WHERE nom='Ruby';
-- CONSULTAS
-- 1) Correo y nombre de todas las personas.
SELECT DISTINCT correo,nombre FROM persona
-- 2) Nombre de los cursos.
SELECT nom FROM curso
-- 3) Nombre del curso que tiene una carga horaria superior a la de todos los cursos que dicta “pedroibañez@yahoo.com.ar”.
SELECT nom FROM curso, (SELECT max(ch) as chMax FROM (
curso NATURAL JOIN (
SELECT nom FROM dicta WHERE correo='pedroibañez@yahoo.com.ar'
) as dicta2
)) as max2 WHERE curso.ch > chMax

--4) Datos (todos) de las personas (docentes o alumnos) que poseen como nombre Rosa (solamente o alguno de ellos).
SELECT * FROM persona WHERE LOWER(nombre) LIKE '%rosa%'

-- 5) Nombres de los cursos que tienen una carga horaria superior a la del curso “Kotlin I”
SELECT nom FROM curso,
(SELECT max(ch) FROM curso WHERE nom='Kotlin I') as mx
WHERE curso.ch > mx.max
--10 Cursos (nombre) junto a los datos del docente que los dicta
SELECT DISTINCT nom,correo, nomu,nombre FROM (dicta NATURAL JOIN persona)
/* 11. Cursos (todos los datos) junto a los datos de los alumnos inscriptos en ellos.
deben incluir todos los cursos registrados más allá que no tengan alumnos inscriptos.*/
SELECT curso.nom,ch,correod,nomu,nombre,nota
FROM (curso LEFT JOIN
(SELECT * FROM inscripcion NATURAL JOIN persona) as np
on curso.nom=np.nom)
-- 12. Docentes (todos los datos) que dictan los cursos “Python I”.
SELECT DISTINCT correo,nomu,nombre
FROM ((SELECT correo,nom FROM dicta WHERE nom='Python I')
as pt1
NATURAL JOIN persona)
--13. Docentes (todos los datos) que dictan los cursos “Python II".
SELECT DISTINCT correo,nomu,nombre
FROM ((SELECT correo,nom FROM dicta WHERE nom='Python II')
as pt1
NATURAL JOIN persona)
-- 14. Docentes (correo y nombre) que dictan el curso “Python I” y/o “Python II”.
SELECT DISTINCT correo,nombre
FROM ((SELECT correo,nom FROM dicta WHERE nom='Python I' or nom='Python II')
as pt1
NATURAL JOIN persona)
-- 15. Docentes (correo) que dictan los cursos “Python I” y “Python II”.
SELECT DISTINCT correo,nombre
FROM
(persona NATURAL JOIN
((SELECT correo FROM dicta WHERE nom='Python I')
INTERSECT
(SELECT correo FROM dicta WHERE nom='Python II'))
as nm)

select correo,nomu,nombre
from persona natural join dicta
where nom = 'Python I'
intersect
select correo,nomu,nombre
from persona natural join dicta
where nom = 'Python II'

-- 16. Docentes (todos los datos) que cursaron algún curso de verano.
SELECT correo,nomu,nombre
FROM (persona NATURAL JOIN
(SELECT inscripcion.correo
FROM inscripcion JOIN dicta on inscripcion.correo=dicta.correo) as cr)
-- 17. Alumnos (todos los datos) que se inscribieron en el curso “Kotlin I”.
SELECT *
FROM (SELECT correo FROM inscripcion WHERE nom='Kotlin I') as np NATURAL JOIN persona

--18. Alumnos (todos los datos) que se inscribieron en el curso “Kotlin II”.
SELECT *
FROM (SELECT correo FROM inscripcion WHERE nom='Kotlin II') as np NATURAL JOIN persona

--19. Alumnos (correo) que se inscribieron tanto en el curso “Kotlin I” como “Kotlin II”.
SELECT DISTINCT correo
FROM
(persona NATURAL JOIN
((SELECT correo FROM inscripcion WHERE nom='Kotlin I')
INTERSECT
(SELECT correo FROM inscripcion WHERE nom='Kotlin II'))
as nm)

--20. Alumnos (todos los datos) que aprobaron el curso “Python I” y “Python II”.
SELECT *
FROM
(persona NATURAL JOIN
((SELECT correo FROM inscripcion WHERE nom='Python I' and nota>=6)
INTERSECT
(SELECT correo FROM inscripcion WHERE nom='Python II' and nota >= 6))
as nm)

--21. Alumnos (Correo) que se inscribieron en más de un curso de verano.

SELECT DISTINCT inscripcion.correo
FROM
(inscripcion JOIN inscripcion as ins2
on inscripcion.correo=ins2.correo and inscripcion.nom != ins2.nom)

--22. Docentes (todos los datos) que dictan más de un curso cuya carga horaria sea inferior a 30 horas reloj.
SELECT DISTINCT *
FROM(
persona NATURAL JOIN
(SELECT dicta.correo FROM ((dicta JOIN dicta as dicta2
on dicta.correo=dicta2.correo and dicta.nom != dicta2.nom)
JOIN CURSO on dicta.nom = curso.nom and curso.ch <= 30
)) as np
)

--28. Especifique la Vista “Cursoscortos” que tenga los siguientes atributos nombre, carga horaria. Los cursos cortos son aquellos cuya carga horaria es inferior a las 40 horas.

CREATE VIEW CursosCortos (nombre,cargahoraria) AS
SELECT nom,ch FROM curso WHERE ch<40

--29. Muestre los datos contenidos en la vista, ordenados según el nombre.

SELECT * FROM CursosCortos ORDER BY nombre

--30. Inserte el curso “DBA PostgreSQL” con una carga horaria de 50 horas, a través de la vista

INSERT INTO CursosCortos VALUES ('DBA PostgreSQL', 50)

--31. Elimine la vista, y vuelva a crearla pero agregando la especificación “WITH CHECK OPTION”

CREATE VIEW CursosCortos (nombre,cargahoraria) AS
SELECT nom,ch FROM curso WHERE ch<40 WITH CHECK OPTION

--32.Inserte el curso “DBA Oracle” con una carga horaria de 55 horas, a través de la vista.

INSERT INTO CursosCortos VALUES ('DBA Oracle', 55)

--33. Especifique la Vista “Alumnos_python1” que tenga los siguientes atributos correo, nombre de usuario, nombre y representan a los alumnos que se inscribieron en el curso “PYTHON I”

CREATE VIEW Alumnos_python1 (correo,nomusuario,nombre) AS
SELECT correo,nomu,nombre FROM (persona NATURAL JOIN (SELECT correo FROM inscripcion WHERE nom='Python I')AS pY)

--34. Muestre los datos contenidos en la vista creada en el punto anterior, cuyo correo sea una cuenta de Gmail.

SELECT * FROM Alumnos_python1 WHERE correo LIKE '%@gmail.com'

--35. Especifique la Vista “Alumnos_python2” que tenga los siguientes atributos nombre de usuario, nombre y representan a los alumnos que se inscribieron en el curso “PYTHON II”

CREATE VIEW Alumnos_python2 (nomusuario,nombre) AS
SELECT nomu,nombre FROM (persona NATURAL JOIN (SELECT correo FROM inscripcion WHERE nom='Python II')AS pY)


--36. Muestre los datos contenidos en la vista.

SELECT * FROM Alumnos_python2

--37. Inserte un nuevo alumno con los siguientes datos: < orm@gmail.com, or, Orlando Martin >
INSERT INTO Alumnos_python1 VALUES ('orm@gmail.com', 'or','Orlando Martin')

--38. Cree un usuario (alumno) con contraseña “alumno1”

CREATE USER alumno WITH ENCRYPTED PASSWORD 'alumno1'


--39. Cambie su contraseña, por “alumno”

ALTER USER alumno WITH PASSWORD 'alumno'

--40. Concédale el permiso de SELECT e INSERT sobre la tabla CURSO.

GRANT SELECT, INSERT on CURSO to alumno

--41. Visualice los permisos del usuario “alumno”: SELECT , privilege_type FROM information_schema.table_privileges WHERE grantee = 'alumno';

SELECT * FROM information_schema.table_privileges WHERE grantee = 'alumno';


--42. Accediendo con ese usuario (debe generar una nueva instancia que referencie al mismo servidor, pero con el usuario “alumno”), ejecute un SELECT sobre la tabla CURSO y luego, sobre la tabla DICTA. Analice las respuestas.

Select * FROM DICTA

--43. Elimine el permiso SELECT sobre la tabla DICTA

REVOKE SELECT ON DICTA FROM alumno

--44. Visualice nuevamente los permisos del usuario “alumno”


SELECT * FROM information_schema.table_privileges WHERE grantee = 'alumno';