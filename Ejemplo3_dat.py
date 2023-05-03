#import intake
import lumen as lm
import panel as pn
import pandas as pd


# Válido para introducir tanto csv como txt.
datos = pd.read_csv('ficheros/summaryRR_comprados.dat', delimiter='	', encoding='latin1')
datos.to_csv('ficheros/datosAutoMod.csv')
    

pn.extension('tabulator')

pipeline = lm.Pipeline.from_spec(
    {    
    'source': {
        'type': 'file',
        'tables': { 'local_table': 'ficheros/datosAutoMod.csv' } # Ruta relativa al fichero en csv generado
    },
     
    
    'auto_update': False

})
pipeline


""" CATTER: para dibujar gráficas.
    pipeline = input de datos 
    kind = scatter
    x = datos a representar sobre el eje x
    y = datos a representar sobre el eje y
    by = leyenda de color en función de otra variable (Ej: by = especies)
    height = altura del imagen del gráfico (no el máximo de datos)
    responsive = True (con True se ajusta al máximo de ventana)

scatter = lm.views.hvPlotView(
    pipeline=pipeline, kind='scatter', x='created_at', y='irr_sup',
    height=400, responsive=True
)
scatter
"""

""" TABLE: para dibujar tablas.
    pipeline = input de datos 
    page_size = total de filas a mostrar
    sizing_mode = 

table = lm.views.Table(pipeline=pipeline, page_size=40, sizing_mode='stretch_width')
table
"""

""" LAYOUT: para mostrar varias cosas de forma conjunta en una página
    En este caso, mostramos el scatter y la tabla, con el título de 'Tracker'

layout = lm.Layout(views={'scatter': scatter, 'table': table}, title='Tracker')
layout
"""

""" DASHBOARD: creación del dash al completo (incluye los filtros del pipeline)
    Introducimos el título que queramos y el layout definido anteriormente
    

dash = lm.Dashboard(config={'title': 'Tracker'}, layouts=[layout])
dash
"""

# .servable() para poder mostrar que se puedan mostrar en el panel

pipeline.servable()
"""
scatter.servable()
table.servable()
layout.servable()
dash.servable()
"""
