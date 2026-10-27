from src.carga import cargar_datos, inspeccionar_datos

def main():
    # Nombre del archivo actualizado dentro de la carpeta datos/
    ruta = "datos/dataset.csv"
    
    print("Iniciando la carga del conjunto de datos original (164 MB)...")
    datos = cargar_datos(ruta)
    
    if datos is not None:
        print("¡Carga completada con éxito!")
        inspeccionar_datos(datos)
    else:
        print("No se pudo procesar el archivo.")

if __name__ == "__main__":
    main()
