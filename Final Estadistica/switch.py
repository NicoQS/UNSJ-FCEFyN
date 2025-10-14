#Cambiar 0 por NoPotable y 1 Por Potable.py lee archivo water_potability csv

""" import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('water_potability.csv')
# Reemplazar 0 por 'No Potable' y 1 por 'Potable' en la columna 'Potability'
df['Potability'] = df['Potability'].replace({0: 'No Potable', 1: 'Potable'})
# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('water_potability_modified.csv', index=False) """

# Eliminar filas con valores vacios en columnas específicas
import pandas as pd
# Cargar el dataset
df = pd.read_csv("water_potability.csv")
# Eliminar filas con valores vacíos en columnas específicas
df_cleaned = df.dropna(subset=['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'])
# Guardar el DataFrame limpio en un nuevo archivo CSV
df_cleaned.to_csv('water_potability_cleaned.csv', index=False)
