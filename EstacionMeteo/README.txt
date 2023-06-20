INSTRUCCIONES PARA LA UTILIZACIÓN DEL PROGRAMA

1. Desde la terminal, dirigirse al directorio que contenga ambos ficheros. 

2. Lanzar el programa de python: 
	" Python Obtener_dato_estacion.py"

3. Lanzar el programa de lumen. Para ello, desde la terminal ejecutar el siguiente comando: 
	" lumen serve Obtener_dato_estacion.yml --show "
	
	IMPORTANTE: lanzar lumen sin la opción de "--autoreload". De esta manera se pueden ver los cambios
		    en tiempo real sin necesidad de lanzar lumen desde la terminal cada vez que se quiera 
		    actualizar el dash

Una vez tengamos en ejecución ambos programas, para actualizar el dash y visualizar los datos en tiempo real 
se debe refrescar la ventana. 

NOTA: Se puede crear una rutina en el computador que inicie el programa de python a cierta hora del día. 
      Así, se podría tener un fichero con los datos acumulados desde la hora de lanzamiento hasta la actual 
      para posteriormente visualizarlos mediante la herramienta Lumen en el caso de así desearlo. 

