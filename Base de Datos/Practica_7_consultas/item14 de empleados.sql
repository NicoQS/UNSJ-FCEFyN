-- 14) Muestre los empleados (first_name y last_name) que no sean supervisores (o directores).
-- NOTA: En la tabla departments el atributo manager_id 
-- tiene la identificación de los supervisores de cada dpto.
-- La consulta implementada muestra employee_id de los empleados,
-- para poner el foco en el problema del null
-- Este query (EXCEPT) da el resultado esperado, es decir,
-- el id de los 96 empleados que no son manager_id de departamentos

select employee_id
from employees
except 
select  *
from departments

-- Si lo implementamos con NOT IN, 
-- dado que el subquery devuelve ademas de los id de los 11 managers, 
-- tambien devuelve el valor nulo ya que hay 8 departamentos no poseen manager_id 
-- NO DA EL RESULTADO ESPERADO (ES ERRONEO)
-- el problema es que el NOT IN aplicado a un conjunto con valores nulos (null, ...)
-- da como resultado DESCONOCIDO, es decir, no da verdadero aunque el valor evaluado 
-- no este en el conjunto de los valores que acompanan al nulo, por eso el resultado es vacio

-- CON NOT IN - RESULTADO INCORRECTO
select employee_id
from employees
where  employee_id not in (select manager_id
				  			from departments)

-- CON NOT IN - RESULTADO CORRECTO AGREGANDO LA CONDICION NOT NULL 
select *
from employees
where  employee_id not in (select manager_id
				  		   from departments
						   where manager_id is not null)
						   
 -- CON NOT EXISTS - RESULTADO CORRECTO
 -- La razon es porque cuando se evalue un id de un empleado que no es manager
 -- no lo va a encontrar (vacio), y cuando compara con el valor null tampoco selecciona nada (vacio)
 -- dado que la condicion dara como resultado desconocido,
 -- por ende el not exists dara VERDADERO para las dos situaciones 
select *
from employees
where not exists (select manager_id
				  from departments
				  where   manager_id = employees.employee_id)

-- esta consulta es identica pero agregando la condicion de not null, 
-- y da el mismo resultado que la anterior (es decir, no hace la condicion)
select *
from employees
where not exists (select manager_id
				  from departments
				  where   manager_id = employees.employee_id
				  and manager_id is not null)


