# Estructura y Finalidad del Proyecto: CONTECCIB 2024

Este proyecto es una aplicación web desarrollada con **Django** diseñada para la gestión integral de congresos, talleres y participantes.

## Finalidad
La plataforma sirve como un sistema de gestión centralizado para organizar eventos académicos o técnicos. Permite la administración de diferentes actores (talleristas, participantes) y la gestión de talleres asociados al congreso.

## Estructura del Proyecto

```text
/
├── congress/           # Configuración principal del proyecto Django
├── home/               # Módulo de la página principal/landing
├── participant/        # Gestión de participantes del congreso
├── tutor/              # Gestión de tutores/talleristas
├── workshop/           # Gestión de talleres y actividades
├── static/             # Archivos estáticos (CSS, JS, imágenes)
├── templates/          # Plantillas HTML base del proyecto
├── manage.py           # Script de línea de comandos de Django
└── requirements.txt    # Dependencias del proyecto
```

## Componentes Clave

*   **`congress/`**: Contiene la configuración global (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`).
*   **Módulos (`home`, `participant`, `tutor`, `workshop`)**: Cada uno es una aplicación de Django encargada de una funcionalidad específica, siguiendo la arquitectura modular del framework.
*   **`templates/`**: Almacena las vistas HTML que definen la interfaz de usuario.
*   **`static/`**: Contiene archivos CSS, JavaScript y elementos multimedia necesarios para el frontend.

## Guía Básica

Para ejecutar el proyecto, asegúrate de tener configurado el entorno virtual y las dependencias:

1.  **Activar entorno virtual:**
    ```bash
    source venv/bin/activate
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

## Notas sobre Diseño y UI

El proyecto utiliza una paleta de colores moderna (verde `#2D5A27`, naranja `#E67E22` y blanco) para mejorar la experiencia del usuario.

*   **Paleta de colores**: Se han definido variables CSS globales (`--primary-color`, `--secondary-color`, etc.) en `congress/static/css/styles.css` para asegurar consistencia.
*   **Modernización**: Se han refinado las sombras, bordes y tipografía, y se han añadido efectos de transición en componentes interactivos como enlaces y botones.
