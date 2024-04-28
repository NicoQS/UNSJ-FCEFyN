from Menu import Menu
from ClaseJugador import Jugador
from ClaseEquipo import Equipo
from ClaseContrato import Contrato
def test():
    jugador=Jugador("44766976","Nicolas Quiroga Santini","San Juan","Argentina","08/05/2003")
    equipo=Equipo("UPCN VOLEY","San Juan")
    contrato=Contrato("22/05/2022","22/05/2023",125000,jugador,equipo)
    print(contrato)


if __name__ == "__main__":
    #test()
    M=Menu()
    M.menuOp()
"""
Lote de prueba:
1
11111111
Club Atletico San Lorenzo de Almagro
22/08/2021
22/08/2022
130000
1
55555555
Club Atletico Colon
20/10/2021
20/10/2022
100000
1
77777777
Club Atletico Boca Juniors
15/05/2021
15/05/2023
230000
1
33333333
Club Atletico Newell's Old Boys
10/02/2020
10/02/2023
170000
1
88888888
Club Atletico San Lorenzo de Almagro
15/08/2020
15/10/2022
165000
"""