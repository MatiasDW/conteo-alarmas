# Sistema de Análisis de Fatiga - Documentación Técnica

h1. Descripción General
Este sistema analiza patrones de fatiga en operadores basado en registros temporales, identificando secuencias de alarmas 3+ en períodos específicos.

h2. Características Principales
* Análisis de fatiga por turnos (día/noche)
* Detección de secuencias 3+ x 14 en ventanas de 60 minutos
* Generación de reportes estadísticos
* Filtrado por rangos de fechas
* Procesamiento optimizado de datos

h2. Arquitectura del Sistema

h3. Estructura de Archivos
{code}
proyecto/
├── main.py              # Punto de entrada principal
├── config.py            # Configuraciones globales
└── utils/
    ├── __init__.py
    ├── data_processor.py    # Procesamiento principal
    ├── file_handler.py      # Manejo de archivos
    ├── input_validator.py   # Validación de entradas
    └── turno_utils.py       # Utilidades de turnos
{code}

h2. Configuración
h3. Parámetros Principales
|| Parámetro || Descripción || Valor por Defecto ||
| INPUT_PATH | Ruta del archivo CSV de entrada | _configurable_ |
| OUTPUT_PATH | Ruta del archivo de resultados | _configurable_ |
| TURNO_DIA_INICIO | Hora de inicio turno día | 08:00:00 |
| TURNO_DIA_FIN | Hora de fin turno día | 20:00:00 |
| MIN_REGISTROS | Mínimo de registros requeridos | 14 |
| VENTANA_TIEMPO_MAX | Ventana máxima en minutos | 60 |

h2. Flujo de Procesamiento
# Carga de datos desde CSV
# Validación de fechas y turno
# Filtrado por nivel de fatiga (>3)
# Pre-filtrado de operadores válidos
# Procesamiento de alarmas optimizado
# Generación de estadísticas
# Exportación de resultados

h2. Algoritmo de Detección de Alarmas
{code:java}
Para cada operador:
    1. Ordenar registros por timestamp (descendente)
    2. Para cada secuencia de 14 registros:
        - Calcular diferencia de tiempo
        - Si diferencia ≤ 60 minutos:
            * Generar alarma
            * Registrar turno y timestamp
{code}

h2. Diferencias con SQL
h3. Ventajas del Sistema Actual
* Procesamiento en memoria más eficiente
* Mayor flexibilidad en la manipulación de datos
* Facilidad de mantenimiento y modificación
* Mejor manejo de cortes de fecha/turno

h3. Comparativa con SQL
|| Característica || Python || SQL ||
| Procesamiento | En memoria | En base de datos |
| Flexibilidad | Alta | Media |
| Velocidad | Optimizada para datasets medianos | Mejor para grandes volúmenes |
| Mantenibilidad | Más modular | Menos modular |

h2. Uso del Sistema

h3. Requisitos Previos
* Python 3.x
* pandas
* datetime

h3. Ejecución
{code:bash}
python main.py
{code}

h3. Entradas Requeridas
# Turno a analizar (día/noche/todos)
# Fecha de inicio (YYYY-MM-DD)
# Fecha de fin (YYYY-MM-DD)

h2. Formato de Salida
h3. Archivo de Resultados
# Alarmas Registradas
# Conteo por Operador
# Estadísticas Globales

h2. Mantenimiento y Soporte
h3. Consideraciones Importantes
* Validar formato de fechas
* Verificar rutas de archivos
* Monitorear uso de memoria
* Revisar logs de errores

h2. Actualizaciones Recientes
* Optimización del procesamiento de alarmas
* Mejora en el manejo de fechas límite
* Implementación de pre-filtrado de operadores
* Corrección del corte de turno noche

h2. Contacto y Soporte
Para soporte técnico o consultas:
* Equipo de Desarrollo
* Administrador del Sistema