#Proyecto QA 

##Descripcion: En este proyecto podemos encontrar 3 script, divididos en 2 casos de pruebas con su logica para poder registrar usuarios en la plataforma de la pagina "https://test-qa.inlaze.com/auth/sign-in"
con su inicio de sesion del usuario nuevo, realizando validacion de los mismos campos del formulario, el 3 scrit se dejan los test de los bugs encontrados en el software.

##Requisitos: Favor antes de iniciar los Scripts tener en cuenta tener las siguientes herramientas y librerias:

- python [version 3.10.4] si no se tiene realizar instalacion descargando el .exe en pagina oficial "https://www.selenium.dev/downloads/".
- pip [Actualizar]
- Selenium [version 4.23.1] se debe descargar libreria dependiendo del lenguaje en la siguiente pagina "https://www.selenium.dev/downloads/".
  
##instlacion de libreria selenium usar comando en la terminal:
-pip install selenium (se utiliza "pip" ya que esta en lenguaje python).

## tener presente que las versiones fueron con las que se realizo el Script.

##librerias:

-from selenium import webdriver
-from selenium.webdriver.common.by import By
-from selenium.webdriver.common.keys import Keys
-from selenium.webdriver.chrome.service import Service (opcional, se deja para lanzar navegador por medio de la clase "Service" del paquete "webdriver"
-import unittest (se deja libreria para poder realizar pruebas unitarias con una clase de metodo)
-import time

##Muchas gracias por su atencion
