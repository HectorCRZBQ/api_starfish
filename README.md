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


## Incorporamos un linter (pylint)

Instalamos **pylint** con el comando **pip install pylint**

![alt text](/images/image20.png)

Ejecutamos el comando **pylint *.py** dentro del directorio de la API.

**Primera ejecuccion**
![alt text](/images/image21.png)

**Segunda ejecuccion**
 - Docstring de nivel de cada modulo de app.py
 - Advertencia de pocas funciones publicas

![alt text](/images/image22.png)

**Tercera ejecuccion**
 - Docstring explicativo a init_db.py

![alt text](/images/image23.png)

## Incorporamos coverage

Instalamos **coverage** con el comando **pip install coverage**

![alt text](/images/image24.png)

Ejecutamos el comando **make setup** para instalar la dependencias y luego **make test** para realizar la prueba de cobertura.

![alt text](/images/image25.png)

Accedemos a navegador para visualizar el reporte que se nos ha generado con el comando **open htmlcov/index.html**

![alt text](/images/image26.png)


## Incorporamos trivy

Instalamos **trivy** con el comando **sudo apt-get install -y wget && wget https://github.com/aquasecurity/trivy/releases/download/v0.46.0/trivy_0.46.0_Linux-64bit.deb && sudo dpkg -i trivy_0.46.0_Linux-64bit.deb**.

![alt text](/images/image27.png)
![alt text](/images/image28.png)

Ejecutamos el comando **make trivy** para realizar un escaneo de vulnerabilidades.

![alt text](/images/image29.png)
![alt text](/images/image30.png)


## Automatizacion de mejoras incorporadas

Ejecutamos el comando **make lint** para realizar una envaluacion de la calidad del codigo de manera automatizada del app.py y todos los tests.

![alt text](/images2/image31.png)

Ejecutamos el comando **make coverage** para realizar un reporte del código.

![alt text](/images2/image32.png)

Ejecutamos el comando **make trivy** para buscar vulnerabilidades de seguridad.

![alt text](/images2/image33.png)


## Incorporamos dotenv (configuracion)

Creamos **.env** con el comando **touch .env** y lo modificamos con **nano**  donde añadimos las variables de configuración.

![alt text](/images2/image34.png)

Para cargar las varisable en la aplicación usamos **dotenv** que istalamos con el comando **pip install python-dotenv**.

![alt text](/images2/image35.png)

Creamos el archivo **secrets.yaml** con el comando **touch secrets.yaml** y lo modificamos con **nano** donde guardamos un usuario y una contraseña(falsas) que son datos sensibles.

![alt text](/images2/image36.png)

Añadimos este archivo dentro de .gitignore para que no se comparta.


## Incorporamos SOPS y PGP (secretos)

Descargamos [SOPS](https://github.com/getsops/sops/releases).

En este caso seguimos los siguientes comandos:

 - **Descargar el binario de la versión 3.9.1**: curl -LO https://github.com/getsops/sops/releases/download/v3.9.1/sops-v3.9.1.linux.amd64
 - **Mover el binario al directorio /usr/local/bin**: sudo mv sops-v3.9.1.linux.amd64 /usr/local/bin/sops
 - **Hacer que el binario sea ejecutable**: sudo chmod +x /usr/local/bin/sops
 - **Verificar la instalacion**: sops --version

![alt text](/images2/image37.png)

Una vez descargada la imagen, ejecutamos el comando **gpg --import sops_functional_tests_key.asc** para importar la clave descargada.

![alt text](/images2/image38.png)

Ciframos el archivo secrets.yaml con el comando **sops --encrypt --pgp FBC7B9E2A4F9289AC0C1D4843D16CEE4A27381B4 secrets.yaml > secrets.enc.yaml** y se nos actualiza el nombre **secrets.enc.yaml**

![alt text](/images2/image39.png)

Revisamos el contenido del archivo **secrets.enc.yaml** para verificar que se ha encriptado correctamente las claves.

![alt text](/images2/image40.png)

Y para desencriptarlo necesitariamos ejecutar el comando **sops --decrypt secrets.enc.yaml > secrets.yaml**

![alt text](/images2/image41.png)


## Automatizacion de mejoras incorporadas

Ejecutamos el comando **make encrypt** para cifrar el archivo secrets.yaml usando SOPS y PGP, convirtiendolo en el secrets.enc.yaml

![alt text](/images2/image42.png)

Ejecutamos el comando **make decrypt** para descifrar el archivo secrets.enc.yaml y lo muestra de nuevo en el archivo secrets.yaml

![alt text](/images2/image43.png)

Al ejecutar el **make all** observamos que tambien se ejecuta el encrypt y decrypt de manera automarizada.

![alt text](/images2/image44.png)


## Integrar Poetry

*Documentación oficial: https://python-poetry.org/docs/*

Creamos una nueva rama **poetry** con el comando **git checkout -b poetry**.

![alt text](/images2/image45.png)

Necesitamos revisar que tenemos correctamente instalo **pipx**, sino se tiene instalado se puede ejecutar el comando **sudo apt install pipx** y incluimos su path con **pipx ensurepath**

![alt text](/images2/image46.png)

*Si se tienen problemas se puede acceder a la documentación oficial de pipx en https://pipx.pypa.io/stable/installation/*

Instalamos Poetry ejecutando el comando **pipx install poetry**

![alt text](/images2/image47.png)

![alt text](/images2/image48.png)

Actualizamos Poetry, que acabamos de descargar con el comando **pipx upgrade poetry**.

![alt text](/images2/image49.png)

Verificamos la version instalada de Poetry con el comando **poetry --version**.

![alt text](/images2/image50.png)

*Si no sale error de que no está instalado, es cuestión de reiniciar la terminal con el comnado **exec $SHELL** y volver a revisar la versio, ahora no va a mostrar ningun error.*

Iniciamos Poetry con el comando **poetry init**

Se nos va a pedir completar la configuración determinando el contenido de los siguientes campos:

 - Project name: Nombre del proyecto, en este caso es **api-starfish**
 - Version: Versión inicial por defecto, la version **0.1.0**
 - Description: La descripción es **A API that makes the CRUD tasks about starfish**
 - Author: Mi nombre que es **HectorCRZBQ** y mi correo que es **hectorcb3333@gmail.com**
 - License: lo dejamos vacio sin una licencia definida
 - Python version: La versión mínima de Python definida es **3.12**
 - Dependencies: Seleccionamos **no** a dependencias interactivas
 
 Y tras haber completado los anteriores campos se habria terminado de configurar de manera basica.

 ![alt text](/images2/image51.png)

 Al terminar este paso se no crea el archivo **pyproject.toml** con el contenido anteriormente definido, lo revisamos con el comando **cat pyproject.toml**.

 ![alt text](/images2/image52.png)

 ![alt text](/images2/image53.png)


 Añadimos las dependencias de nuestro archivo **requirements.txt** con el comando **poetry add $(cat requirements.txt)**.

 ![alt text](/images2/image54.png)

*Vemos como se han cargado todas las dependencias declaradas en el archivo requirements.txt*

Tras haber realizado la copia de las dependencias se ha creado el archivo **poetry.lock** y donde su contenido es el siguiente mostrado.

 ![alt text](/images2/image55.png)

 ![alt text](/images2/image56.png)

Se nos ha actualizado el contenido de las dependencias del archivo **pyproject.toml**.

 ![alt text](/images2/image57.png)

Instalamos las dependencias con el comando **poetry install**

 ![alt text](/images2/image58.png)

*Optamos por el comando **poetry install --no-root** para no instalar el proyecto, solo instalar las dependencias necesarias.*

*Documentacion oficial: https://python-poetry.org/docs/basic-usage/#initialising-a-pre-existing-project*

Una vez que las dependencias estan descargadas, podemos acceder al entorno de trabajo con el comando **poetry shell**.

 ![alt text](/images2/image59.png)

Y para salir del entorno virtual solo nos queda ejecutar el comando **exit**

 ![alt text](/images2/image60.png)


## Integrar Projen

*Documentación oficial: https://github.com/projen/projen*

Creamos una nueva rama **projen** con el comando **git checkout -b projen**.

 ![alt text](/images3/image61.png)

Vamos a usar **npm**, por lo que vamos a añadir **nodejs 22.8.0** dentro de **.tool-versions**.

 ![alt text](/images3/image62.png)

Revisamos las versiones presentes de **node** y de **npm** con los comandos de **node --version** y de **npm --version**.

 ![alt text](/images3/image63.png)

*Si dan error puede deberse a que asdf este desactualizado y no contenga nodejs por lo que ejecutamos el comando **asdf plugin-add nodejs***.

Instalamos Projen ejecutando el comando **npx projen new typescript-app**

 ![alt text](/images3/image64.png))





Se nos crea el archivo **.projenrc.js** donde guardamos nuestras dependencias.

Instalamos las dependencias y configuramos el proyecto con el comando **npx projen**


### **Autor**: [HectorCRZBQ](https://github.com/HectorCRZBQ) 
