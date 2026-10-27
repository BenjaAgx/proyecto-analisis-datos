import pandas as pd

def cargar_datos(ruta):
    """
    Carga el archivo CSV con separador de punto y coma y codificacion latin-1.
    """
    try:
        datos = pd.read_csv(
            ruta, 
            sep=';', 
            encoding='latin-1', 
            decimal=',', 
            on_bad_lines='skip'
        )
        return datos
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo '{ruta}'.")
        return None
    except Exception as e:
        print(f"Error inesperado al cargar los datos: {e}")
        return None

def inspeccionar_datos(datos):
    """
    Realiza la inspeccion inicial solicitada por la pauta del Avance 1.
    """
    if datos is None:
        print("No hay datos para inspeccionar.")
        return
    
    print("\n=== DIMENSIONES ===")
    print(f"Filas: {datos.shape[0]:,} | Columnas: {datos.shape[1]}")
    
    print("\n=== COLUMNAS ===")
    print(datos.columns.tolist())
    
    print("\n=== TIPOS DE DATOS ===")
    print(datos.dtypes)
    
    print("\n=== PRIMEROS 5 REGISTROS ===")
    print(datos.head())
    
    print("\n=== VALORES NULOS POR COLUMNA ===")
    print(datos.isna().sum())
    
    print("\n=== FILAS DUPLICADAS ===")
    print(f"Total de duplicados: {datos.duplicated().sum():,}")
