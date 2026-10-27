# Proyecto 14: Evolucion del Turismo Nacional e Internacional

## Informacion del Proyecto
- Institucion: Universidad Autonoma de Chile
- Asignatura: Programacion Avanzada
- Proyecto: Avance 1 - Analisis del Flujo de Turismo
- Integrantes:
  - Benjamin Aguayo
  - Enzo Illanes
  - Jaime Panguinao

---

## Descripcion del Problema
El turismo en Chile representa un sector economico clave influido por estacionalidad, factores socioeconomicos y patrones de movilidad. Este proyecto busca analizar la evolucion del flujo de visitantes a nivel comunal, regional y por paises emisores de turistas, permitiendo identificar temporadas de alta demanda y proyectar el flujo de visitantes para apoyar la toma de decisiones en el sector.

### Pregunta Principal:
¿Que tendencia presenta el flujo de turismo en los ultimos anos y como varia la estacionalidad entre las distintas regiones de Chile?

---

## Diseno del Pipeline de Datos

El recorrido de los datos en este proyecto sigue una arquitectura modular en Python desde la obtencion de las fuentes originales hasta la interpretacion final para la toma de decisiones.

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
│   └── archivocsvlink.txt        # Enlace alternativo a Google Drive
│
├── reportes/
│   └── avance_1.pdf              # Informe del Avance 1 en formato PDF
│
├── src/
│   ├── __init__.py               # Paquete de modulos Python
│   └── carga.py                  # Modulo de carga e inspeccion de datos
│
├── .gitignore                    # Reglas de exclusion de archivos
├── README.md                     # Documentacion general del repositorio
├── requirements.txt              # Dependencias del proyecto
└── main.py                       # Script principal ejecutable

---

## Tecnologias y Librerias
- Lenguaje: Python 3
- Librerias principales: pandas, openpyxl
- Control de versiones: Git & GitHub

---

## Instrucciones de Ejecucion

1. Clonar el repositorio:
   git clone https://github.com/BenjaAgx/proyecto-analisis-datos.git
   cd proyecto-analisis-datos

2. Obtener el dataset:
   - Debido al limite de tamano de GitHub (164 MB), el archivo dataset.csv no se encuentra dentro del repositorio.
   - Siga las instrucciones ubicadas en datos/README.md o descargue el archivo dataset.csv desde el enlace provisto en datos/archivocsvlink.txt.
   - Coloque el archivo dataset.csv dentro de la carpeta datos/.

3. Instalar dependencias:
   pip install -r requirements.txt

4. Ejecutar el programa principal:
   python main.py
