import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import scipy.stats as st
import seaborn as sns
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson
def coef(datos):
    corr = datos.Height.corr(datos.Weight).round(3)
    print(f"\nCoeficiente de correlacion Pearson Altura y Peso {corr:.3f}") #Mide la relación lineal entre dos variables.
    
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

def R_L(datos):
    #Predecir el peso (Weight) en función de la altura (Height)
    
    X = datos[['Height']]  # Variable independiente (altura)
    y = datos['Weight']    # Variable dependiente (peso)

    #Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)  # Entrenar el modelo con los datos de entrenamiento

    #Hacer predicciones con el conjunto de prueba
    y_pred = modelo.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'\nError cuadrático medio (MSE): {mse:.2f}')
    print(f'Coeficiente de determinación (R²): {r2:.2f}')
    mse_manual = np.mean((y_test - y_pred) ** 2)
    print(f'\nMSE: {mse_manual:.2f}\n')
    
    # Cálculo manual de la varianza de los residuos (S_e^2)
    sce = np.sum((y_test - y_pred) ** 2)  # Suma de cuadrados de los errores (SCE)
    n = len(y_test)  # Número de observaciones
    se2 = sce / (n - 2)  # Varianza de los residuos
    se = np.sqrt(se2)  # Desviación estándar de los residuos

    print(f'\nVarianza de los residuos (S_e^2): {se2:.2f}')
    print(f'Desviación estándar de los residuos (S_e): {se:.2f}\n')
    
    #Pendiente m (2.50): Indica que, por cada pulgada adicional de altura, el peso aumenta en aproximadamente 2.50 libras.
    pendiente = modelo.coef_[0]  # Coeficiente de la variable independiente (Height)
    ordenada = modelo.intercept_  #Ordenada b (valor de y cuando x = 0)

    # Mostrar la ecuación de la recta
    print(f"Ecuación de la recta: y = {pendiente:.2f}x + {ordenada:.2f}")
    altura = 70
    peso_predicho = pendiente * altura + ordenada
    print(f"Para una altura de {altura} pulgadas, el peso predicho es: {peso_predicho:.2f} libras\n")

    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', label='Datos reales')  
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Línea de regresión: y=2.50x−0.8') 
    # Líneas de desviación estándar (bandas de confianza)
    X_sorted = np.sort(X_test.values.flatten())  # Ordenar valores de X
    y_pred_sorted = modelo.predict(X_sorted.reshape(-1, 1))  # Predicción ordenada
    plt.plot(X_sorted, y_pred_sorted + se, color="green", linestyle="--", label="± Se")
    plt.plot(X_sorted, y_pred_sorted - se, color="green", linestyle="--")
    plt.title('Regresión Lineal: Altura vs Peso', fontsize=16)
    plt.xlabel('Altura (inches)', fontsize=12)
    plt.ylabel('Peso (lbs)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    
def analisis_residuos(datos):
    x = datos['Height']
    y = datos['Weight']
    # Ajustar modelo de regresión lineal
    X_const = sm.add_constant(x)  # Agregar constante para la regresión
    modelo = sm.OLS(y, X_const).fit()

    # Obtener residuos y valores ajustados
    residuos = modelo.resid
    valores_ajustados = modelo.fittedvalues

    # Calcular la Suma de Cuadrados del Error (SCE)
    SCE = np.sum(residuos**2)
    se = np.sqrt(SCE / (len(y) - 2))
    
    # --- Gráfico 1: Residuos vs Valores Ajustados (Homocedasticidad) ---
    plt.figure(figsize=(6, 4))
    #sns.scatterplot(x=valores_ajustados, y=residuos, alpha=0.7)
    sns.scatterplot(x=range(len(residuos)), y=residuos, alpha=0.7)
    plt.axhline(y=0, color='red', linestyle='dashed')
    plt.axhline(y=2 * se, color="green", linestyle="--", label="2 * Se")
    plt.axhline(y=-2 * se, color="green", linestyle="--", label="-2 * Se")
    plt.xlabel("Índice")
    plt.ylabel("Residuos")
    #plt.title("Residuos vs Valores Ajustados (Homocedasticidad)")
    plt.title("Residuos vs Índice (Homocedasticidad)")
    plt.show()

    # --- Gráfico 2: QQ-Plot (Normalidad de los residuos) ---
    sm.qqplot(residuos, line='45', fit=True)
    plt.title("QQ-Plot de los Residuos")
    plt.show()

    # --- Gráfico 3: Residuos vs Índice (Independencia de los errores) ---
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=range(len(residuos)), y=residuos, alpha=0.7)
    plt.axhline(y=0, color='red', linestyle='dashed')
    plt.axhline(y=2 * se, color="green", linestyle="--", label="2 * Se")
    plt.axhline(y=-2 * se, color="green", linestyle="--", label="-2 * Se")
    plt.xlabel("Índice")
    plt.ylabel("Residuos")
    plt.title("Residuos vs Índice (Independencia)")
    plt.show()


    # Verificar que el 95% de los residuos estén dentro de la banda (-2*Se, 2*Se)
    dentro_banda = np.sum((residuos >= -2 * se) & (residuos <= 2 * se)) / len(residuos)
    print(f"Porcentaje de residuos dentro de la banda (-2*Se, 2*Se): {dentro_banda * 100:.2f}%\n")
    
    # Prueba de homocedasticidad de Breusch-Pagan
    from statsmodels.stats.diagnostic import het_breuschpagan
    bp_test = het_breuschpagan(residuos, X_const)
    print(f"Breusch-Pagan Test: p-valor={bp_test[1]} , Estadístico={bp_test[0]}\n")
    
    # Calcular la media de los residuos
    media_residuos = np.mean(residuos)
    print(f"Media de los residuos: {media_residuos}")
    # Calcular el error estándar de la media de los residuos
    error_estandar = st.sem(residuos)

    # Prueba t para verificar si la media es significativamente diferente de cero
    t_stat, p_value = st.ttest_1samp(residuos, 0)
    print(f"T-statistic: {t_stat}")
    print(f"P-valor: {p_value}\n")

    # Evaluación del resultado
    if p_value > 0.05:
        print("No se rechaza la hipótesis nula: La media de los residuos es aproximadamente cero.\n")
    else:
        print("Se rechaza la hipótesis nula: La media de los residuos es significativamente diferente de cero.\n")

    # Calcular el intervalo de confianza
    intervalo_confianza = st.t.interval(0.95, len(residuos)-1, loc=media_residuos, scale=error_estandar)

    print(f"Intervalo de confianza al {0.95*100}% para la media de los residuos: {intervalo_confianza}\n")
    
    ks_statistic, p_value = st.kstest(residuos, 'norm', args=(0, np.std(residuos, ddof=1)))
    
    print("\nPrueba de Kolmogorov-Smirnov:")
    print(f"Estadístico KS: {ks_statistic:.4f}")
    print(f"Valor p: {p_value:.4f}")

    # Interpretación
    if p_value > 0.05:
        print("\nNo se rechaza la hipótesis nula: Los residuos siguen una distribución normal.")
    else:
        print("\nSe rechaza la hipótesis nula: Los residuos NO siguen una distribución normal.")
    
    
    # Prueba de Durbin-Watson
    durbin_watson_stat = durbin_watson(residuos)

    # Mostrar resultados
    print("\nPrueba de Durbin-Watson:")
    print('Nivel de significancia: 0.01')
    print('DL: 1.664')
    print('DU: 1.884')
    print('4-DU: 2.116')
    print('4-DL: 2.336')
    print(f"Estadístico de Durbin-Watson: {durbin_watson_stat:.4f}")

    # Interpretación
    if durbin_watson_stat < 1.5:
        print("\nEvidencia de autocorrelación positiva.")
    elif durbin_watson_stat > 2.5:
        print("\nEvidencia de autocorrelación negativa.")
    else:
        print("\nNo hay evidencia de autocorrelación (los residuos son independientes).")

    