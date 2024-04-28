from Hospital import Paciente, Especialidad, Hospital
import random

names=['Mark', 'Sam', 'Henry','Marcos', 'Juan', 'Martin','Nico', 'Samanta']

if __name__ == "__main__":
    hospital = Hospital()
    
    Frecuencia = int(input("Ingrese la frecuencia de ingreso de pacientes: "))
    tPromTurno = int(input("Ingrese el tiempo promedio de turno: "))
    tPromAtencion = int(input("Ingrese el tiempo promedio de atencion: "))
    
    tTotalSimulacion=int(input("Ingrese el tiempo de simulacion en minutos: "))
    noTurnos = 0
    conTurno = 0
    tTransc = 1
    TotalColaTurno = 0
    TotalPEspecialidad = 0
    
    while tTransc <= tTotalSimulacion:
        if tTransc % tPromTurno == 0 and tTransc <= 60: #Turnos de atencion
            paciente = Paciente(random.choice(names),random.randrange(1500000,5500000))
            especialidad = paciente.getEspecialidad()-1
            
            hospital.anotarPaciente(paciente)
            
            TotalColaTurno += hospital.getTiempoEspera()
            conTurno += 1
            
            print("Paciente {} ingresado a la especialidad {}".format(paciente.getNombre(), hospital.getEspecialidad(especialidad)))
        else:
            noTurnos += 1

        if tTransc > 0 and tTransc % tPromAtencion == 0: #Atencion Medico
            hospital.pacientesAtendidos()
        
        hospital.calcularPromedioEspecialidad()
        tTransc += 1 
    
    print("A ) El tiempo promedio de espera en la cola de turnos es: {} inci".format(TotalColaTurno/conTurno))
    hospital.getPromedioEspecialidad()
    print("C ) Cantidad de pacientes que no obtuvieron turno: {} ".format(noTurnos))