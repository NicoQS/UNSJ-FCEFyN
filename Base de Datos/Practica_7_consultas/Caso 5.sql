/*
Persona= {dni, pais, nombre, sexo, fechanac (fecha de nacimiento), provincia (provincia donde reside)}
Centro = {nombre, dirección, provincia}
Vacuna= {nombre, fechac (fecha de creación), cantidad (cantidad de dosis), laboratorio}
Aplica = {dni, pais, nombre (nombre del centro), nombrev (nombre de la vacuna), fecha, dnip (dni del profesional), paisp (país del profesional)}

*/

-- 1. Personas argentinas (dni, país y nombre) que se han aplicado más de una dosis.
SELECT persona.dni,persona.pais, persona.nombre
FROM (
	persona JOIN aplica 
	ON (persona.dni = aplica.dni AND persona.pais = aplica.pais) 
) WHERE persona.pais= 'argentina'
GROUP BY persona.dni, persona.pais, persona.nombre
HAVING COUNT(aplica.dni) > 1;
-- 2. Centros de salud (todos los datos) en los cuales se han aplicado la vacuna Sinopharm y/o Sputnik.
SELECT centro.*
FROM centro NATURAL JOIN aplica
WHERE aplica.nombrev = 'sinopharm' OR aplica.nombrev = 'sputnik';

-- 3. Personas (dni) que se han aplicado la vacuna Sinopharm pero no la Sputnik
SELECT dni 
FROM aplica
WHERE nombrev = 'Sinopharm'
EXCEPT
SELECT dni 
FROM aplica
WHERE nombrev = 'Sputnik';

-- 4. Centros de salud (nombre y provincia) que han vacunado tanto a personas oriundas de San Juan como oriundas de Mendoza durante el 2020.
SELECT centro.nombre, centro.provincia
FROM
centro
NATURAL JOIN
(SELECT nombre,fecha FROM (SELECT * FROM
							(aplica
							NATURAL JOIN
							(SELECT dni FROM persona WHERE provincia='san juan'  
							 INTERSECT
							SELECT dni FROM persona WHERE provincia='mendoza' )as sdf)) as fdg) as fgfg
WHERE EXTRACT (YEAR FROM fecha) = 2020;

-- 5. Profesionales (todos los datos) que han vacunado únicamente a personas argentinas.
SELECT *
FROM 
persona JOIN (SELECT dnip FROM (
								SELECT dnip FROM aplica WHERE paisp='argentina'
								EXCEPT
								SELECT dnip FROM aplica WHERE paisp != 'argentina'
								) AS pers
							) arg
ON (persona.dni = arg.dnip);

-- 6. Vacunas (todos los datos) que se han aplicado en todas las provincias de Cuyo (San Juan, Mendoza y San Luis).

SELECT *
FROM vacuna JOIN (SELECT nombrev FROM 
			(SELECT nombrev FROM (centro NATURAL JOIN aplica) WHERE provincia='san juan'
			INTERSECT
			SELECT nombrev FROM (centro NATURAL JOIN aplica) WHERE provincia='mendoza'
			INTERSECT
			SELECT nombrev FROM (centro NATURAL JOIN aplica) WHERE provincia='san luis')as cuyo) as cuyo ON vacuna.nombre = cuyo.nombrev;

-- 7. Centros de salud (nombre) que han vacunado a más de 100 personas (aplicaciones)
SELECT nombre
FROM (centro NATURAL JOIN aplica)
GROUP BY nombre
HAVING COUNT(nombre) > 100;

-- 8. Profesional (todos los datos) que realizó más vacunaciones (aplicaciones) durante el año 2020.
SELECT * FROM
persona JOIN (SELECT dnip FROM aplica WHERE EXTRACT (YEAR FROM fecha)=2020
							GROUP BY dnip
							HAVING COUNT(dnip) = (SELECT MAX(cant) FROM (SELECT COUNT(dnip) as cant FROM aplica WHERE EXTRACT (YEAR FROM fecha)=2020 GROUP BY dnip) as dni)
							) as maximo ON persona.dni = maximo.dnip;