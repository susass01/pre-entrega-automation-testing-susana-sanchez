# Pre-entrega Automation Testing - Susana Sanchez

## Propósito del proyecto
Automatización de flujos básicos de navegación web sobre
[saucedemo.com](https://www.saucedemo.com) utilizando Selenium WebDriver y Python.
Se automatizan tres casos de prueba: login, navegación del catálogo y carrito de compras.

## Tecnologías utilizadas
- Python 3
- Pytest (estructura de testing)
- Selenium WebDriver (automatización del navegador)
- pytest-html (reportes en HTML)
- Git y GitHub (control de versiones)

## Requisitos previos
- Python 3.10 o superior
- Google Chrome instalado

## Instalación de dependencias
1. Clonar el repositorio:
```
   git clone https://github.com/susass01/pre-entrega-automation-testing-susana-sanchez.git
   cd pre-entrega-automation-testing-susana-sanchez
```
2. Crear y activar un entorno virtual:
```
   python -m venv venv
   venv\Scripts\activate
```
   En Mac/Linux: `source venv/bin/activate`
3. Instalar las dependencias:
```
   pip install -r requirements.txt
```

## Cómo ejecutar las pruebas
```
python -m pytest tests/test_saucedemo.py -v
```
Para ver también lo que imprimen los tests (nombre y precio del primer producto):
```
python -m pytest tests/test_saucedemo.py -v -s
```

## Generar el reporte HTML
```
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```
El reporte se guarda en `reports/reporte.html`.

## Casos de prueba
| Test | Qué valida |
|------|-----------|
| `test_login_exitoso` | Login con `standard_user`, redirección a `/inventory.html`, texto "Products" y "Swag Labs" |
| `test_navegacion_catalogo` | Título de la página, presencia de productos, nombre y precio del primero, menú, filtro y carrito |
| `test_agregar_producto_al_carrito` | Agrega el primer producto, verifica el contador del carrito y que el ítem aparezca en el carrito |

## Estructura del proyecto
```
├── tests/        casos de prueba
├── utils/        funciones auxiliares (login, esperas)
├── datos/        datos externos (sin uso por ahora)
├── reports/      reportes HTML
├── conftest.py   fixtures de pytest (navegador y sesión iniciada)
└── requirements.txt
```

## Autora
Susana Sanchez