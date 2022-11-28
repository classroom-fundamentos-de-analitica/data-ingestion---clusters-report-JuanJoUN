"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------
Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.
"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    fileName = "clusters_report.txt"
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()
    columnas = [i.strip().lower().replace(' ', '_') for i in lines[0].strip().split('  ')]
    columnas.remove('')
    cluster = []
    cantPalabras = []
    porcPalabras = []
    principalesPalabras = []
    for i in range(len(columnas)):
        if i==1 or i==2:
            columnas[i] = columnas[i] + '_palabras_clave'
    del lines[:4]

    parrafo = 1
    palabras = []
    for line in lines:
        values = [item for item in line.split('  ') if item != '']
        if values == ['\n'] or values == [' \n']:
            parrafo = 1
            principalesPalabras.append(" ".join(palabras))
            palabras = []
            continue
        if parrafo == 1:
            cluster.append(int(values.pop(0).strip()))
            cantPalabras.append(int(values.pop(0).strip()))
            porcPalabras.append(float(values.pop(0)[:-2].strip().replace(",", ".")))
        values = [i.strip().replace(".", "") for i in values]
        palabras.append(" ".join(values))
        parrafo += 1
    data = {
        columnas[0]: cluster,
        columnas[1]: cantPalabras,
        columnas[2]: porcPalabras,
        columnas[3]: principalesPalabras
    }
    df = pd.DataFrame(data)

    return df