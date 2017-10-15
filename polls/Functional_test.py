__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/davidortiz/Downloads/chromedriver')
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('/Users/davidortiz/Downloads/1069335_10201430825270099_1021007166_n.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_login_independiente(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        nombreUsuario = self.browser.find_element_by_id('id_username_1')
        nombreUsuario.send_keys('juan645')
        clave = self.browser.find_element_by_id('id_password_1')
        clave.send_keys('clave123')
        botonLogin = self.browser.find_element_by_id('id_login_submmit')
        botonLogin.click()
        self.browser.implicitly_wait(3)
        editar_element = self.browser.find_element_by_id('id_editar')

        self.assertIn("Editar", editar_element.text)

    def test_edit_user(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        nombreUsuario = self.browser.find_element_by_id('id_username_1')
        nombreUsuario.send_keys('juan645')
        clave = self.browser.find_element_by_id('id_password_1')
        clave.send_keys('clave123')
        botonLogin = self.browser.find_element_by_id('id_login_submmit')
        botonLogin.click()
        self.browser.implicitly_wait(5)
        link = self.browser.find_element_by_id('id_editar')
        link.click()
        new_correo = 'jd.patino2@uniandes.edu.co'
        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys(new_correo)
        update = self.browser.find_element_by_id('id_update')
        update.click()

        self.browser.implicitly_wait(5)
        correo2 = self.browser.find_element_by_id('id_correo')
        self.assertIn(correo2.text, new_correo)

    def test_comments(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        comentario_nuevo = 'Hola esto es un comentario'

        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('david@gmail.com')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys(comentario_nuevo)
        boton = self.browser.find_element_by_id('adicionar_comentario')
        boton.click()
        self.browser.implicitly_wait(5)
        buscar_Correo = self.browser.find_element_by_name("david@gmail.com")
        print (buscar_Correo.text)
        self.assertIn('david@gmail.com', buscar_Correo.text)