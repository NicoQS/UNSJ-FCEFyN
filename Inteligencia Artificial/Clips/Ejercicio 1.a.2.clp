; Ejercicio 2
(deftemplate persona
   (slot nombre)
   (slot edad)
)

(defrule persona-mayor-de-edad
   (persona (nombre ?nombre) (edad ?edad))
   (test (> ?edad 18))
   =>
   (printout t "La persona " ?nombre " es mayor de 18 años." crlf)
)

(defrule dos-personas-diferentes
   (persona (nombre ?nombre1))
   (persona (nombre ?nombre2&~?nombre1))
   =>
   (printout t "Hay dos personas con nombres diferentes: " ?nombre1 " y " ?nombre2 crlf)
)

(defrule todo-el-mundo-es-mayor-de-edad
	(forall (persona (edad ?edad))
    (test (not (< ?edad 18))))
   =>
   (printout t "Todo el mundo es mayor de edad." crlf)
)

(deffacts personas-iniciales
   (persona (nombre "Juan") (edad 18))
   (persona (nombre "María") (edad 30))
)

(reset)
(run)
