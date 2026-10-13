# Resumen de cambios

Este documento resume los ajustes realizados al sistema de registro de participantes y talleres.

## Control de aforo e inscripción

- La disponibilidad de lugares y el estado de taller lleno se calculan con el número de participantes relacionados con el taller. Esto evita depender de un contador que podía quedar desactualizado.
- La inscripción se realiza dentro de una transacción y bloquea los registros del participante y del taller para evitar sobrecupo por solicitudes simultáneas y dobles inscripciones.
- La vista valida en el servidor que el participante tenga su folio validado, que no esté inscrito en otro taller y que haya lugares disponibles.
- La ruta de inscripción solo acepta solicitudes `POST`.
- Se conserva `seats_occupied` por compatibilidad y se sincroniza al completar una inscripción.
- Los participantes sin folio validado pueden consultar los talleres, pero no inscribirse. La vista rechaza también solicitudes que intenten saltarse la interfaz.

## Permisos de tutores

- Al crear tutores ya no se activa `is_superuser`.
- Se conserva `is_staff`, que la aplicación utiliza para permitir el acceso a la gestión de folios.
- La generación de contraseñas de tutores no se modificó.
- Los instructores ya se creaban sin privilegios de superusuario; su generación de contraseña tampoco se modificó.

## Datos del ponente en el detalle del taller

- La página de detalle ahora obtiene el ponente desde la relación `workshop.instructor`.
- Muestra la foto cuando está disponible, además del título, nombre y semblanza.
- Muestra un mensaje cuando el taller no tiene instructor asignado.
- Se agregaron estilos para presentar la foto del instructor de forma circular.

## Archivos principales modificados

- `congress/workshop/models.py`
- `congress/workshop/views.py`
- `congress/tutor/views.py`
- `congress/templates/workshop/detail.html`
- `congress/static/css/styles.css`

## Verificación

No se ejecutaron pruebas automatizadas durante estos cambios.
