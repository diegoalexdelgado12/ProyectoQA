from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time #Se deja la modulo de "time" para validar cada test por medio de la funcion "time.sleep"


class bugs_testing(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        time.sleep(7)

    def tearDown(cls):
        cls.driver.close()

    #Se encuentra bug donde en el formulario de registro nuevo usuario, el email se puede colocar para varios usuarios
    #Se encuentra bug sobre el password, deja realizar registro con 7 caracteres y sin caracter especial
       
    def test__bug_email_repetido_password_incorrecto(self):

        driver = self.driver
        driver.get("https://test-qa.inlaze.com/auth/sign-up")

       
        #Datos de nuevo usuario, con esta prueba validamos el bug que se puede dejar el mismo correo para varios usuarios 
        #dejaremos el email del usuarios que se registro en en CP 1.

        full_name = "Nombre Falso" #Nombre diferente al usuarios ya registrado
        email = "tom40@hotmail.com"
        password = "Error12" #El password no tiene la parametria de 8 caracteres y un caracter especial
        repeat_your_password = "Error12"

        #registro de campos obligatorios, guardar registro con el boton "Sing-Up"

        nombre_Falso = driver.find_element(By.XPATH, '//input [@id="full-name"]')
        nombre_Falso.send_keys(full_name)
        correo = driver.find_element(By.XPATH, '//input[@id="email"]')
        correo.send_keys(email)
        contraseña_inco = driver.find_element(By.XPATH, '//input[@id="password"]')
        contraseña_inco.send_keys(password)
        contraseña_conf= driver.find_element(By.XPATH, '//input[@id="confirm-password"]')
        contraseña_conf.send_keys(repeat_your_password)

        #termina registro con email de otro usuario y password sin parametria con cofirmacion de registro "Successful registration!"
               
        confirmar_registro = driver.find_element(By.XPATH, '//button[contains(text(),"Sign up")]')
        confirmar_registro.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()
    
    def test_Bug_registro_email_sin_formato_apellido_numerico(self):

        driver = self.driver
        driver.get("https://test-qa.inlaze.com/auth/sign-up")

        #Datos de usuario con email sin formato
        #apellido mnumerico, debe ser dos palabras con cadenas de caracteres alfabeticos

        full_name = "Nombre 2" #nombre incorrecto
        email = "sinformatohotmail.com"
        password = "Error13" #El password no tiene la parametria de 8 caracteres y un caracter especial
        repeat_your_password = "Error13"

        #registro de campos obligatorios, guardar registro con el boton "Sing-Up"

        nombre_inco = driver.find_element(By.XPATH, '//input [@id="full-name"]')
        nombre_inco.send_keys(full_name)
        correo = driver.find_element(By.XPATH, '//input[@id="email"]')
        correo.send_keys(email)
        contraseña_inco = driver.find_element(By.XPATH, '//input[@id="password"]')
        contraseña_inco.send_keys(password)
        contraseña_conf= driver.find_element(By.XPATH, '//input[@id="confirm-password"]')
        contraseña_conf.send_keys(repeat_your_password) 

        #termina registro con email sin formato falta "@" y password sin parametria con cofirmacion de registro "Successful registration!"
               
        confirmar_registro1 = driver.find_element(By.XPATH, '//button[contains(text(),"Sign up")]')
        confirmar_registro1.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

    def test_bug_inicio_sesion_email_sin_formato(self):

        driver = self.driver
        driver.get("https://test-qa.inlaze.com/auth/sign-in")
        time.sleep(10)

        #Datos de usuario con el email sin formato

        email = "sinformatohotmail.com"
        password = "Error13"

        #Se inicia sesion con usuario que lleva como email sin "@", falta de formato estandar de un correo electronico
        #Nuevamente se revisa en el password sin parametria, para inicio de sesion

        email_sin_formato = driver.find_element(By.XPATH, ('//input[@id="email"]'))
        email_sin_formato.send_keys(email)
        contraseña_sesion = driver.find_element(By.XPATH, ('//input[@id="password"]'))
        contraseña_sesion.send_keys(password)
        inicio_sesion = driver.find_element(By.XPATH, ('//button[contains(text(),"Sign in")]'))
        inicio_sesion.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()     


if __name__ == '__main__':
    unittest.main()
