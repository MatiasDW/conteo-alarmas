import pandas as pd
import os

def load_data(ruta_csv):
    """
    Carga y prepara los datos del archivo CSV.
    """
    try:
        df = pd.read_csv(ruta_csv, encoding='utf-16', sep=';')
        df.columns = [col.strip() for col in df.columns]
        df['FatigueLogStatusTimestamp'] = pd.to_datetime(df['FatigueLogStatusTimestamp'])
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def save_results(df_alarmas, df_conteo, ruta_salida):
    """
    Guarda los resultados en un archivo CSV.
    """
    try:
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        
        with open(ruta_salida, 'w', encoding='utf-16', newline='') as f:
            f.write("Alarmas Registradas:\n")
            df_alarmas.to_csv(f, index=False, sep='\t')
            f.write("\n")
            f.write("Conteo de Alarmas por Operador:\n")
            df_conteo.to_csv(f, index=False, sep='\t')
            f.write("\n")
            f.write(f"Numero total de operadores con al menos una alarma:\t{len(df_conteo)}\n")
            f.write(f"Numero total de alarmas registradas:\t{len(df_alarmas)}\n")
            
        print(f"Resultados guardados en: {ruta_salida}")
        print("Proceso completado exitosamente.")
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")