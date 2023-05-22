# David Rodríguez Blanco

# Programa válido para introducir ficheros .csv / .txt / .dat
# Sería necesario modificar los filtros, leyendas, delimtier, etc en función de
# los datos importados y las funciones deseadas

# Para la EJECUCIÓN, desde la terminal nos dirigimos al directorio
# que contiene el archivo .py y ejecutamos el siguiente comando: 
#   lumen serve Ejemplo_V2.py --show -autoreload


import lumen as lm
import panel as pn
import pandas as pd
import intake 

pn.extension('tabulator')

sources=lm.Source(
    {
     'data1': {
         'type':'intake',
         'shared':'true',
         'cache_dir': 'cache',
         'catalog':{
             'sources':{
                 'data1_info':{
                     'driver':'csv',
                     'args': {
                         'urlpatha'
                         }
                     }
                 }
             }
         }
     
     
     }
    
    
    
    )

# ***************************** PIPELINE **************************************
pipeline = lm.Pipeline.from_spec(
    {    
    'source': {
        'type': 'intake', 
        'source':{
            'driver':'csv', 
            'args': {'urlpath' : 'ficheros/datosAutoMod.csv'}
            }
          
    },
          
    'filters': [
        {'type': 'widget', 'field': 'irr_sup'},
        {'type': 'widget', 'field': 'irr_fro'},
        {'type': 'widget', 'field': 'irr_tra'},
        {'type': 'widget', 'field': 'irr_der'},
        {'type': 'widget', 'field': 'irr_izq'}

    ],
    'auto_update': False

})
pipeline



# ******************* REPRESENTACIÓN GRÁFICA **********************************
""" SCATTER: dibujar gráficas
    pipeline = input de datos 
    kind = scatter
    x = datos a representar sobre el eje x
    y = datos a representar sobre el eje y
    by = leyenda de color en función de otra variable (Ej: by = especies)
    height = altura del imagen del gráfico (no el máximo de datos)
    responsive = True (con True se ajusta al máximo de ventana)
"""
"""
scatter = lm.views.hvPlotView(
    pipeline=pipeline, kind='scatter', x='created_at', y='irr_sup',
    height=400, responsive=True
)
scatter
"""

# ********************************* TABLA *************************************
""" TABLE: dibujar tablas
    pipeline = input de datos 
    page_size = total de filas a mostrar
    sizing_mode = 
"""
"""
table = lm.views.Table(pipeline=pipeline, page_size=40, sizing_mode='stretch_width')
table
"""


# ****************************** LAYOUT ***************************************
""" LAYOUT: mostrar varias elementos de forma conjunta en una página
    En este caso, mostramos el scatter y la tabla, con el título de 'Tracker'
"""
"""
layout = lm.Layout(views={'scatter': scatter, 'table': table}, title='Tracker')
layout
"""


# ****************************** LAYOUT ***************************************
""" DASHBOARD: creación del dash al completo (incluye los filtros del pipeline)
    Introducimos el título que queramos y el layout definido anteriormente
"""  
"""
dash = lm.Dashboard(config={'title': 'Tracker'}, layouts=[layout])
dash
"""


# .servable() , necesario para poder visualizar los elementos


pipeline.servable()
"""
scatter.servable()
table.servable()
layout.servable()


dash.servable()
"""

