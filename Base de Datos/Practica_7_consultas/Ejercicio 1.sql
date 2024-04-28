CREATE TABLE IF NOT EXISTS CIU (
ciudadID INT PRIMARY KEY,
ciudadNom TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS PERS (
id INT PRIMARY KEY,
nom TEXT NOT NULL,
idC INT NOT NULL REFERENCES CIU (ciudadID) ON DELETE RESTRICT ON UPDATE CASCADE,
edad INT NOT NULL
);

CREATE TABLE IF NOT EXISTS PERS2 (
id INT PRIMARY KEY,
nom TEXT NOT NULL,
idC INT NOT NULL REFERENCES CIU (ciudadID) ON DELETE SET NULL ON UPDATE RESTRICT,
edad INT NOT NULL
);

INSERT INTO CIU(ciudadID, ciudadNom) VALUES
(1,'Estambul'),
(2,'Roma'),
(3,'Barcelona'),
(4,'Praga');


DELETE FROM public.ciu WHERE ciudadid = 3;

SELECT * FROM public.ciu
ORDER BY ciudadid ASC

INSERT INTO PERS(id,nom,idC,edad) VALUES
(6,'Juan Manuel Ariza',1,16),
(2,'Santiago Manrique',2,25),
(3,'Luciano Perez',4,50),
(4,'Andrea Hernández',1,22),
(5,'Ana Perez',3,30);

-- CONSULTAS
-- a) Muestre el nombre de las ciudades ordenadas alfabéticamente.
SELECT ciudadNom FROM CIU ORDER BY ciudadNom ASC
-- b) Muestre las personas (todos los datos) mayores de edad.
SELECT * FROM PERS WHERE edad >= 18
SELECT * FROM PERS2 WHERE edad >= 18
-- c) Muestre la cantidad de personas.
SELECT COUNT (*) FROM PERS
SELECT COUNT (*) FROM PERS2
-- d) Muestre la cantidad de ciudades.
SELECT COUNT (*) FROM CIU
-- e) Eliminar la ciudad con identificador igual a 1.
DELETE FROM CIU WHERE ciudadid=1
-- f) Muestre la cantidad de ciudades donde viven personas.
SELECT COUNT(*) FROM (SELECT DISTINCT ciudadID FROM PERS, CIU WHERE PERS.idc = CIU.ciudadID) as c