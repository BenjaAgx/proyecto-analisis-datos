import pandas as pd


def cargar_datos(ruta):
    """Carga un conjunto de datos desde un archivo."""
    try:
        datos = pd.read_csv(ruta)
        return datos
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
    except pd.errors.EmptyDataError:
        print("Error: el archivo no contiene datos.")
    except pd.errors.ParserError:
        print("Error: no fue posible interpretar el archivo.")
    except UnicodeDecodeError:
        print("Error: la codificación del archivo no es compatible.")
    return None


def inspeccionar_datos(datos):
    if datos is None:
        print("No existen datos disponibles para inspeccionar.")
        return

    print("\nDimensiones:")
    print(datos.shape)
    print("\nColumnas:")
    print(datos.columns.tolist())
    print("\nTipos de datos:")
    print(datos.dtypes)
    print("\nPrimeros registros:")
    print(datos.head())
    print("\nValores nulos por columna:")
    print(datos.isna().sum())
    print("\nFilas duplicadas:")
    print(datos.duplicated().sum())
    print("\nResumen estadístico:")
    print(datos.describe(include='all'))
