import pandas as pd
from datetime import timedelta, datetime
import os
from .turno_utils import determinar_turno
from .file_handler import load_data, save_results
from config import TURNO_DIA_INICIO

def procesar_datos_fatiga(ruta_csv, turno_deseado, fecha_inicio, fecha_fin, ruta_salida):
    """
    Procesa los datos de fatiga para identificar alarmas de fatiga 3+*14.
    """
    # Cargar datos
    df = load_data(ruta_csv)
    if df is None:
        return

    # Procesar fechas
    try:
        fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d')
        fecha_fin_dt = fecha_fin_dt + timedelta(days=1)
        fecha_fin_dt = datetime.combine(
            fecha_fin_dt.date(),
            datetime.strptime(TURNO_DIA_INICIO, '%H:%M:%S').time()
        )
        
        df = df[(df['FatigueLogStatusTimestamp'] >= fecha_inicio_dt) &
                (df['FatigueLogStatusTimestamp'] < fecha_fin_dt)]
    except Exception as e:
        print(f"Error al filtrar por rango de fechas: {e}")
        return

    # Filtrar por nivel de fatiga
    df = df[df['FatigueLevel'] > 3]

    # Pre-filtrar operadores con al menos 14 registros
    operadores_validos = df.groupby('OperatorEid').size()
    operadores_validos = operadores_validos[operadores_validos >= 14].index

    df = df[df['OperatorEid'].isin(operadores_validos)]

    # Procesar alarmas usando método similar a SQL
    alarmas = procesar_alarmas_optimizado(df)
    
    # Filtrar por turno
    df_alarmas = pd.DataFrame(alarmas)
    if turno_deseado.lower() in ['dia', 'noche']:
        df_alarmas = df_alarmas[df_alarmas['Turno'] == turno_deseado.lower()]

    # Generar estadísticas
    df_conteo = generar_estadisticas(df_alarmas)
    
    # Guardar resultados
    save_results(df_alarmas, df_conteo, ruta_salida)

def procesar_alarmas_optimizado(df):
    """
    Procesa las alarmas de fatiga usando un método similar al SQL.
    """
    alarmas = []
    
    for operador, grupo in df.groupby('OperatorEid'):
        # Ordenar registros de más reciente a más antiguo
        registros = grupo.sort_values('FatigueLogStatusTimestamp', ascending=False).reset_index(drop=True)
        
        for i in range(len(registros) - 13):
            tiempo_actual = registros.iloc[i]['FatigueLogStatusTimestamp']
            tiempo_anterior = registros.iloc[i + 13]['FatigueLogStatusTimestamp']
            
            # Calcular diferencia de tiempo en segundos
            delta_tiempo = (tiempo_actual - tiempo_anterior).total_seconds()
            
            if delta_tiempo <= 3600:  # 60 minutos en segundos
                turno_alarma = determinar_turno(tiempo_actual)
                alarmas.append({
                    'OperatorEid': operador,
                    'AlarmaTimestamp': tiempo_actual.strftime('%Y-%m-%d %H:%M:%S'),
                    'Turno': turno_alarma,
                    'ShiftStartTimestamp': registros.iloc[i]['ShiftStartTimestamp']
                })
    
    return alarmas

def generar_estadisticas(df_alarmas):
    """
    Genera estadísticas de las alarmas.
    """
    return df_alarmas.groupby('OperatorEid').size().reset_index(name='CantidadAlarmas')