# Test-code
Codigo para Calidad del software

Integrantes:
Emanuel Rojas Aguero
Kevin Villalobos Fernández 
Carolina Méndez Campos
Fabiola Mora Torres

Proyecto desarrollado en el lenguaje de python utilizando el web driver de selenium

Pasos para instalar el web driver:
  1- descargar el browser driver: "https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/"

En el archivo de python necesitaremos importar la libreria:

  1- from webdriver_manager.chrome import ChromeDriverManager

La variable service va a albergar la ubicacion de instalacion del web driver.
  
  1-service = Service(executable_path=ChromeDriverManager().install())
  
Por ultimo necesitamos inicializar el driver para poder utilizarlo:
  1- driver = webdriver.Chrome(service=service)


Paso para probar el proyecto crear un archivo de python con el nombre 'config'
Que contenga lo siguiente:

username = '' /* este el correo para realizar el login de la cuenta cada usuario le asigna el valor que desee*/
password = '' /* esta es contraseña para realizar el login de la cuenta cada usuario le asigna el valor correspondiente a la cuenta*/
website = 'https://www.netflix.com/cr-en/'
profile = '' /* En esta parte se le asigna el valor del nombre del perfil de netflix que va estar accediendo*/
