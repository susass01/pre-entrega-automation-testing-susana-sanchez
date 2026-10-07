"""Fixtures compartidos para todos los tests."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.helpers import hacer_login


@pytest.fixture
def driver():
    """Abre un Chrome nuevo para cada test y lo cierra al terminar."""
    opciones = Options()
    opciones.add_argument("--incognito")
    opciones.add_argument("--start-maximized")
    # Desactiva los popups de contraseñas de Chrome, que interfieren con la automatización
    opciones.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })

    navegador = webdriver.Chrome(options=opciones)
    yield navegador      # acá se ejecuta el test
    navegador.quit()     # corre siempre al final, pase o falle el test


@pytest.fixture
def driver_logueado(driver):
    """Entrega un navegador que ya inició sesión (para tests que parten del inventario)."""
    hacer_login(driver)
    return driver