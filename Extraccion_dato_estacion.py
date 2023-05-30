import pygeonica as geo
import pandas as pd
import datetime
#import schedule
import time


step_time = 30           # Tiempo en segundos
etiquetas = 0
df = pd.DataFrame()


def job():
    
    global df
    global etiquetas
    
    lista_canales = ['Temp. Ai 1', 'R.Directa1', 'PIRAN.1', 'PIRAN.2', 'Celula Top', 'Celula Mid', 'Celula Bot', 'Top - Cal ', 'Mid - Cal ', 'Bot - Cal ', 'Presion', 'V.Vien.1', 'D.Vien.1', 'Bateria', 'Elev.Sol', 'Orient.Sol', 'Est.Geo3K']
    datos_estacion = geo.estacion.lee_canales(num_estacion=316, canales=lista_canales, obtiene_unidades=False)
        

    # datos_estacion = (datetime.datetime(2023, 5, 26, 10, 30, 15),
    # {'Temp. Ai 1': [16.125030517578125, '°C'],
    #  'R.Directa1': [0.0, 'W/m2'],
    #  'PIRAN.1': [59.970359802246094, 'W/m2'],
    #  'PIRAN.2': [54.79669189453125, 'W/m2'],
    #  'Celula Top': [-0.17593203485012054, 'W/m2   '],
    #  'Celula Mid': [6.012368679046631, 'W/m2   '],
    #  'Celula Bot': [7.0605244636535645, 'W/m2   '],
    #  'Top - Cal ': [0.6942732334136963, 'W/m2   '],
    #  'Mid - Cal ': [0.5443870425224304, 'W/m2   '],
    #  'Bot - Cal ': [-0.23981809616088867, 'W/m2   '],
    #  'Presion': [938.0963134765625, 'kPa'],
    #  'V.Vien.1': [1.1699999570846558, 'm/s'],
    #  'D.Vien.1': [333.0, '°'],
    #  'Bateria': [13.580316543579102, 'V'],
    #  'Elev.Sol': [61.03712463378906, '°'],
    #  'Orient.Sol': [124.24305725097656, '°'],
    #  'Est.Geo3K': [0.0, 'Estado']
    # })

    datos = datos_estacion[1]
    cabecera = ["Fecha"]
    datos_concat = [str(datos_estacion[0])]

    for elemento in datos: 
        cabecera.append(elemento)
    for valor in datos.values(): 
        datos_concat.append(valor[0])
    
    
    if etiquetas == 0:  
        df = pd.DataFrame(data = [cabecera])
        df = df.append([datos_concat])
        etiquetas = 1
    else:
        df = df.append([datos_concat])
        
    df.to_csv('ficheros/estacion_TiempoReal.csv', mode='w', index=False, header=False)
    print ("csv actualizado")
    return df
     

while True:
    time.sleep(step_time)
    job()
 
# schedule.every(step_time).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
        
    
    # df = pd.DataFrame(datos_estacion)
    # df.to_csv('ficheros/estacion_TiempoReal.csv', mode='a', index=False, header=False)



    # rad = datos_estacion[1]['PIRAN.1'][0]       # El ultimo 0 es para quitar la unidad
    # print (rad)


    #print (datos_estacion[0])       # Print de la hora

    #df = pd.DataFrame(data = [datos_concat], index = [str(datos_estacion[0])])
    #df = pd.DataFrame(data = [datos_concat], columns=cabecera, index = [str(datos_estacion[0])])
    #df = df.append(pd.DataFrame(columns = cabecera, data  = datos_concat), ignore_index=True)


