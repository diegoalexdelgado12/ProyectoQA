from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time #Se deja la modulo de "time" para validar cada test por medio de la funcion "time.sleep"

class inicio_sesion_usuario_nuevo(unittest.TestCase):
    
    @classmethod
    def setUp(cls):

        cls.driver = webdriver.Chrome()
        time.sleep(7)

    def tearDown(cls):
        cls.driver.close()

        #Inicio de sesion de nuevo usario en pagina de inicio

    def test_inicio_sesion(self):

        #Busqueda de la pagina web

        driver = self.driver
        driver.get("https://test-qa.inlaze.com/auth/sign-in")
        time.sleep(7)

        #Datos de nuevo usuario para inicio de sesion

        email = "tom40@hotmail.com"
        password = "Slayer12+"

        #Se realiza formulario para inicio de sesion

        email_sesion = driver.find_element(By.XPATH, ('//input[@id="email"]'))
        email_sesion.send_keys(email)

        contraseña_sesion = driver.find_element(By.XPATH, ('//input[@id="password"]'))
        contraseña_sesion.send_keys(password)

        ingresar_sesion = driver.find_element(By.XPATH, ('//button[contains(text(),"Sign in")]'))
        ingresar_sesion.click()

        #Inicio de sesion de usuario, para el ingreso a la plataforma
                     
        time.sleep(10)
        #Validacion de que si muestra el nombre despues de ingresar a la plataforma (nombre y apellido que se hicieron registro)

        nombre_sesion = driver.find_element(By.XPATH, ('//h2[contains(text(),"Tom Araya")]'))
        self.assertTrue(nombre_sesion.is_displayed(),"nombre no esta")

        #Mensaje en consola
        
        print("si se encuentra el nombre")
        time.sleep(10)

    def tearDown(self):
        self.driver.close()
           
    def test_validacion_cierre_sesion(self):

        driver = self.driver
        driver.get("https://test-qa.inlaze.com/auth/sign-in")

        time.sleep(7)

        #Datos de nuevo usuario para inicio de sesion

        email = "tom40@hotmail.com"
        password = "Slayer12+"

        #rellena formulario mismo usuario

        email_sesion = driver.find_element(By.XPATH, ('//input[@id="email"]'))
        email_sesion.send_keys(email)
        contraseña_sesion = driver.find_element(By.XPATH, ('//input[@id="password"]'))
        contraseña_sesion.send_keys(password)
        ingresar_sesion = driver.find_element(By.XPATH, ('//button[contains(text(),"Sign in")]'))
        ingresar_sesion.click()

        time.sleep(10)

        #Se selecciona perfil para desplegar opciones

        icono = driver.find_element(By.XPATH, ('//div[@class="w-10 rounded-full"]'))
        icono.click()
        time.sleep(10)

        #En las opciones buscamos la opcion para cerrar sesion "Logout"

        cierre_sesion = driver.find_element(By.XPATH, ('//li/a[contains(text(),"Logout")]'))
        cierre_sesion.click()
        time.sleep(10)                                               

        #Mensaje en consola 

        print("sesion cerrada")

    def tearDown(self):
        self.driver.close()

    def test_validacion_incio_sesion_imcopleto(self):

        driver = self.driver
        driver.get("https://test-qa.inlaze.com/auth/sign-in")
        time.sleep(7)

        #Datos de nuevo usuario para inicio de sesion, se agrega una variable incompleto (email)

        email = "tom40@hotmail.com"
        password = "Slayer12+"
        email_incompleto = "tom40@hotmail"

        email_sesion = driver.find_element(By.XPATH, ('//input[@id="email"]'))
        email_sesion.send_keys(email_incompleto)
        contraseña_sesion = driver.find_element(By.XPATH, ('//input[@id="password"]'))
        contraseña_sesion.send_keys(password)
        ingresar_sesion = driver.find_element(By.XPATH, ('//button[contains(text(),"Sign in")]'))
        ingresar_sesion.click()
        time.sleep(10)

        #Se realiza utiliza un metodo de asecion para validar que el email este completo

        self.assertIn(email_incompleto, email, "formulario incompleto")

        #Se valida que nos comunique el error de registro ya que el formulario no se encuentra con los campos completos en este caso (email) errado

        Registro_fallido = driver.find_element(By.XPATH, ('//div[contains(text(),"User not found")]'))
        self.assertTrue(Registro_fallido.is_displayed(),"email completo")

        #Mensaje de consolo 

        print("email no registrado")
        time.sleep(10)

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
