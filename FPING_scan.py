import subprocess
import os
import sys

# Directorio donde se guardarán los resultados
directorio_resultados = "resultados"

# Leer el nombre del archivo de segmentos de red desde los argumentos de línea de comandos
if len(sys.argv) < 2:
    print("Debe proporcionar el nombre del archivo de segmentos de red como argumento.")
    sys.exit(1)

nombre_archivo = sys.argv[1]

# Comprobar si el archivo existe
if not os.path.isfile(nombre_archivo):
    print(f"No se encontró el archivo: {nombre_archivo}")
    sys.exit(1)

# Crear el directorio de resultados si no existe
os.makedirs(directorio_resultados, exist_ok=True)

# Leer los segmentos de red desde el archivo
with open(nombre_archivo, "r") as file:
    segmentos_red = file.read().splitlines()

# Realizar el escaneo para cada segmento de red
for segmento in segmentos_red:
    # Crear el nombre de la carpeta correspondiente al segmento de red
    nombre_carpeta = os.path.join(directorio_resultados, segmento.replace("/", "_"))

    # Crear la carpeta correspondiente al segmento de red
    os.makedirs(nombre_carpeta, exist_ok=True)

    # Ejecutar el comando fping y redirigir la salida al archivo correspondiente
    archivo_resultado = os.path.join(nombre_carpeta, "resultado.txt")
    subprocess.run(["fping", "-a", "-g", segmento], stdout=open(archivo_resultado, "w"))

    # Imprimir mensaje de finalización para el segmento de red
    print(f"Escaneo completado para el segmento de red: {segmento}. Resultados guardados en: {archivo_resultado}")
