import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sn 
import os, math
from sklearn.linear_model import LinearRegression 
import Analisis_Exploratorio_Dataset as dd
import Estimaciones as es
import Pruebas_Hipotesis as hp
import Regresion_Lineal as rl

def cargadataset():
    data = pd.read_csv('Baseball_Players_Discreto_Correlacion.csv')
    # Agregar un pequeño ruido aleatorio a los valores de Height y Weight
    np.random.seed(42)  # Para reproducibilidad: que al ejecutarlo siempre de los mismos valores
    ruido_height = np.random.normal(loc=0, scale=0.5, size=len(data))  # Ruido para Height
    ruido_weight = np.random.normal(loc=0, scale=2, size=len(data))    # Ruido para Weight
    
    data['Height'] += (ruido_height).round(1)
    data['Weight'] += (ruido_weight).round(1)
    print(data.head(10))
    return data

def mostrarpuntos(datos):
    plt.figure(figsize=(8,6))
    #sn.scatterplot(x='Height',y='Weight',data=datos,color='b',s=100)
    plt.scatter(datos['Height'], datos['Weight'], color='blue', alpha=0.7, edgecolors='w')  # Scatter plot
    plt.title('Grafico de dispersion: Altura vs Peso')
    plt.xlabel('Altura (Pulgadas)')
    plt.ylabel('Peso (Libras)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    datos = cargadataset()
    
    
    mostrarpuntos(datos)
    dd.mostrar_descripcion(datos)
    op = int(input("\nVer Histogramas? 1 para ver: "))
    if op == 1:
        dd.Histogramas(datos)
        exit
    es.estimacion_puntual_Altura(datos)
    es.estimacion_por_intervalos_Peso(datos)
    hp.Docima_Media_Altura(datos)
    hp.Bondad_Ajuste_Peso(datos)
    hp.P_Independencia_Edad_Posicion(datos)
    rl.coef(datos)
    rl.R_L(datos)
    rl.analisis_residuos(datos)
    
    