# 🧪 Web Automation Suite (Selenium, Python & Pytest)

Proyecto de pruebas automatizadas de interfaz web diseñado bajo el patrón de arquitectura **Page Object Model (POM)**, utilizando **Python**, **Selenium WebDriver** y **Pytest**. El objetivo principal es validar flujos de búsqueda en el motor de búsqueda **DuckDuckGo**, asegurando escalabilidad, mantenibilidad y robustez en las ejecuciones.

---

## 🛠️ Tecnologías y Herramientas
* 🐍 **Python 3.x** - Lenguaje de programación base.
* 🌐 **Selenium WebDriver** - Automatización e interacción con navegadores web.
* 🧪 **Pytest** - Framework de pruebas y gestión de fixtures.
* 🏛️ **Page Object Model (POM)** - Patrón de diseño para separar la lógica de negocio de los localizadores.
* 📄 **JSON** - Archivo de configuración centralizada para parámetros de entorno (*browser*, tiempos de espera, etc.).

---

## 📁 Estructura del Proyecto

```text
tau_selenium/
├── config.json          # Configuración global (navegador, tiempos, headless)
├── pages/               # Capa de Objetos de Página (POM)
│   ├── search.py        # Localizadores y acciones de la página principal
│   └── result.py        # Localizadores y acciones de la página de resultados
├── tests/               # Capa de Pruebas
│   ├── conftest.py      # Fixtures de Pytest y configuración del driver
│   └── test_search.py   # Casos de prueba parametrizados
└── README.md            # Documentación del proyecto