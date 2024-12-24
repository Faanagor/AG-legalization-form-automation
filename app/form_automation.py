import email
import imaplib
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CHROMEDRIVER_PATH = "AG-legalization-form-automation/statics/chromedriver-win64/chromedriver.exe"
# Carga las variables de entorno
load_dotenv()
service = Service(executable_path=CHROMEDRIVER_PATH)
# Configuración del WebDriver
driver = webdriver.Chrome()  # Usa el driver adecuado para tu navegador
driver.get("https://example.com/formulario")

# Llenar y enviar el formulario
try:
    # Esperar a que el campo esté disponible
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "campo-usuario")))
    usuario = driver.find_element(By.ID, "campo-usuario")
    usuario.send_keys("mi_usuario")

    password = driver.find_element(By.ID, "campo-password")
    password.send_keys("mi_password")
    password.send_keys(Keys.RETURN)
except Exception as e:
    print(f"Error: {e}")
    driver.quit()


# Obtener el código del mensaje (Ejemplo con IMAP)
def obtener_codigo_email():
    imap_host = "imap.gmail.com"
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")

    with imaplib.IMAP4_SSL(imap_host) as mail:
        mail.login(email_user, email_pass)
        mail.select("inbox")
        _, data = mail.search(None, "ALL")
        latest_email_id = data[0].split()[-1]
        _, email_data = mail.fetch(latest_email_id, "(RFC822)")
        for response_part in email_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            # Extrae el código con regex o búsqueda
                            return body.split("Código:")[1].strip()
    return None


# Insertar el código en el formulario
try:
    codigo = obtener_codigo_email()
    if codigo:
        campo_codigo = driver.find_element(By.ID, "campo-codigo")
        campo_codigo.send_keys(codigo)
        boton_enviar = driver.find_element(By.ID, "boton-enviar")
        boton_enviar.click()
    else:
        print("No se pudo obtener el código.")
finally:
    driver.quit()
