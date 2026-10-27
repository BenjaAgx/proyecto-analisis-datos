# Proyecto 14: Evolucion del Turismo Nacional e Internacional

## Informacion del Proyecto
- **Institucion:** Universidad Autonoma de Chile
- **Carrera:** Ingenieria Civil Plan Común
- **Asignatura:** Programacion Avanzada
- **Docente:** Alex Flores Fuentealba
- **Proyecto:** Avance 1 - Analisis del Flujo de Turismo
- **Integrantes:**
  - Benjamin Aguayo
  - Enzo Illanes
  - Jaime Panguinao
- **Enlace al Repositorio:** https://github.com/BenjaAgx/proyecto-analisis-datos

---

## Descripcion del Problema
El turismo en Chile representa un sector economico fundamental cuyo comportamiento varia drasticamente segun la estacionalidad, factores socioeconomicos y patrones de movilidad territorial. Este proyecto busca analizar la evolucion del flujo de visitantes a nivel comunal, regional y por paises emisores de turistas, permitiendo identificar temporadas de alta demanda y proyectar el flujo de visitantes para apoyar la toma de decisiones en el sector publico y privado.

### Pregunta Principal:
¿Que tendencia presenta el flujo de turismo en los ultimos anos y como varia la estacionalidad entre las distintas regiones de Chile?

### Objetivos:
- **Objetivo General:** Analizar los registros de movilidad turistica comunal y regional para identificar patrones estacionales y tendencias de flujo de visitantes.
- **Objetivos Especificos:**
  1. Cargar e inspeccionar la matriz de movilidad comunal mediante la biblioteca Pandas.
  2. Identificar la presencia de valores nulos, duplicados y anomalias en los datos de visitantes mensuales.

---

## Diseno del Pipeline de Datos

El recorrido de los datos sigue una arquitectura modular en Python desde la obtencion de las fuentes originales hasta la generacion del informe final para la toma de decisiones.

### Diagrama del Pipeline:

Fuente de datos (SERNATUR / INE)
       ↓
Descarga o recepcion del dataset
       ↓
Almacenamiento en datos/ (dataset.csv)
       ↓
Carga con Pandas (src/carga.py)
       ↓
Validacion de estructura e inspeccion inicial
       ↓
Limpieza y transformacion (Tratamiento de nulos y formato largo)
       ↓
Analisis exploratorio (KPIs, estacionalidad y crecimiento)
       ↓
Visualizacion de resultados (Matplotlib / Seaborn)
       ↓
Interpretacion e Informe final (reportes/avance_1.pdf)


### Tabla Descriptiva del Pipeline:

| Etapa | Entrada | Proceso | Salida | Herramienta |
| :--- | :--- | :--- | :--- | :--- |
| Obtencion | Fuente original (SERNATUR / INE) | Descarga manual o consulta | Archivo CSV | Portal institucional |
| Carga | Archivo datos/dataset.csv | Lectura con manejo de encoding y separadores | DataFrame inicial | Pandas (src/carga.py) |
| Validacion | DataFrame inicial | Inspeccion de dimensiones, tipos, nulos y duplicados | Diagnostico descriptivo | Pandas (inspeccionar_datos) |
| Limpieza | Datos originales | Formateo de decimales y conversion de matriz a serie | DataFrame limpio | Pandas |
| Analisis | Datos limpios | Calculo de promedios mensuales y variacion interanual | Indicadores turisticos | Pandas / NumPy |
| Visualizacion | Resultados estadisticos | Generacion de graficos de barras y lineas | Figuras de tendencias | Matplotlib / Seaborn |
| Reporte | Resultados e imagenes | Redaccion y sintesis metacognitiva | Informe PDF | PDF (reportes/avance_1.pdf) |

---

## Estructura del Repositorio

proyecto-analisis-datos/
│
├── datos/
│   ├── README.md                 # Documentacion para la obtencion del dataset
│   └── instrucciones_descarga.txt # Enlace alternativo a Google Drive
│
├── reportes/
│   └── avance_1.pdf              # Informe del Avance 1 en formato PDF
│
├── src/
│   ├── __init__.py               # Paquete de modulos Python
│   └── carga.py                  # Modulo de carga e inspeccion de datos
│
├── .gitignore                    # Reglas de exclusion de archivos (*.csv)
├── README.md                     # Documentacion general del repositorio
├── requirements.txt              # Dependencias del proyecto
└── main.py                       # Script principal ejecutable

---

## Tecnologias y Librerias
- **Lenguaje:** Python 3
- **Librerias principales:** pandas, openpyxl
- **Control de versiones:** Git & GitHub
- **Entorno de desarrollo:** Visual Studio Code

---

## Instrucciones de Ejecucion

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/BenjaAgx/proyecto-analisis-datos.git](https://github.com/BenjaAgx/proyecto-analisis-datos.git)
   cd proyecto-analisis-datos
==================================================
==================================================

Este proyecto sirve como base para continuar con análisis estadístico, identificación de estacionalidad y proyección del turismo nacional e internacional.

