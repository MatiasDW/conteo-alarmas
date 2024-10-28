from datetime import datetime

def validate_turno():
    """
    Valida y obtiene el turno del usuario.
    """
    turno = ''
    while turno.lower() not in ['dia', 'noche', 'todos']:
        turno = input("Ingrese el turno a analizar ('dia', 'noche' o 'todos'): ").strip().lower()
        if turno not in ['dia', 'noche', 'todos']:
            print("Entrada inválida. Por favor, ingrese 'dia', 'noche' o 'todos'.")
    return turno

def validate_dates(fecha_inicio, fecha_fin):
    """
    Valida el formato de las fechas.
    """
    try:
        datetime.strptime(fecha_inicio, '%Y-%m-%d')
        datetime.strptime(fecha_fin, '%Y-%m-%d')
        return True
    except ValueError:
        return False