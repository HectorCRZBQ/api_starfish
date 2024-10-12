# Api_starfish

## Estructura del proyecto

![image](/images/image19.png)
*Se uso la libreria tree (sudo apt-get install tree), en concreto el comando tree -a -L 2*.

## Funcionamiento automatizado

Nos dirigimos al directorio *api_starfish*

Instalamos *make* con el comando **sudo apt-get install make**.

Revisar la version de python y pip que tenemos instalada con los comandos **python --version** y **pip --version**.

Solo resta ejecutar el comando **make all**. (Es recomendable tener en otra terminal ejecutado el comando **python app.py**)

## Funcionamiento sin automatizar

Accedemos al directorio *api_starfish*

![image](/images/image1.png)

Configuramos el entorno para realizar las pruebas.

Nos movemos a la carpeta donde tengamos el proyecto y activamos el entorno con el comando **source venv/bin/activate**.

![alt text](/images/image2.png)

Para desactivar el entorno solo es necesario usar el comando **deactivate**.

Todas las pruebas que se realicen con **pytest** es necesario que en otra terminal este ejecutandose la aplicación Flask, en este caso con el comando **python app.py**

## Prueba unitaria (test_1.py)

En este caso en la carpeta he tenido que añadir el archivo **__init__.py** para que funcionase el siguiente comando.

Ejecutamos el comando **python -m unittest test.test_1** y se nos devuelve el siguente resultado por terminal.

![alt text](/images/image3.png)


## Prueba de integración (test_2.py)

Ejecutamos el comando **pytest test/test_2.py** y se nos devuelve el siguente resultado por terminal.

![alt text](/images/image4.png)


## Prueba de funcionalidad (test_3.py)

Ejecutamos el comando **pytest test/test_3.py** y se nos devuelve el siguente resultado por terminal.

![alt text](/images/image5.png)

## Prueba de rendimiento (test_4.py)

En este caso se va a usar **Locust**.

Vamos a necesitar tener dos terminales abiertos simultaneamente y un navegador web.

En un primer terminal ejecutamos el comando **python app.py** para iniciar la aplicación.

![alt text](/images/image6.png)

En un segundo terminal ejecutamos el comando **locust -f test/test_4.py --host=http://127.0.0.1:5000** para iniciar Locust.

![alt text](/images/image7.png)

Solo quedaría acceder desde un navegador y visitar la dirección **http://localhost:8089**. Donde podemos configurar la cantidad de usuarios simulados y la tasa de generación de solicitudes (cantidad de usuarios nuevos por segundo).

![alt text](/images/image8.png)
![alt text](/images/image9.png)
![alt text](/images/image10.png)
![alt text](/images/image11.png)
![alt text](/images/image12.png)
![alt text](/images/image13.png)

## Prueba de seguridad (test_5.py)

Ejecutamos el comando **pytest test/test_5.py** y se nos devuelve el siguente resultado por terminal.
    
![alt text](/images/image14.png)

### Ahora todos los tests a la vez

Se pueden ejecutar a la vez los test_1.py, test_2.py, test_3.py y el test_5.py con el comando **pytest test/**. No pudiendo ejecutar el test_4.py porque necesita una interfaz externa.

![alt text](/images/image15.png)

Para ejecutar los 5 tests, se usa el comando **python -m unittest discover -s test**.

![alt text](/images/image16.png)


### Automatizarlo con un archivo Makefile

Para ejecutar el archivo Makefile solo ejecutamos el comando **make all**.

![alt text](/images/image17.png)
![alt text](/images/image18.png)

### **Autor**: [HectorCRZBQ](https://github.com/HectorCRZBQ) 
