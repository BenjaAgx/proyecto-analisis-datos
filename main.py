from src.carga import cargar_datos, inspeccionar_datos


def main():
    ruta = "datos/dataset.csv"
    datos = cargar_datos(ruta)
    if datos is not None:
        print("Carga realizada correctamente.")
        inspeccionar_datos(datos)
    else:
        print("El programa finalizó sin procesar los datos.")


if __name__ == "__main__":
    main()
