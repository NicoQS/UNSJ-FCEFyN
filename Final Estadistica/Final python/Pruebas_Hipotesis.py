import os
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as st
import matplotlib.pyplot as plt

def Docima_Media_Altura(datos):
    #Dócimas para 𝝁 cuando σ² es desconocida. Y suponiendo una poblacion normal
    #Si la V.A 𝑋 no fuera normalmente distribuida, el Teorema Central del Límite nos garantiza la normalidad aproximada de Z con tal que 𝑛 ≥ 30. 
    media_muestral = datos['Height'].mean()
    desvio_muestral = datos['Height'].std(ddof=1)
    alpha = 0.05
    n = len(datos['Height'])
    # H0: 𝝁 = 73 
    # H1: 𝝁 ≠ 73
    mu = 73
    t = (media_muestral-mu) / (desvio_muestral / np.sqrt(n))
    
    t_critico = st.t.ppf(1-(alpha/2), n-1)
    # Calcular el p-valor (prueba de dos colas)
    n = len(datos['Height'])  # Tamaño de la muestra
    t_obs = abs(t)  # Valor absoluto del estadístico t observado
    p_der = 1 - st.t.cdf(t_obs, df=n-1)
    p_izq = st.t.cdf(-t_obs, df=n-1)
    p_valor = 2 * min(p_izq, p_der)
    
    print(f'\nP-valor izq: {p_izq}')
    print(f'P-valor der: {p_der}')
    print(f'P-valor min: {p_valor}')
    print("\nDocima para la media cuando la varianza es desconocida")
    print(f"Media muestral: {media_muestral:.2f}")
    print(f"Desviación estándar muestral: {desvio_muestral:.2f}")
    print(f"Tamaño de la muestra: {n}")
    print(f"Valor crítico: {t_critico:.4f}")
    #print(f"Estadístico de prueba: {t:.2f}")
    print(f'\nEstadistico de prueba t absoluto: {abs(t):.4f}')
    print(f"p-valor eligiendo el minimo valor entre las dos comparaciones: {p_valor:.4f}\n")
    
    print(f"No rechazamos la hipotesis nula H0: No hay evidencia suficiente para afirmar que la media es diferente de 73."
            if abs(t) < t_critico else  
           "Rechazamos la hipotesis nula H0: Hay evidencia suficiente para afirmar que la media es diferente de 73."
        )
    
    
    print(f"Rechazamos la hipotesis nula H0: Hay evidencia suficiente para afirmar que la media es diferente de 73."
      if p_valor < alpha else  
      "No rechazamos la hipotesis nula H0: No hay evidencia suficiente para afirmar que la media es diferente de 73."
        )
    
    # Crear un rango de valores para t
    x = np.linspace(-10, 10, 1000)
    
    # Calcular la densidad de probabilidad de la distribución t
    y = st.t.pdf(x, n-1)
    
    # Crear la figura
    plt.figure(figsize=(10, 6))
    
    # Graficar la distribución t
    plt.plot(x, y, label=f"Distribución t (df={n-1})", color="blue")
    
    # Sombrear las regiones críticas (dos colas)
    t_critico = st.t.ppf(1 - alpha/2, n-1)
    x_izq = np.linspace(-10, -t_critico, 500)
    x_der = np.linspace(t_critico, 10, 500)
    plt.fill_between(x_izq, st.t.pdf(x_izq, n-1), color="red", alpha=0.5, label="Región crítica (cola izquierda)")
    plt.fill_between(x_der, st.t.pdf(x_der, n-1), color="red", alpha=0.5, label="Región crítica (cola derecha)")
    
    # Marcar el valor observado de t
    plt.axvline(abs(t), color="green", linestyle="--", label=f"t observado abs= {abs(t):.2f}")
    
    # Añadir etiquetas y leyenda
    plt.title("Distribución t de Student y Regiones Críticas")
    plt.xlabel("Valor de t")
    plt.ylabel("Densidad de probabilidad")
    plt.legend()
    plt.grid(True)
    
    # Mostrar la gráfica
    plt.show()

def Bondad_Ajuste_Peso(datos):
  # Prueba de Shaphiro Wilk para comprobar si los datos siguen una distribución normal.
  # H0: Los datos siguen una distribucion normal
  # H1: Los datos no siguen una distribucion normal
  
  alpha = 0.05
  media_muestral = datos['Weight'].mean()
  desvio_estandar = datos['Weight'].std(ddof=1)  # ddof=1 para usar n-1 en el denominador
  estadistico_p, p_valor = st.shapiro(datos['Weight'])
  
  print("\nBondad de Ajuste para una distribucion normal")
  print(f'Media muestral: {media_muestral}')
  print(f'Desvío estándar muestral: {desvio_estandar}')
  print(f'Estadístico de prueba: {estadistico_p}')
  print(f'P-valor: {p_valor}\n')

  # Interpretar el resultado
  if p_valor < alpha:
      print('Los datos no siguen una distribución normal (se rechaza H0)')
  else:
      print('Los datos parecen seguir una distribución normal (no se rechaza H0)')

def P_Independencia_Edad_Posicion(datos):
  #H0: La edad y la posición del jugador son independientes.
  #H1: Hay una relación entre la edad y la posición del jugador.
  # Convertimos la edad en categorías 
  datos['Grupo_Edad'] = pd.cut(datos['Age'], bins=[20, 25, 30, 35, 40], labels=['20-25', '25-30', '30-35', '35-40'], right=False)

  #Crear la tabla de contingencia
  tabla_contingencia = pd.crosstab(datos['Position'], datos['Grupo_Edad'])

  #Aplicar la prueba de chi-cuadrado
  chi2, p_valor, dof, expected = st.chi2_contingency(tabla_contingencia)
  tabulado = st.chi2.ppf(1-0.05,(7-1)*(4-1)) # tambien se puede usar dof en vez del producto

  print("\nTabla de contingencia:\n", tabla_contingencia)
  print(f"\n Estadistico de prueba: {chi2:.4f}")
  print(f'Valor tabulado: {tabulado}')
  print(f"Grados de libertad: {dof}")
  print(f"P-valor: {p_valor:.4f}")
  print(f'Tabla de Frecuencias Esperadas \n{expected}') #Muestra cuántos datos se esperaría en cada celda si las variables fueran independientes.

  alpha = 0.05  #Nivel de significancia
  if p_valor < alpha:
      print("\nSe rechaza H0: Hay relación entre la edad y la posición del jugador.")
  else:
      print("\nNo se rechaza H0: No hay evidencia suficiente para decir que están relacionadas.")
