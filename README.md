# DOCUMENTACIÓN LUMEN

## Estructura de un fichero YAML 
 - CONFIG: Se puede establecer el nombre del dash junto con la temática (claro/oscuro). 
 - SOURCE: Origen del archivo fuente. Se puede/debe definir el tipo de archivo a utilizar (p.ej: file), la libreria adecuada junto con la ruta del fichero que contiene los datos.  
 - PIPELINE: Se pueden crear tantos "pipeline" como se quiera. En cada uno de ellos se define la fuente y tabla de donde queremos coger los datos (ambos definidos en "source"). A continuación se pueden definir los filtros (campos) que queremos aplicar a esos datos.
 - LAYOUT: Diferentes ventanas donde mostraremos los datos deseados de la forma más adecuada (tablas, gráficos de barras, gráficos de puntos ... ). Al igual que en los anteiores, definimos que datos queremos mostrar e indicamos el tipo de gráfica. 

    *[Ver ejemplos para las distintas funciones](https://lumen.holoviz.org/gallery/index.html)* 

  
## Importar ficheros fuente  
Lumen permite utilizar directamente: CSV, XLSX, XLS, Parquet, y JSON. 

En la sección de 'source' del siguiente [enlace](https://lumen.holoviz.org/reference/index.html) se muestran los distintos tipos de ficheros que se pueden importar junto con sus adecuadas declaraciones (p.ej: type:file).  
 

Se han explorado las opciones de 'FileSource' para importar de manera directa los archivos 'csv' y, mediante una pequeña conversión, ficheros de tipo txt y dat ( mediante Python). 
Se ha tratado de hacer uso de la libreria 'intake' utilizando Python sin éxito. Para utilizar esta libreria con YAML hay númerosos [ejemplos](https://lumen.holoviz.org/gallery/precip.html) en el repositorio de Lumen. 


## Mostrar gráficas 
Para mostrar tablas se puede emplear dentro de 'view' el 'type:table'.

Para mostrar gráficas, se puede utilizar 'type:hvplot_ui' si queremos mostrarlo de forma dinámica, o 'type:hvplot. 

Para ver más opciones y consultar los argumentos de cada una de las funciones, ir al apartado '[View](https://lumen.holoviz.org/reference/index.html)'.

  
## PANEL 
Proporciona una representación visual de los datos.
Más información en la [ayuda](https://lumen.holoviz.org/reference/view/Panel.html)

## INTAKE 
Aumenta el rango de capacidades a la hora de importar ficheros de distintos tipos. En el [enlace](https://intake.readthedocs.io/en/latest/plugin-directory.html) se listan los 'plugin' disponibles junto con sus funcionalidades.

[Ayuda](https://lumen.holoviz.org/reference/source/IntakeSource.html) y [ejemplos](https://lumen.holoviz.org/gallery/precip.html) disponibles en GitHub.

  
## STREAMZ 
Plugin de intake que permite mostrar gráficas a partir de dataframes o streams de manera directa.

[Ayuda](https://github.com/intake/intake-streamz/) y [ejemplos](https://github.com/intake/intake-streamz/blob/master/examples/simple_plot.ipynb) disponibles en GitHub.