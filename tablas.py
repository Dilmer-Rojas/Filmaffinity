import os
import pandas as pd

# 📂 Directorio donde están los archivos .xlsx
carpeta = "./data/tablas"  # Cambia esto a la ruta donde están los archivos

# 📌 Crear un objeto de Excel
ruta_salida = "./data/archivo_final.xlsx"
with pd.ExcelWriter(ruta_salida, engine="openpyxl") as writer:
    # 📌 Recorremos los archivos en la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".xlsx"):  # Filtra solo archivos .xlsx
            ruta_archivo = os.path.join(carpeta, archivo)

            # 📌 Cargar el archivo en un DataFrame
            df = pd.read_excel(ruta_archivo)

            # 📌 Eliminar la extensión ".xlsx" para usarlo como nombre de hoja
            nombre_hoja = os.path.splitext(archivo)[0]

            # 📌 Guardar en el archivo final como una hoja diferente
            df.to_excel(writer, sheet_name=nombre_hoja, index=False)

print(f"✅ Archivo consolidado guardado en: {ruta_salida}")
