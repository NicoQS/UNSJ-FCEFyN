from Simulador import Simulador

if __name__ == "__main__":
    
    tSimulacion = int(input('Ingrese el tiempo de la simulacion: '))
    tAtencionCajero = int(input('Ingrese el tiempo que el cajero atiende (en minutos): '))
    tFrecuenciaClientes = int(input('Ingrese la frecuencia de los clientes (en minutos): ')) 
    
    Simulacion = Simulador(tSimulacion,tAtencionCajero,tFrecuenciaClientes)
    Simulacion.simular()