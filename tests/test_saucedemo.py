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

def test_navegacion_catalogo(driver_logueado):
    """Verifica título, presencia de productos y elementos clave de la interfaz."""
    driver = driver_logueado
    espera = obtener_espera(driver)

    # Título de la pestaña del navegador
    assert driver.title == "Swag Labs", f"Título inesperado: {driver.title}"

    # Al menos un producto visible
    productos = espera.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    assert len(productos) > 0, "No se encontraron productos en el inventario"

    # Nombre y precio del primer producto
    primer_producto = productos[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {nombre} - {precio}")
    assert nombre != "", "El nombre del primer producto está vacío"
    assert precio.startswith("$"), f"Precio con formato inesperado: {precio}"

    # Elementos importantes de la interfaz: menú, filtro y carrito
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed(), "Falta el menú"
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed(), "Falta el filtro"
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed(), "Falta el carrito"