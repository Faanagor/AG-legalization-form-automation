import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Cargar credenciales del archivo .env
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
CHROMEDRIVER_PATH = "statics/chromedriver-win64/chromedriver.exe"


def send_gmail(to_email, subject, message):
    """Función para enviar un correo usando Gmail y Selenium."""
    # Configuración del controlador
    # service = Service("ruta/a/chromedriver")  # Cambia la ruta según tu instalación
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get("https://mail.google.com/")
    wait = WebDriverWait(driver, 15)

    try:
        # Iniciar sesión
        wait.until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys(EMAIL, Keys.RETURN)
        time.sleep(2)  # Espera para cargar la página de contraseña
        wait.until(EC.presence_of_element_located((By.NAME, "Passwd"))).send_keys(PASSWORD, Keys.RETURN)

        # Redactar un correo
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Redactar']"))).click()
        time.sleep(2)  # Espera para cargar el formulario de redacción
        wait.until(EC.presence_of_element_located((By.NAME, "to"))).send_keys(to_email)
        driver.find_element(By.NAME, "subjectbox").send_keys(subject)
        driver.find_element(By.XPATH, "//div[@aria-label='Cuerpo del mensaje']").send_keys(message)

        # Enviar el correo
        driver.find_element(By.XPATH, "//div[text()='Enviar']").click()
        print("Correo enviado con éxito.")

    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        # Cerrar el navegador
        time.sleep(5)
        driver.quit()


# Ejemplo de uso
if __name__ == "__main__":
    DESTINATARIO = "faanagor@gmail.com"
    ASUNTO = "Asunto de prueba"
    MENSAJE = "Este es un mensaje de prueba enviado con Selenium."
    send_gmail(DESTINATARIO, ASUNTO, MENSAJE)


# import time

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# CHROMEDRIVER_PATH = "statics/chromedriver-win64/chromedriver.exe"
# URL = "https://gmail.com"
# USER_CREDENTIAL = "est.forozco460@smart.edu.co"
# PASSWORD_CREDENTIAL = "Sm4rt4256*"

# chrome_options = Options()
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--user-data-dir=/path/to/custom/temp")  # Cambia la ruta por una válida en tu sistema

# service = Service(executable_path=CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.get(URL)

# # Interactúa con el formulario de inicio de sesión
# try:
#     user = driver.find_element("id", "identifierId")
#     user.send_keys(USER_CREDENTIAL)
#     user.send_keys(Keys.ENTER)
#     time.sleep(10)
#     password = driver.find_element("name", "password")
#     password.send_keys(PASSWORD_CREDENTIAL)
#     password.send_keys(Keys.ENTER)
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     driver.quit()
