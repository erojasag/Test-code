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
