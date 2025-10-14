import pandas as pd

# Cargar el dataset
df = pd.read_csv("water_potability.csv")

# Mezclar aleatoriamente el dataset (sin modificar el original)
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Dividir a la mitad
n = len(df_shuffled) // 2
poblacion_1 = df_shuffled.iloc[:n].copy()
poblacion_2 = df_shuffled.iloc[n:].copy()

print(f"Población 1: {len(poblacion_1)} registros")
print(f"Población 2: {len(poblacion_2)} registros")

poblacion_1.to_csv("poblacion_1.csv", index=False)
poblacion_2.to_csv("poblacion_2.csv", index=False)