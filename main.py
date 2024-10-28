import os
from datetime import datetime
from utils.data_processor import procesar_datos_fatiga
from utils.input_validator import validate_dates, validate_turno
from config import INPUT_PATH, OUTPUT_PATH

def main():
    # Solicitar y validar el turno
    turno = validate_turno()
    
    # Solicitar y validar fechas
    fecha_inicio = input("Ingrese la fecha de inicio (formato YYYY-MM-DD): ").strip()
    fecha_fin = input("Ingrese la fecha de fin (formato YYYY-MM-DD): ").strip()
    
    if not validate_dates(fecha_inicio, fecha_fin):
        print("Formato de fecha incorrecto. Por favor, use el formato YYYY-MM-DD.")
        return

    # Procesar los datos
    procesar_datos_fatiga(INPUT_PATH, turno, fecha_inicio, fecha_fin, OUTPUT_PATH)

if __name__ == "__main__":
    main()