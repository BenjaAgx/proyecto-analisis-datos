import pandas as pd

def procesar_datos_turismo(filepath_excel, output_csv):
    # Cargar hoja desglosada
    df = pd.read_excel(filepath_excel, sheet_name='CONSULTA_DESAGREGADA')
    
    # Filtrar rango de años del proyecto (2021-2025)
    df = df[(df['AÑO'] >= 2021) & (df['AÑO'] <= 2025)]
    
    # Agrupar y resumir
    df_grouped = df.groupby(['AÑO', 'MES', 'REGION', 'REGION_01'])['SumaDeTTAS'].sum().reset_index()
    
    # Renombrar columnas según el Diccionario de Datos
    df_grouped.columns = ['año', 'mes', 'region', 'nacionalidad', 'visitantes']
    
    # Guardar como CSV para GitHub
    df_grouped.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Dataset generado exitosamente en: {output_csv}")

if __name__ == "__main__":
    procesar_datos_turismo('dataset(2).xlsx', 'datos/dataset.csv')
    print("\nFilas duplicadas:")
    print(datos.duplicated().sum())
    print("\nResumen estadístico:")
    print(datos.describe(include='all'))
