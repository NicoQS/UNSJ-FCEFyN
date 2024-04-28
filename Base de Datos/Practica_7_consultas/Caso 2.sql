--1. Muestre el nombre (first_name y last_name) y el salario (salary) de todos los empleados. Cambie el nombre de la columna first_name a Nombre y last_name a Apellido y salary a Salario.

SELECT first_name as nombre,last_name as apellido ,salary as salario FROM employees

--2. Muestre el nombre (first_name y last_name) y el salario (salary) de todos los empleados ordenado alfabéticamente por apellido (last_name).

SELECT first_name as nombre,last_name as apellido ,salary as salario FROM employees ORDER BY apellido

--3. Muestre el apellido (last_name) y la Comisión (commission_pct) que perciben los empleados cuya comisión sea mayor a 0.25. Mostrarlos ordenados en forma descendente por last_name.

SELECT last_name, commission_pct FROM employees WHERE commission_pct > 0.25 ORDER BY last_name

--4. Muestre la cantidad de empleados que trabajan en el departamento 100.
SELECT COUNT(*) FROM employees WHERE department_id = 100;
-- 5. Muestre todos los datos de los departamentos con identificador 10 ó 70 (department_id).
SELECT * FROM departments WHERE department_id = 10 OR department_id = 70;
-- 6. Muestre el nombre (last_name) de los empleados junto al nombre del departamento (department_name) donde trabajan.
SELECT DISTINCT last_name, department_name 
FROM
	(employees JOIN departments 
	ON
	employees.department_id = departments.department_id);
-- 7. Muestre el nombre (last_name) de los empleados de los departamentos de Finanzas (Finance) y/o Transporte (Shipping).
SELECT DISTINCT last_name, department_name 
FROM 
	(employees  JOIN departments
	ON
	employees.department_id = departments.department_id) 
	WHERE 
	department_name = 'Finance' OR department_name = 'Shipping';
--8. Muestre sin repetir los tipos de trabajos (jobs) que realizan en los departamentos los empleados. Liste el identificador del departamento y el nombre del trabajo.
SELECT DISTINCT department_id, job_title
FROM
(employees NATURAL JOIN jobs);

-- 9. Muestre los departamentos en los que los empleados realizan trabajos de Contabilidad (Stock Clerk) y Asistente de Administración (Shipping Clerk). Liste el identificador del departamento y el nombre del trabajo.
SELECT DISTINCT department_id, job_title
FROM
(employees NATURAL JOIN jobs)
WHERE job_title = 'Stock Clerk' OR job_title = 'Shipping Clerk';

-- 10. Muestre el nombre de los departamentos que tienen al menos 3 empleados.
SELECT department_name, COUNT(*)
FROM
	(employees JOIN departments
	ON
	employees.department_id = departments.department_id)
GROUP BY department_name
HAVING COUNT(*) >= 3;

-- 11. Muestre el nombre de los empleados (last_name) y el salario (salary) de aquellos empleados que tienen un salario mayor que el salario promedio. Ordene el listado en forma descendente por salario.
SELECT last_name, salary
FROM 
	employees
WHERE 
	salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

-- 12. Muestre el salario máximo de los empleados del departamento 110. Ordene el listado en forma ascendente por salario.
SELECT first_name,MAX(salary)
FROM
	employees
WHERE
	department_id = 110
GROUP BY salary
ORDER BY salary ASC;


SELECT DISTINCT salary
FROM
	employees
WHERE
	department_id = 110 and salary = (SELECT MAX(salary) FROM employees WHERE department_id = 110)
ORDER BY salary ASC;

-- 13. Muestre el nombre del/de los empleados que tienen el sueldo máximo del departamento 110. Ordene el listado en forma ascendente por salario

SELECT DISTINCT first_name,salary
FROM
	employees
WHERE
	department_id = 110 and salary = (SELECT MAX(salary) FROM employees WHERE department_id = 110)
ORDER BY salary ASC;


-- 14. Muestre los empleados (first_name y last_name) que no sean supervisores (o directores). NOTA: En la tabla departments el atributo manager_id tiene la identificación de los supervisores de cada dpto.
SELECT first_name,last_name
FROM employees 
WHERE employee_id NOT IN (SELECT manager_id FROM departments);
-- Otra manera
SELECT first_name, last_name
FROM employees
WHERE NOT EXISTS (SELECT * FROM departments WHERE manager_id = employee_id);

-- 15. Especifique la Vista EmpFinan que contenga todos los empleados del departamento 100 con los atributos first_name como nombre, last_name como apellido y department_name como nom_dpto.
CREATE VIEW EmpFinan (first_name, last_name,  nom_dpto) AS (SELECT first_name, last_name, department_name FROM (employees JOIN departments ON employees.department_id = departments.department_id)  WHERE departments.department_id = 100);

-- 16. Realice una consulta que muestre la vista completa.
SELECT * FROM EmpFinan;
-- 17. Gestión de usuarios y privilegios: Crear los siguientes usuarios y otorgarles privilegios.
-- HRDep Permisos de SELECT, INSERT, UPDATE, ALTER sobre objetos del esquema.
CREATE USER HRDep WITH ENCRYPTED PASSWORD 'HRDep';
GRAN SELECT, INSERT, UPDATE, ALTER ON ALL TABLES IN SCHEMA public TO HRDep;
-- HrUser Permisos de SELECT sobre objetos del esquema.
CREATE USER HrUser WITH ENCRYPTED PASSWORD 'HrUser';
GRAN SELECT ON ALL TABLES IN SCHEMA public TO HrUser;