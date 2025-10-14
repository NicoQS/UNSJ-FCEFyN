import numpy as np
import scipy.stats as st 
import matplotlib.pyplot as plt

#E(estimador - parametro)**2 == Var(estimador) + (parametro - E(estimador))**2
#Insesgado: E(estimador) = parametro
#Sesgo: E(estimador) - parametro
def errorCM(estimador,valor_exacto):
    return np.var(estimador) + (valor_exacto - np.mean(estimador))**2

def estimacion_puntual_Altura(datos):
    estimacion_media_muestral = sum(datos['Height']) / len(datos['Height'])
    #est_media = datos['Height'].mean()
    #ecm_media = errorCM([estimacion_media_muestral], parametro_media)
    #ecm = (parametro_media - estimacion_media_muestral)**2
    
    #print("\nEstimacion Puntual de la Media:")
    print("\nEstimacion Puntual para la Media: {:.5f}".format(estimacion_media_muestral))
    #print("Estimacion de la media. Estimador 2: {:.5f}".format(est_media))

    #print("Error Cuadratico Medio: {:.2f}".format(ecm_media))
    #print("Error Cuadratico Medio: {:.2f}".format(ecm))

    #print('Parametro media: {:.2f}'.format(parametro_media))
    
    estimacion_varianza_muestral = sum((datos['Height'] - estimacion_media_muestral)**2) / (len(datos['Height'])-1)
    #est_varianza = np.var(datos['Height'],ddof=1)
    #ecm_varianza = errorCM([estimacion_varianza_muestral],parametro_varianza)
    #ecm1 = (parametro_varianza - estimacion_varianza_muestral)**2
    
    #print("\nEstimacion Puntual de la Varianza:")
    print("\nEstimacion Puntual para la Varianza: {:.5f}".format(estimacion_varianza_muestral))
    #print("Estimacion de la varianza. Estimador 2: {:.5f}".format(est_varianza))
    #print("Error Cuadratico Medio: {:.2f}".format(ecm_varianza))
    #print("Error Cuadratico Medio: {:.2f}".format(ecm1))

    #print('Parametro varianza: {:.2f}'.format(parametro_varianza))
    
    #ier = estimacion_varianza_muestral / est_varianza
    
    #print(f'\nIndice de Eficiencia Relativa: {ier}')
    #if ier < 1:
    #    print(f'\nComo el Indice se encuentra en el rango (0,1), el mejor estimador es el estimador 2')
    #elif ier > 1:
    #    print(f'\nComo el Indice se encuentra en el rango (1,+∞), el mejor estimador es el estimador 1')
    #else:
    #    print(f'\nEl Indice nos indica que el cociente es 1, por lo que los estimadores son iguales')
        
def estimacion_por_intervalos_Peso(datos):
    #Intervalo para la media con varianza desconocida
    alpha = 0.05 #Nivel de confianza
    grado_confianza = 1 - alpha
    
    media_muestral = datos['Weight'].mean()
    desviacion_muestral = datos['Weight'].std()
    n = len(datos['Weight'])
    z = st.t.ppf(1 - (alpha / 2), n - 1) #ppf: Percent Point Function (Función de Punto Percentil), también conocida como la función cuantil o inversa de la función de distribución acumulada (CDF).
    error_estimacion = z * (desviacion_muestral/np.sqrt(n))
    
    print("\nIntervalo de confianza para la media de una distribución normal con varianza desconocida:")
    print("Media muestral: {:.2f}".format(media_muestral))
    print('Desvio muestral: {:.2f}'.format(desviacion_muestral))
    print('Valor critico de la distribucion t de student: ',z)
    print(f'Nivel de significación: {alpha}')
    print("Error de estimacion: ±{:.2f}".format(error_estimacion))
    print(f"Intervalo de confianza para la media:({media_muestral-error_estimacion:.2f} <μ< {media_muestral+error_estimacion:.2f})")
    print("El intervalo tiene una longitud de: {:.2f}".format(2*error_estimacion))
    print(f"Se obtiene un intervalo centrado en X̅, que contendra al parametro μ, en el {grado_confianza*100}% de las veces")
    
    #Intervalo para la varianza de una distribución normal. Suponemos una distribucion normal
    varianza_muestral = np.var(datos['Weight'], ddof=1)  # Varianza muestral (ddof=1 para corrección de Bessel n-1)

    # Cálculo de los valores críticos Chi-cuadrado
    chi2_critico_inf = st.chi2.ppf(alpha/2, n-1)  # Cuantil inferior
    chi2_critico_sup = st.chi2.ppf(1 - alpha/2, n-1)  # Cuantil superior

    # Cálculo del intervalo de confianza
    limite_inf = ((n-1) * varianza_muestral) / chi2_critico_sup
    limite_sup = ((n-1) * varianza_muestral) / chi2_critico_inf 
    
    print("\nIntervalo de confianza para la varianza de una distribución normal:")
    print("varianza muestral: {:.2f}".format(varianza_muestral))
    print(f"Valor crítico de Chi-cuadrado (inferior): {chi2_critico_inf:.2f}")
    print(f"Valor crítico de Chi-cuadrado (superior): {chi2_critico_sup:.2f}")
    print(f"Intervalo de confianza para la varianza:({limite_inf:.2f} <σ²< {limite_sup:.2f})")
    print(f"El intervalo de confianza contendrá el valor de σ² en el {grado_confianza*100}% de las muestras.")
    
    # Gráfico del intervalo de confianza para la media
    #plt.figure(figsize=(10, 6))
    
    # Distribución normal basada en el peso (Weight)
    #x = np.linspace(170, 190, 100)
    #p = st.norm.pdf(x, loc=media_muestral, scale=desviacion_muestral / np.sqrt(n))
    #plt.plot(x, p, 'k-', linewidth=2, label='Distribución T student')
#
    #plt.axvline(media_muestral, color='b', linestyle='dashed', linewidth=2, label=f'Media muestral(μ): {media_muestral:.2f}')
    #plt.axvline(media_muestral - error_estimacion, color='r', linestyle='dashed', linewidth=2, label=f'Límite inferior: {media_muestral - error_estimacion:.2f}')
    #plt.axvline(media_muestral + error_estimacion, color='r', linestyle='dashed', linewidth=2, label=f'Límite superior: {media_muestral + error_estimacion:.2f}')
    #
    #plt.title('Intervalo de Confianza para la Media')
    #plt.xlabel('Peso (Pounds)')
    #plt.ylabel('Densidad')
    #plt.legend()
    #plt.show()
    # Gráfico del intervalo de confianza para la media
    plt.figure(figsize=(10, 6))
    #x = np.linspace(media_muestral - 4 * desviacion_muestral / np.sqrt(n), media_muestral + 4 * desviacion_muestral / np.sqrt(n), 100)
    x = np.linspace(170, 190, 100)
    p = st.t.pdf(x, df=n-1, loc=media_muestral, scale=desviacion_muestral / np.sqrt(n))
    plt.plot(x, p, 'k-', linewidth=2, label='Distribución t de Student')

    plt.axvline(media_muestral, color='b', linestyle='dashed', linewidth=2, label=f'Media muestral (X̅): {media_muestral:.2f}')
    plt.axvline(media_muestral - error_estimacion, color='r', linestyle='dashed', linewidth=2, label=f'Límite inferior: {media_muestral - error_estimacion:.2f}')
    plt.axvline(media_muestral + error_estimacion, color='r', linestyle='dashed', linewidth=2, label=f'Límite superior: {media_muestral + error_estimacion:.2f}')

    plt.title('Intervalo de Confianza para la Media')
    plt.xlabel('Peso (Pounds)')
    plt.ylabel('Densidad')
    plt.legend()
    plt.show()

    # Gráfico de Chi-cuadrado
    x = np.linspace(0, chi2_critico_sup * 1.1, 1000)
    y = st.chi2.pdf(x, n - 1)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'k-', label=f'Chi-cuadrado (df={n-1})')
    plt.axvline(varianza_muestral, color='b', linestyle='dashed', linewidth=2, label=f'Varianza muestral(S²): {varianza_muestral:.2f}')
    plt.axvline(limite_inf, color='r', linestyle='dashed', linewidth=2, label=f'Límite inferior: {limite_inf:.2f}')
    plt.axvline(limite_sup, color='r', linestyle='dashed', linewidth=2, label=f'Límite superior: {limite_sup:.2f}')

    plt.title('Curva Chi-cuadrado e Intervalo de Confianza para la Varianza')
    plt.xlabel('Valor Chi-cuadrado')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend()
    plt.show()
    