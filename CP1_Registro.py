from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import unittest
import time #Se deja la modulo de "time" para validar cada test por medio de la funcion "time.sleep"


class registro_nuevo_usuario(unittest.TestCase):

    @classmethod

    def setUp(cls): 
      
        #Desde mi maquina incio la webdriver desde le modulo service (opcional)
        #navegador = Service ("C:\ChromeDriver\chromedriver.exe")
        #inicio de navegador utilizando el modulo de "Service"
        #cls.driver = webdriver.Chrome(service=navegador) 

        #iniciar navegador (chrome)

        cls.driver = webdriver.Chrome()
        time.sleep(7)
      
    def tearDown(cls):
        cls.driver.close()

        #ingresar a la pagina principal para realizar un registro de nuevo usuario, ingresar al enlace registro "Sing-up"
        
    def test_registro(self): 

        #busqueda de pagina web
        driver = self.driver
        driver.get("https://test-qa.inlaze.com/auth/sign-in")

        registro = driver.find_element(By.XPATH, '//span/a[contains(text(),"Sign up")]')
        registro.click()
        time.sleep(7)

        #realizar registro de un usuario nuevo

        full_name = "Tom Araya"
        email = "tom40@hotmail.com"
        password = "Slayer12+"
        repeat_your_password = "Slayer12+"
        repeat_your_password_distinta = "Motorhead12+"

        #registro de campos obligatorios, guardar registro con el boton "Sing-Up"

        nombre_apellido = driver.find_element(By.XPATH, '//input [@id="full-name"]')
        nombre_apellido.send_keys(full_name)

        correo = driver.find_element(By.XPATH, '//input[@id="email"]')
        correo.send_keys(email)

        contraseña = driver.find_element(By.XPATH, '//input[@id="password"]')
        contraseña.send_keys(password)

        #Se realiza validacion de contraseña, donde en el campo confirmar contraseña se deja un diferente para saltar un error de "Passwords do not match"

        contraseña_conf_errada= driver.find_element(By.XPATH, '//input[@id="confirm-password"]')
        contraseña_conf_errada.send_keys(repeat_your_password_distinta)
        time.sleep(10)

        mensaje_password = driver.find_element(By.XPATH, ('//span[contains(text(),"Passwords do not match")]'))
        self.assertTrue(mensaje_password.is_displayed(),"contraseña no compatible")
        
        #Se limpia el campo de "confirm.password" para volverlo a diligenciar con la contraseña correcta

        contraseña_conf_errada.clear() 
        time.sleep(10)

        #Constraseña correcta

        contraseña_conf= driver.find_element(By.XPATH, '//input[@id="confirm-password"]')
        contraseña_conf.send_keys(repeat_your_password)
        guardar = driver.find_element(By.XPATH, '//button[contains(text(),"Sign up")]')
        guardar.click()

        #termina registro de nuevo usuario
        time.sleep(10)

        #validacion de registro aprobado

        aprobacion = driver.find_element(By.XPATH, ('//div[contains(text(),"Successful registration!")]'))
        self.assertTrue(aprobacion.is_displayed(),"aprobacion no encontrada")

        #se realizo un registro interno para validar que se aprobo el registro
        
        print("Registro culminado")
        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()



