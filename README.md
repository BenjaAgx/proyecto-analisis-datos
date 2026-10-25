# Evolución del Turismo Nacional e Internacional (Proyecto 14)

## Portada
- Institución: Universidad de Chile
- Asignatura: Programacion Avanzada
- Título del proyecto: Evolución del Turismo Nacional e Internacional
- Nombre de los integrantes: Enzo Illanes, Benjamin Aguayo y Jaime Panguinao
- Carrera: Ingenieria Civil Plan Común
- Docente: Alex Flores Fuentealba
- Fecha de entrega: 27 de Octubre 2026
- Enlace al repositorio: https://github.com/enzoillanes6-art/proyecto-analisis-datos

## Descripción del problema
El turismo es una actividad económica clave para el desarrollo regional y nacional, pero su comportamiento cambia según la temporada, la región y la nacionalidad de los visitantes. Esta variación afecta la planificación del servicio, la ocupación de alojamientos y la toma de decisiones por parte de la autoridad y del sector privado. El problema que se investiga es la falta de una visión clara sobre la tendencia del flujo turístico en los últimos años y la necesidad de proyectar la demanda esperada para el próximo período.

La pregunta principal del proyecto es: ¿Qué tendencia presenta el turismo en los últimos años? El objetivo general es analizar la evolución del flujo de turistas nacionales e internacionales, identificar estacionalidad y comparar regiones para proyectar la cantidad esperada para el próximo año. Los objetivos específicos son: (1) calcular visitantes promedio por mes, (2) identificar temporadas de mayor demanda, (3) comparar el comportamiento entre regiones y nacionalidades, y (4) proyectar la cantidad esperada de visitantes para el próximo año.

Los usuarios potenciales de estos resultados son autoridades públicas de turismo, operadores de alojamiento, agencias de viajes, municipios y comunidades dependientes del turismo. Las decisiones que pueden apoyarse con este análisis incluyen campañas de promoción, programación operativa, planificación de infraestructura y estrategias de temporada.

## Fuente de datos
El proyecto utiliza un conjunto de datos sintético diseñado para representar la evolución de turismo nacional e internacional por año, mes, región y nacionalidad. Esta fuente es adecuada para la primera etapa del proyecto porque permite analizar tendencias, estacionalidad y comparación regional sin publicar información sensible ni privada.

| Elemento | Información del proyecto |
|---|---|
| Nombre del conjunto de datos | Evolución del turismo nacional e internacional |
| Organización responsable | Proyecto académico |
| URL o ubicación del archivo | datos/dataset.csv |
| Fecha de consulta | 2026-10-24 |
| Formato | CSV |
| Cantidad aproximada de registros | 180 |
| Cantidad de variables | 8 |
| Período cubierto | 2021-2025 |
| Licencia o condición de uso | Uso académico y sintético |
| Frecuencia de actualización | Mensual |
| Limitaciones detectadas | Datos sintéticos y no oficiales |

## Diccionario de datos

| Variable | Descripción | Tipo original | Tipo esperado | Unidad o formato | Valores permitidos | ¿Permite nulos? | Ejemplo |
|---|---|---|---|---|---|---|---|
| año | Año de la observación | int | int64 | YYYY | 2021-2025 | No | 2024 |
| mes | Mes del registro | str | object | Texto | Enero-Diciembre | No | Enero |
| region | Región del destino | str | object | Texto | Metropolitana, Norte, Centro, Sur | No | Metropolitana |
| nacionalidad | Tipo de visitante | str | object | Texto | Nacional, Internacional | No | Internacional |
| visitantes | Visitas registradas | int | int64 | personas | Enteros positivos | No | 24500 |
| pernoctaciones | Noches de alojamiento | int | int64 | noches | Enteros positivos | Sí | 54000 |
| tasa_ocupacion | Porcentaje de ocupación | float | float64 | % | 0-100 | Sí | 62.4 |
| temporada | Categoría estacional | str | object | Texto | Alta, Media, Baja | No | Alta |

## Diseño del pipeline
```text
Fuente de datos
      ↓
Descarga o recepción
      ↓
Almacenamiento en datos/
      ↓
Carga con Pandas
      ↓
Validación de estructura
      ↓
Limpieza y transformación
      ↓
Análisis exploratorio
      ↓
Visualización
      ↓
Interpretación
      ↓
Informe final
```

| Etapa | Entrada | Proceso | Salida | Herramienta |
|---|---|---|---|---|
| Obtención | Fuente original | Generar o recopilar datos | Archivo CSV | CSV local |
| Carga | Archivo original | Leer archivo | DataFrame | Pandas |
| Validación | DataFrame | Revisar estructura y tipos | Diagnóstico inicial | Pandas |
| Limpieza | Datos originales | Corregir nulos y duplicados | Datos limpios | Pandas |
| Análisis | Datos limpios | Calcular indicadores | Resultados | Pandas y NumPy |
| Visualización | Resultados | Crear gráficos | Figuras | Matplotlib |
| Reporte | Resultados y figuras | Interpretar hallazgos | Informe final | PDF |

El proyecto combina un enfoque de análisis exploratorio con una proyección anual de visitantes. Se almacenan los datos en la carpeta `datos/`, se validan columnas y tipos con Pandas, y se evaluarán valores nulos, duplicados y anomalías. Las transformaciones esperadas incluyen limpieza de columnas, estandarización de categorías y agregación por mes y región. Los resultados esperados son estadísticas descriptivas, comparación por zona y proyección para el próximo año.

## Estructura del repositorio
```text
proyecto/
├── datos/
│   ├── dataset.csv
│   └── README.md
├── reportes/
│   └── avance_1.pdf
├── src/
│   ├── __init__.py
│   └── carga.py
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
```

## Ejecución
1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar: `python main.py`

## Dependencias
```text
pandas
```

## Conclusión
La fuente seleccionada permite abordar el problema porque ofrece una estructura útil para estudiar la evolución del turismo por año, mes, región y nacionalidad. El conjunto presenta variables relevantes para responder la pregunta principal, como visitantes, pernoctaciones, tasa de ocupación y estacionalidad. Los problemas iniciales esperados incluyen valores faltantes, registros duplicados y posibles inconsistencias de texto en categorías. En la siguiente etapa se realizará una limpieza más profunda, un análisis exploratorio por mes y región y una proyección del flujo turístico para el próximo año.

## Preguntas finales
- ¿Qué criterio utilizaron para seleccionar el problema? Se priorizó un tema económico y social con fuerte impacto en la planificación regional.
- ¿Por qué la fuente elegida es adecuada? Porque permite analizar la tendencia del turismo por región y temporada.
- ¿Qué variable podría generar mayores dificultades durante la limpieza? `pernoctaciones` y `tasa_ocupacion` si contienen valores incompletos o inconsistentes.
- ¿Qué supuestos están realizando sobre los datos? Que la serie mensual es representativa de la demanda real y que los patrones estacionales se repiten con cierta estabilidad.
- ¿Qué decisión del pipeline fue más difícil? Definir la fase de agregación y proyección.
- ¿Qué aprendieron al realizar la primera carga con Pandas? A revisar la estructura, los nulos y los tipos antes del análisis.
- ¿Qué error apareció durante la implementación? Una ruta o importación incorrecta al iniciar el programa.
- ¿Cómo resolvieron ese error? Validando la estructura del proyecto desde la raíz y corrigiendo la importación.
- ¿Cómo distribuyeron las tareas dentro del equipo? Se dividieron roles entre documentación, datos y ejecución del programa.
- ¿Qué evidencia demuestra que el proyecto puede continuar? La carga inicial funciona y muestra columnas, tipos y nulos correctamente.

## Evidencia de ejecución
```text
Carga realizada correctamente.
Dimensiones:
(180, 8)
Columnas:
['año', 'mes', 'region', 'nacionalidad', 'visitantes', 'pernoctaciones', 'tasa_ocupacion', 'temporada']
Tipos de datos:
año             int64
mes            object
region         object
nacionalidad   object
visitantes      int64
pernoctaciones  int64
tasa_ocupacion float64
temporada      object
Valores nulos por columna:
año               0
mes               0
region            0
nacionalidad      0
visitantes        0
pernoctaciones    2
tasa_ocupacion    3
temporada         0
Filas duplicadas:
1
```

Este proyecto sirve como base para continuar con análisis estadístico, identificación de estacionalidad y proyección del turismo nacional e internacional.

