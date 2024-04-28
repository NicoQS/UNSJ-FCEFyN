def func_max(lista,opciones):
    if opciones == "Temperatura":
        maxx=-1000000
        for i in range(30):
            for j in range(24):
                if lista[i][j].get_temp() > maxx:
                    maxx=lista[i][j].get_temp()
                    dia=i
                    hora=j
    elif opciones == "Humedad":
        maxx=-1000000
        for i in range(30):
            for j in range(24):
                if lista[i][j].get_hum() > maxx:
                    maxx=lista[i][j].get_hum()
                    dia=i
                    hora=j
    elif opciones == "Presion":
        maxx=-1000000
        for i in range(30):
            for j in range(24):
                if lista[i][j].get_pre() > maxx:
                    maxx=lista[i][j].get_pre()
                    dia=i
                    hora=j
    return dia,hora
def func_min(lista,opciones):
    if opciones == "Temperatura":
        minn=1000000
        for i in range(30):
            for j in range(24):
                if lista[i][j].get_temp() < minn:
                    minn=lista[i][j].get_temp()
                    dia=i
                    hora=j
    elif opciones == "Humedad":
        minn=10000000
        for i in range(30):
            for j in range(24):
                if lista[i][j].get_hum() < minn:
                    minn=lista[i][j].get_hum()
                    dia=i
                    hora=j
    elif opciones == "Presion":
        minn=10000000
        for i in range(30):
            for j in range(24):
                if lista[i][j].get_pre() < minn:
                    minn=lista[i][j].get_pre()
                    dia=i
                    hora=j
    return dia,hora
def variable_op1(lista):
    opciones=["Temperatura","Humedad","Presion"]
    for i in range(len(opciones)):
        maxx=func_max(lista,opciones[i])
        minn=func_min(lista,opciones[i])
        print ("Se registro la mayor {} en el dia {}  y hora {}, y el de menor en el dia {} y hora {}\n".format(opciones[i],maxx[0]+1,maxx[1],minn[0]+1,minn[1]))
def temp_prom(lista):
    for j in range(24):
        acum=0
        for i in range(30):
            acum+=lista[i][j].get_temp()
        print("La temperatura promedio de la hora {} en el mes es de: {:.2f}".format(j,acum/30))
def listado (lista):
    day=int(input("Ingrese un dia en especifico: "))
    print ("DIA:---{}--- ".format(day))
    print ("Hora\tTemperatura\tHumedad\t\tPresion\n")
    for j in range(24):
        print ("{}\t{}\t\t{}\t\t{}\n".format(j+1,lista[day-1][j].get_temp(),lista[day-1][j].get_hum(),lista[day-1][j].get_pre()))
def Menu_1 (lista):
    op=int(input("1- Mostrar para cada variable el día y hora de menor y mayor valor.\n2- Indicar la temperatura promedio mensual por cada hora.\n3-Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato. \nIngrese una opcion (0 Para salir):"))
    while op != 0:
            if op==1:
                variable_op1(lista)
            elif op==2:
                temp_prom(lista)
            elif op==3:
                listado(lista)
            op=int(input("1- Mostrar para cada variable el día y hora de menor y mayor valor.\n2- Indicar la temperatura promedio mensual por cada hora.\n3-Dado un número de día listar los valores de las tres variables para cada hora del día dado.\nIngrese una opcion (0 Para salir):"))
    print("--FIN--")