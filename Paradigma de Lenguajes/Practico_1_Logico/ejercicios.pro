humano(turing).
humano(socrates).
griego(socrates).
mortal(X) :- humano(X).

% Se pide:
% a) Definir un objetivo (consulta) que nos permita conocer todos los mortales que son griegos.
% b) Especificar todos los pasos que debe realizar el intérprete Prolog para obtener las soluciones del objetivo anterior

mortal(X), griego(X).

----------------------------------------------------------------------------------------------------------------------------

% Suponga definidas las siguientes claúsulas:
padre(X,Y). % X es padre de Y.
madre(X,Y). % X es madre de Y.
hombre(X). % X es hombre.
mujer(X). % X es mujer.
progenitor(X,Y). % X es padre o madre de Y.

% Se pide definir en base a ellas las siguientes relaciones:
% es_madre (X). X es madre.
% es_padre (X). X es padre.
% es_hijo (X). X es hijo.
% hija (X,Y). X es hija de Y.
% tio (X,Y). X es tío de Y.
% sobrino (X,Y). X es sobrino de Y.
% prima (X,Y). X es prima de Y.
% abuelo_o_abuela (X,Y). X es abuelo o abuela de Y

es_madre(X) :- madre(X, _).
% es_madre(X) :- mujer(X), progenitor(X, _).

es_padre(X) :- padre(X, _).
% es_padre(X) :- hombre(X), progenitor(X, _).

es_hijo(X) :- hombre(X), progenitor(_, X).
hija(X, Y) :- mujer(X), progenitor(Y, X).

hermano(X, Y) :- progenitor(Padre, X), progenitor(Padre, Y), X \= Y.

tio(Tio, Sobrino) :- hombre(Tio), hermano(Tio, Padre), progenitor(Padre, Sobrino).
sobrino(X,Y) :- tio(Y, X).
prima(X,Y) :- mujer(X), progenitor(Padre, X), tio(Padre, Y).

abuelo_o_abuela(X, Y) :- progenitor(X, Z), progenitor(Z, Y).

----------------------------------------------------------------------------------------------------------------------------
% Defina el predicado POTENCIA:
% potencia (3,0,X). ---> X=1
% potencia (5,2,25). ---> true

% potencia(A, B, C) :- C is A ** B.

potencia(_, 0, 1) :- !.
potencia(A, B, C) :- B > 0, D is B - 1, potencia(A, D, E), C is A * E.

----------------------------------------------------------------------------------------------------------------------------

% Defina el predicado MODULO:
% modulo(10,5,R). ---> R=0
% modulo(14,3,R). ---> R=2

% modulo(A, B, C) :- C is A mod B.

modulo(A, B, A) :- A < B, !.
modulo(A, B, R) :- A >= B, C is A - B, modulo(C, B, R).

----------------------------------------------------------------------------------------------------------------------------

% Defina el predicado MIEMBRO:
% miembro (1, [3,2,1]). ---> true
% miembro (X, [3,2,1]). ---> X=3, X=2, X=1

% miembro(X, LISTA) :- member(X, LISTA).

miembro(X, [X | _]).
miembro(X, [_ | COLA]) :- miembro(X, COLA).

----------------------------------------------------------------------------------------------------------------------------

% Defina el predicado ADYAC que verifica si dos elementos son adyacentes en una lista.
% adyac(3, 2, [3,2,1]). ---> true
% adyac(2, 3, [3,2,1]). ---> true
% adyac(X, 2, [3,2,1]). ---> X=3, X=1

% adyac(A, B, LIST) :- nextto(A, B, LIST).
% adyac(A, B, LIST) :- nextto(B, A, LIST).

adyac(A, B, [A, B | _]).
adyac(A, B, [B, A | _]).
adyac(A, B, [_ | COLA]) :- adyac(A, B, COLA).

----------------------------------------------------------------------------------------------------------------------------

% Defina el predicado REVES:
% reves([3,2,1], [1,2,3]). ---> true (Hacer seguimiento)
% reves([3,2,1], X). ---> X=[1,2,3]

% reves(LISTA, RESULTADO) :- reverse(LISTA, RESULTADO).

reves([], []).
% reves([A], [A]) :- !.
reves([CABEZA | COLA], RESULTADO) :- reves(COLA, A), append(A, [CABEZA], RESULTADO).

----------------------------------------------------------------------------------------------------------------------------

% Defina el predicado ELIM que permita eliminar un elemento de una lista.
% elim(2, [3,2,1], [3,1]). ---> true
% elim(2, [2,3,1], X). ---> X=[3,1]

% elim(LISTA, ELEM, RESULTADO) :- delete(LISTA, ELEM, RESULTADO).

elim(_, [], []).
elim(ELEM, [ELEM | COLA], COLA).
elim(ELEM, [CABEZA | COLA], [CABEZA | A]) :- elim(ELEM, COLA, A).

----------------------------------------------------------------------------------------------------------------------------

% Dadas las cláusulas medico y paciente y una relación entre ellas representada por la cláusula atiende, mediante los siguientes hechos:
medico(m1,rosales).
medico(m2,manni).
paciente(p1,juan).
paciente(p2,ana).
atiende(m1,p1).
atiende(m1,p2).
atiende(m2,p2).

atiende2(M, P) :- medico(A, M), atiende(A, B), paciente(B, P).

opcion(1) :- write("Nombre del medico: "), read(X), atiende2(X, P), writeln(P), fail.
opcion(2) :- write("Nombre del paciente: "), read(P), atiende2(X, P), writeln(X), fail.
opcion(3) :- writeln("ADIOS"), !.
opcion(_) :- base.

base :-
    writeln('1. encontrar pacientes de un medico'),
    writeln('2. encontrar medicos de un paciente'),
    writeln('3. Terminar'),
    read(X), opcion(X).