--3. Muestre los materiales (descripción) pedidos el día 06/06/2010.

SELECT descrip
FROM (materiales NATURAL JOIN (
SELECT cm FROM pedidos WHERE to_date('13/02/2020', 'DD/MM/YYYY') = fecha
)as dp );

select descrip from materiales
natural join pedidos
where fecha= '2010-06-06'


--4. Muestre para cada obra (indicando descripción) todos los materiales solicitados (descripción).
--Deben informarse todas las obras, más allá que aún no tenga materiales pedidos.

SELECT obras.descrip,pd.descrip
FROM
obras LEFT JOIN (
SELECT pedidos.co,materiales.descrip
FROM pedidos join materiales on pedidos.cm = materiales.cm
) as pd
on obras.co = pd.co;

--5. Muestre la cantidad total de bolsas de cal que han sido pedidas a la ferretería MR S.A.

select sum(cant)
from pedidos
where cuit=(select cuit from ferreterias where nom='MR S.A')
and cm=(select cm from materiales where descrip='Cal')


--6. Muestre la cantidad total de obras que han pedido materiales a la ferretería MR S.A.


SELECT COUNT(*)
FROM (
ferreterias JOIN (SELECT pedidos.cuit FROM (
pedidos NATURAL JOIN materiales
)) as pd on ferreterias.cuit = pd.cuit
) WHERE ferreterias.nom='MR S.A';


-- 7. Muestre, para cada material pedido a alguna ferretería, el código de material
-- , código de obra y la cantidad total pedida (independientemente de la ferretería).

SELECT cm,co, sum(cant) FROM pedidos group by cm ,co

--8. Muestre la descripción de materiales pedidos para alguna obra en una cantidad
--promedio mayor a 320 unidades.

SELECT materiales.descrip
FROM (
materiales natural join
(SELECT pedidos.cm FROM pedidos GROUP BY cm,co HAVING AVG(cant) > 320)AS np
);

select descrip
from pedidos natural join materiales
group by cm,descrip
having avg(cant)>320
order by cm


--9. Muestre el nombre del material menos pedido (en cantidad total).

SELECT cm FROM pedidos GROUP BY cm HAVING
SUM(cant) = (
SELECT SUM(cant) FROM pedidos GROUP BY cm ORDER BY SUM(cant) LIMIT 1
)

--10. Muestre la descripción de las obras que no han utilizado pintura.

SELECT descrip
FROM obras
WHERE NOT EXISTS (
SELECT * FROM (pedidos NATURAL JOIN materiales) WHERE descrip='Pintura' AND pedidos.co = obras.co
)

--11. Muestre el nombre de las obras abastecidas totalmente por la ferretería MR S.A.

SELECT descrip
FROM obras
WHERE NOT EXISTS (
SELECT * FROM pedidos
WHERE pedidos.co=obras.co
AND pedidos.cuit != (SELECT cuit FROM ferreterias WHERE nom='MR S.A')
)


--12. Muestre el nombre de los materiales que han sido pedidos para todas las obras realizadas.

SELECT descrip FROM materiales
WHERE NOT EXISTS(
SELECT * FROM obras
WHERE NOT EXISTS(
SELECT * FROM pedidos WHERE obras.co = pedidos.co and pedidos.cm=materiales.cm )
);

--13. Actualice el teléfono de la Ferretería San Ignacio por el número 4312548 .


UPDATE ferreterias SET tel='4312548' WHERE nom='San Ignacio'