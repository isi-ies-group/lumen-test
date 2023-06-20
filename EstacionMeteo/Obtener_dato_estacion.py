import pygeonica as geo
import pandas as pd
import time

step_time = 30              # Periodo de extracción del dato en SEGUNDOS
etiquetas = 0               # Flag
df = pd.DataFrame()         # Dataframe vacío


def job():
    
    # Declaración variables globales
    global df               
    global etiquetas        
    
    
    lista_canales = ['Temp. Ai 1', 'R.Directa1', 'PIRAN.1', 'PIRAN.2', 'Celula Top', 'Celula Mid', 'Celula Bot', 'Top - Cal ', 'Mid - Cal ', 'Bot - Cal ', 'Presion', 'V.Vien.1', 'D.Vien.1', 'Bateria', 'Elev.Sol', 'Orient.Sol', 'Est.Geo3K']
    
    # Llamada a la función para obtener los datos de la estación
    datos_estacion = geo.estacion.lee_canales(num_estacion=316, canales=lista_canales, obtiene_unidades=False)

    datos = datos_estacion[1]               
    cabecera = ["Fecha"]                        # Primer campo de la cabecera
    datos_concat = [str(datos_estacion[0])]

    for elemento in datos: 
        cabecera.append(elemento)
    for valor in datos.values(): 
        datos_concat.append(valor[0])
    
    # Si es la primera vez que se leen los datos, obtenemos la cabecera, si no, solo los datos
    if etiquetas == 0:  
        df = pd.DataFrame(data = [cabecera])
        df = df.append([datos_concat])
        etiquetas = 1
    else:
        df = df.append([datos_concat])
        
    # Escribimos los datos obtenidos en el fichero
    df.to_csv('estacion_TiempoReal.csv', mode='w', index=False, header=False)
    print ("csv actualizado")           # Mensaje de comprobación
    return df
     

while True:
    time.sleep(step_time)
    job()