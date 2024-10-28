from datetime import datetime
from config import TURNO_DIA_INICIO, TURNO_DIA_FIN

def determinar_turno(timestamp):
    """
    Determina el turno al que pertenece un timestamp dado.
    """
    hora = timestamp.time()
    if (datetime.strptime(TURNO_DIA_INICIO, '%H:%M:%S').time() <= 
        hora < 
        datetime.strptime(TURNO_DIA_FIN, '%H:%M:%S').time()):
        return 'dia'
    return 'noche'