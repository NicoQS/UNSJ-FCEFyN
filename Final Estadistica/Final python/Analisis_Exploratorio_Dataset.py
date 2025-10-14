# descripcion_datosset.py
import pandas as pd
import numpy as np
import scipy.stats as st
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import math
import seaborn as sns 

def mostrar_descripcion(datos):
    print("Descripcion del datosset")
    print(datos.describe().round(3))
    
    print("\nVarianza:")
    print(datos[['Height', 'Weight', 'Age']].var().round(3))
    
    print("\nMediana:")
    print(datos[['Height', 'Weight', 'Age']].median().round(3))
    
    print("\nModa/s:")
    print(datos[['Height', 'Weight', 'Age']].mode().values.tolist())
    
    #print("\nFrecuencia de valores:")
    #print(datos[['Height', 'Weight', 'Age']].apply(lambda x: x.value_counts()))
    print("\nFrecuencia de valores: ",datos.Height.value_counts(),datos.Weight.value_counts(),datos.Age.value_counts())

    #Un CV bajo indica que los datos están más concentrados alrededor de la media, mientras que un CV alto indica mayor dispersión.
    print("\nCoeficiente de variacion:") 
    cv_height = (datos.Height.std() / datos.Height.mean()).round(3)
    cv_weight = (datos.Weight.std() / datos.Weight.mean()).round(3)
    cv_age = (datos.Age.std() / datos.Age.mean()).round(3)
    print(f"Height: {cv_height}, Weight: {cv_weight}, Age: {cv_age}")
    
    print("\nRecorrido:")
    rango_height = (datos.Height.max() - datos.Height.min()).round(3)
    rango_weight = (datos.Weight.max() - datos.Weight.min()).round(3)
    rango_age = (datos.Age.max() - datos.Age.min()).round(3)
    print(f"Height: {rango_height}, Weight: {rango_weight}, Age: {rango_age}")
    
    #Indica si los datos se encuentran centrados, o si tienen sesgo hacia izquierda o derecha
    print("\nCoeficiente de asimetria:")
    print(datos[['Height', 'Weight', 'Age']].skew().round(3))
    
    #Indica la forma de las colas, una curtosis grande puede indicar un mayor número de datos alejados de la media
    print("\nCoeficiente de curtosis:")
    print(datos[['Height', 'Weight', 'Age']].kurtosis().round(3))
    
    print("\nInformacion del dataset")
    print(datos.info())
    
    print("\nCoeficiente de correlacion Pearson Altura y Peso") #Mide la relación lineal entre dos variables.
    corr = datos.Height.corr(datos.Weight).round(3)
    print(corr)
    
    pearson_result = st.pearsonr(datos.Height, datos.Weight)
    print(f"Pearson: {pearson_result.statistic:.3f}, p-value: {pearson_result.pvalue:.3f}")
    
    x = datos.Height.values.reshape(-1, 1)
    y = datos.Weight
    #cuadrado del coeficiente de correlación de Pearson. Indica la proporción de la variabilidad en la variable dependiente (Weight) que es explicada por la variable independiente (Height).
    print("\nCoeficiente de determinacion R**2") #Indica que tan bien la variable independiente X explica la variabilidad de Y. Un valor de 1 indica que el modelo explica toda la variabilidad de Y.
    result = st.linregress(datos.Height, datos.Weight)
    r_squared = (result.rvalue ** 2).round(3)
    print(f"Coeficiente de determinación (R^2): {r_squared}")
    
    model = LinearRegression()
    model.fit(x, y)
    r_squared_sklearn = model.score(x, y)
    r_squared_sklearn = round(r_squared_sklearn,3)
    print(f"Coeficiente de determinacion por sklearn: {r_squared_sklearn}")
    
    # Calcular los cuartiles
    Q1 = datos["Height"].quantile(0.25)  # Primer cuartil (Q1): 25% de los jugadores tienen una altura de x pulgadas o menos.
    Q3 = datos["Height"].quantile(0.75)  # Tercer cuartil (Q3): 75% de los jugadores tienen una altura de x pulgadas o menos.
    IQR = Q3 - Q1  # Rango intercuartil (IQR): mide la dispersión de los datos en el 50% central de la distribución
    Pq = datos["Weight"].quantile(0.25)  # Primer cuartil (Q1)
    Tq = datos["Weight"].quantile(0.75)  # Tercer cuartil (Q3)
    RIC = Tq - Pq  # Rango intercuartil (IQR)

    # Definir los límites de los outliers
    limite_inferior = Q1 - 1.5 * IQR #Limite del Brazo inferior
    limite_superior = Q3 + 1.5 * IQR
    li = Pq - 1.5 * RIC
    ls = Tq + 1.5 * RIC
    # Definir los límites de los valores extremadamente atípicos
    extremo_inferior = Q1 - 3 * IQR #Valores que sobrepasan los brazos
    extremo_superior = Q3 + 3 * IQR
    ei = Pq - 3 * RIC
    es = Tq + 3 * RIC
    # Identificar outliers
    outliers = datos[(datos["Height"] < limite_inferior) | (datos["Height"] > limite_superior)] #son datos que se encuentran fuera de un rango considerado "normal" para la distribución de los datos.
    extremos = datos[(datos["Height"] < extremo_inferior) | (datos["Height"] > extremo_superior)]
    o2 = datos[(datos["Weight"] < li) | (datos["Weight"] > ls)]
    e2 = datos[(datos["Weight"] < ei) | (datos["Weight"] > es)]

    # Mostrar resultados
    print("\nResultados Altura:")
    print(f"Primer Cuartil (Q1): {Q1}")
    print(f"Tercer Cuartil (Q3): {Q3}")
    print(f"Rango Intercuartil (IQR): {IQR}")
    print(f"Límite Inferior (Outliers): {limite_inferior}")
    print(f"Límite Superior (Outliers): {limite_superior}")
    print(f"Límite Inferior (Extremadamente Atípicos): {extremo_inferior}")
    print(f"Límite Superior (Extremadamente Atípicos): {extremo_superior}")
    print(f"\nValores Atípicos (Outliers):\n{outliers}")
    print(f"\nValores Extremadamente Atípicos:\n{extremos}")
    print("\nResultados Peso:")
    print(f"Primer Cuartil (Q1): {Pq}")
    print(f"Tercer Cuartil (Q3): {Tq}")
    print(f"Rango Intercuartil (IQR): {RIC}")
    print(f"Límite Inferior (Outliers): {li}")
    print(f"Límite Superior (Outliers): {ls}")
    print(f"Límite Inferior (Extremadamente Atípicos): {ei}")
    print(f"Límite Superior (Extremadamente Atípicos): {es}")
    print(f"\nValores Atípicos (Outliers):\n{o2}")
    print(f"\nValores Extremadamente Atípicos:\n{e2}")
    
def Histogramas(datos):
    
    # Calcular el número de bins usando la Regla de Sturges
    N = int(1 + 3.3 * math.log10(len(datos['Height'])))
    N2 = int(1 + 3.3 * math.log10(len(datos['Weight'])))

    # Calcular el rango y el tamaño de los bins
    height_range = datos['Height'].max() - datos['Height'].min()
    weight_range = datos['Weight'].max() - datos['Weight'].min()

    bin_width_height = height_range / N
    bin_width_weight = weight_range / N2

    # Crear los bins
    bins_height = np.arange(datos['Height'].min(), datos['Height'].max() + bin_width_height, bin_width_height)
    bins_weight = np.arange(datos['Weight'].min(), datos['Weight'].max() + bin_width_weight, bin_width_weight)
    
    print(f'\nnumero de intervalos altura: {N}')
    print(f'\nancho del intervalo para la altura: {bin_width_height}')
    print(f'\nintervalo: {bins_height}')
    # Crear la figura con dos subgráficos
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Configuración del estilo
    sns.set_style("whitegrid")

    # Histograma para Height
    sns.histplot(datos["Height"], bins=bins_height, kde=True, color="green", edgecolor="black", alpha=0.7, ax=axes[0])
    axes[0].set_title("Distribución de Alturas (pulgadas)")
    axes[0].set_xlabel("Altura")
    axes[0].set_ylabel("Frecuencia")

    # Histograma para Weight
    sns.histplot(datos["Weight"], bins=bins_weight, kde=True, color="blue", edgecolor="black", alpha=0.7, ax=axes[1])
    axes[1].set_title("Distribución de Pesos (libras)")
    axes[1].set_xlabel("Peso")
    axes[1].set_ylabel("Frecuencia")

    # Ajustar el diseño
    plt.tight_layout()
    plt.show()
    
    plt.figure("Histograma de torta para la posición")
    plt.pie(datos["Position"].value_counts(), labels=datos["Position"].value_counts().index, autopct="%1.1f%%", startangle=90)
    plt.axis("equal")
    plt.title("Distribución de Posiciones")
    
    # Seleccionar el subplot (Altura)
    plt.figure("Diagramas de Caja y Brazos")
    plt.subplots_adjust(wspace=0.5)
    plt.subplot(131)
    plt.xlabel('Altura')
    plt.boxplot([datos.Height], vert=True, labels=[''])
    
    plt.subplot(132)
    plt.xlabel('Peso')
    plt.boxplot([datos.Weight], vert=True, labels=[''])

    
    plt.show()
    plt.close()
    