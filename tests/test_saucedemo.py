"""Casos de prueba automatizados para saucedemo.com."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import hacer_login, obtener_espera


def test_login_exitoso(driver):
    """Login con credenciales válidas y validación de la página de inventario."""
    hacer_login(driver)
    espera = obtener_espera(driver)

    # Validación 1: la URL corresponde al inventario
    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"

    # Validación 2: el encabezado de la sección dice "Products"
    titulo_seccion = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo_seccion.text == "Products"

    # Validación 3: el logo de la app dice "Swag Labs"
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs"