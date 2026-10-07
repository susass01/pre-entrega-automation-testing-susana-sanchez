"""Funciones auxiliares para los tests de saucedemo.com."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constantes: si algo cambia, se modifica en un solo lugar
URL_BASE = "https://www.saucedemo.com"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"
TIEMPO_ESPERA = 10  # segundos máximos de espera explícita


def obtener_espera(driver):
    """Devuelve un WebDriverWait con el tiempo estándar del proyecto."""
    return WebDriverWait(driver, TIEMPO_ESPERA)


def hacer_login(driver, usuario=USUARIO_VALIDO, password=PASSWORD_VALIDO):
    """Navega a la página de login, ingresa credenciales y espera la redirección al inventario."""
    driver.get(URL_BASE)
    espera = obtener_espera(driver)

    # Espera explícita: no avanza hasta que el campo usuario sea visible
    campo_usuario = espera.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Espera a que la URL cambie al inventario
    espera.until(EC.url_contains("/inventory.html"))