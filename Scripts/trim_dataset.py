import pandas as pd
import random

# Cargar el archivo CSV
df = pd.read_csv('US_Accidents_March23.csv')

# Comprobar si el archivo tiene al menos 10,000 filas
if len(df) > 10000:
    # Seleccionar 10,000 filas al azar
    df_sampled = df.sample(n=10000, random_state=1)
else:
    print("El archivo no tiene suficientes filas. Se usarán todas las filas disponibles.")
    df_sampled = df

# Guardar las filas seleccionadas en un nuevo archivo CSV
df_sampled.to_csv('US_Accidents_Sample.csv', index=False)

print("Archivo generado con éxito: US_Accidents_Sample.csv")
