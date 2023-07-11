# DOCUMENTACIÓN LUMEN

## Estructura de un fichero YAML 
 - CONFIG: Se puede establecer el nombre del dash junto con la temática (claro/oscuro). 
 - SOURCE: Origen del archivo fuente. Se puede/debe definir el tipo de archivo a utilizar (p.ej: file), la libreria adecuada junto con la ruta del fichero que contiene los datos.  
 - PIPELINE: Se pueden crear tantos "pipeline" como se quiera. En cada uno de ellos se define la fuente y tabla de donde queremos coger los datos (ambos definidos en "source"). A continuación se pueden definir los filtros (campos) que queremos aplicar a esos datos.
 - LAYOUT: Diferentes ventanas donde mostraremos los datos deseados de la forma más adecuada (tablas, gráficos de barras, gráficos de puntos ... ). Al igual que en los anteriores, definimos que datos queremos mostrar e indicamos el tipo de gráfica.

   Se encuentran disponibles en este repositorio algunos ejemplos completos, tanto en [Python](Ejemplos/Python/ej_csv_DashCompleto.py) como en [Yaml](Ejemplos/Yaml/ej_csv_DashCompleto.yml).

    *Ver [ejemplos](https://lumen.holoviz.org/gallery/index.html) para las distintas funciones.* 

  
## Importar ficheros fuente  
Lumen permite utilizar directamente: CSV, XLSX, XLS, Parquet, y JSON. 

En la sección '[source](https://lumen.holoviz.org/reference/index.html)' se muestran los distintos tipos de ficheros que se pueden importar junto con sus adecuadas declaraciones (p.ej: type:file).  

Se han explorado las opciones de 'FileSource' para importar de manera directa los archivos '.csv' y, mediante una pequeña conversión, ficheros de tipo txt y dat (mediante Python). 
Se puede utilizar Intake con YAML. En [este](https://lumen.holoviz.org/gallery/precip.html) ejemplo se incluye el driver ['csv'](https://intake.readthedocs.io/en/latest/api_user.html#intake.source.csv.CSVSource). Permite usar "csv_kwargs" que enlaza con los parámetros de read_csv() de Pandas.

## Mostrar gráficas 
Para mostrar tablas se puede emplear dentro de 'view' el 'type:table'.

Para mostrar gráficas, se puede utilizar 'type:hvplot_ui' si queremos que sean dinámicas, o 'type:hvplot' en su defecto. 

Para ver más opciones y consultar los argumentos de cada una de las funciones, ir al apartado '[View](https://lumen.holoviz.org/reference/index.html)'.

  
## PANEL 
Proporciona una representación visual de los datos.
Más información en la [ayuda](https://lumen.holoviz.org/reference/view/Panel.html).

[Ejemplo básico](Ejemplos/Python/ej_panel_streamz.py) en Python. 

## INTAKE 
Aumenta el rango de capacidades a la hora de importar ficheros de distintos tipos. 

En el [enlace](https://intake.readthedocs.io/en/latest/plugin-directory.html) se listan los 'plugin' disponibles junto con sus funcionalidades.

[Ayuda](https://lumen.holoviz.org/reference/source/IntakeSource.html) y [ejemplos](https://lumen.holoviz.org/gallery/precip.html) disponibles en GitHub.

Disponibles ejemplos básicos en el repositorio, empleando [Python y cargando un catalog en YAML](Ejemplos/Python/ej_intake_basico.py). 

  
## STREAMZ 
Plugin de intake que permite mostrar gráficas a partir de dataframes o streams de manera directa.

[Ayuda](https://github.com/intake/intake-streamz/) y [ejemplos](https://github.com/intake/intake-streamz/blob/master/examples/simple_plot.ipynb) disponibles en GitHub.
