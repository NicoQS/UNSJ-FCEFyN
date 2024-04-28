/*
Sucursal = {num, direcc, tel, provincia}
Producto = {cod, num, nombre, precio, stock}
Ingrediente = {cod (código del producto), num, nombre, kcal (cantidad de calorías)}
Factura = {num (número de factura), fecha, calif(calificación otorgada)}
Detalle = {numf (número de factura), cod (código del producto), num (número de la sucursal), precio, cantidad}
*/

-- 1. Sucursales (todos los datos) que vendieron todos los productos que se comercializan en San Luis.
SELECT *
FROM sucursal
WHERE NOT EXISTS (
		SELECT *
		FROM producto NATURAL JOIN SUCURSAL
		WHERE provincia = 'San Luis' AND NOT EXISTS (
			SELECT *
			FROM detalle
			WHERE detalle.cod = producto.cod AND sucursal.num = detalle.num
		)
	);
select *
from sucursal s
where not exists (select *
				 from producto p natural join sucursal 
				 where provincia= 'San Luis' and not exists (select *
															  from detalle d
															  where d.cod = p.cod and s.num = d.num))
-- 2. Provincias donde se venden más de un producto.
SELECT provincia
FROM sucursal NATURAL JOIN producto
GROUP BY provincia
HAVING COUNT(cod) > 1;

-- 3. Sucursales (todos los datos) que venden tanto Pizza napolitana como Pizza napolitana especial.
SELECT * 
FROM sucursal NATURAL JOIN (
	(SELECT num FROM producto
	WHERE nombre = 'Pizza napolitana')
	INTERSECT
	(SELECT num FROM producto
	WHERE nombre = 'Pizza napolitana especial')
) AS pz;
-- 4. Productos (nombre y stock) comercializados en las provincias de Cuyo (San Juan, Mendoza y San Luis).
SELECT DISTINCT nombre, stock
FROM producto NATURAL JOIN (
	(SELECT nombre FROM (producto NATURAL JOIN sucursal)
	WHERE provincia = 'San Juan')
	INTERSECT
	(SELECT nombre FROM (producto NATURAL JOIN sucursal)
	WHERE provincia = 'Mendoza')
	INTERSECT
	(SELECT nombre FROM (producto NATURAL JOIN sucursal)
	WHERE provincia = 'San Luis')
) as cuyo
group by nombre,stock;
-- 5. Provincias que no venden Pizza muzzarella.
SELECT provincia
FROM sucursal
EXCEPT
(SELECT provincia FROM producto NATURAL JOIN sucursal
WHERE nombre = 'Pizza muzzarella');
-- 6. Sucursales (número y dirección) que no venden el producto ‘Pizza con jamón’. 
SELECT num, direcc
FROM sucursal
EXCEPT
(SELECT num FROM producto NATURAL JOIN sucursal
WHERE nombre = 'Pizza con jamón');

-- 7. Nombre de productos vendidos por todas las sucursales de San Juan.
SELECT DISTINCT nombre
FROM producto
WHERE NOT EXISTS (
	SELECT *
	FROM (SELECT num
				   FROM (detalle NATURAL JOIN sucursal)
				   WHERE provincia='San Juan'
				  ) as sucSJ
	WHERE NOT EXISTS (
		SELECT *
		FROM detalle 
		WHERE detalle.num=sucSJ.num AND detalle.cod = producto.cod
	)		
)
-- 8. Para cada sucursal de la provincia de San Juan, obtener número e importe total facturado.
SELECT num, SUM(precio*cantidad) as importe
FROM (detalle NATURAL JOIN sucursal)
WHERE provincia = 'San Juan'
GROUP BY num;
-- 10. Provincia/s que más facturó durante el 2020.
SELECT provincia
FROM (
	SELECT provincia, SUM(precio*cantidad) as importe
	FROM factura JOIN (detalle NATURAL JOIN sucursal) ON factura.num = detalle.numf
	WHERE EXTRACT(YEAR FROM fecha) = 2020
	GROUP BY provincia) as A
	WHERE importe = (SELECT MAX(importe) FROM (
		SELECT provincia, SUM(precio*cantidad) as importe
		FROM factura JOIN (detalle NATURAL JOIN sucursal) ON factura.num = detalle.numf
		WHERE EXTRACT(YEAR FROM fecha) = 2020
		GROUP BY provincia) as A);

SELECT provincia, importe
FROM
    (SELECT provincia, sum(precio*cantidad) as importe
	 FROM factura
    JOIN
   	 (detalle
   	 NATURAL JOIN
   	 sucursal)
     ON numf=factura.num
    WHERE EXTRACT(YEAR FROM fecha)=2020
    GROUP BY provincia) as A
WHERE importe= (SELECT max(importe) FROM
   		   		 (SELECT provincia, sum(precio*cantidad) as importe
					 FROM factura
   				 JOIN
   				 (detalle
   				 NATURAL JOIN
   				 sucursal) ON numf=factura.num
   				 WHERE EXTRACT(YEAR FROM fecha)=2020
   				 GROUP BY provincia) as A)