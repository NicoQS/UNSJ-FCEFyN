"""
La Secretaría de Ciencia y Tecnología del Rectorado, lo ha contratado a usted para desarrollar una aplicación que permita cargar los datos de los Proyectos y de las Personas que los integran, con distintos roles (director, codirector, integrante), los investigadores que integran los proyectos pueden tener categorías: I, II, III, IV o V.

Los proyectos vienen cargados en un archivo separado por el símbolo “;”, denominado proyectos.csv, que posee los siguientes datos:  idProyecto, titulo, palabrasClave.

Los integrantes de proeyectos vienen cargados en un archivo separado por el símbolo “;”, denominado integrantesProyecto.csv, que posee los siguientes datos: idProyecto, apellidoNombre, dni, categoriaInvestigacion, rol (director, codirector, integrante).

Para cargar los datos en memoria, deberá crear una clase ManejadorProyecto (implementado con una lista Python), y una clase ManejadorIntegrantesProyecto (implementado con un arreglo Numpy).

Nota: a la hora de procesar el archivo integrantesProyecto.csv, es importante destacar que no presenta un orden en particular, por lo que los integrantes de los proyectos se mezclan con los integrantes de otros proyectos

El analista funcional del sistema le encarga a usted que desarrolle un programa que lleve a cabo las siguientes funcionalidades:

1)      Cargar los datos de los Proyectos desde el archivo proyectos.csv.

2)      Cargar los datos de las Personas integrantes de los Proyectos, leyendo los datos del archivo integrantesProyecto.csv.

3)      Calcular los puntos por Proyecto, teniendo en cuenta las reglas de negocio.

4)      Listar los datos de los Proyectos ordenados por puntaje (de mayor a menor puntaje, rankin de Proyectos por puntaje), para ello, el analista le solicita que en la clase Proyecto sobrecargue el operador __gt__).

Reglas de negocio para el cálculo del puntaje (el puntaje final se acumula para dar un número que entrega un rankin de proyectos):

a)      Un proyecto debe tener como mínimo 3 (tres) integrantes (10 puntos si cumple, -20 si no cumple). Mensaje ‘El Proyecto debe tener como mínimo 3 integrantes’.

b)      Un proyecto debe tener  un Director con categoría I o II (10 puntos si cumple, -5 si no cumple). Mensaje ‘El Director del Proyecto debe tener categoría I o II.

c)       Un proyecto debe tener un codirector con categoría I, II o III (10 puntos si cumple, -5 si no cumple). Mensaje ‘El Codirector del Proyecto debe tener como mínimo categoría III’.

d)      Un Proyecto debe tener una persona con rol de  Director. Mensaje ‘El Proyecto debe tener un Director’

e)      Un proyecto debe tener una persona con el rol de Codirector. Mensaje ‘El Proyecto debe tener un Codirector’.

f)       Si el Proyecto no tiene Director o Codirector, restar 10 al puntaje.

Por cada regla que el proyecto no cumple, debe emitirse el mensaje propuesto por pantalla.
"""
from Menu import Menu
if __name__=="__main__":
    M=Menu()
    M.Menu_1()