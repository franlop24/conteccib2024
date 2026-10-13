# validators.py
import re

from django.core.exceptions import ValidationError
from PIL import Image, UnidentifiedImageError

def validate_image(image):
    if not image:
        return

    max_size_mb = 2
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(
            f"El tamaño máximo permitido para la imagen es de {max_size_mb} MB."
        )

    try:
        image.seek(0)
        with Image.open(image) as opened_image:
            opened_image.verify()
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError):
        raise ValidationError("El archivo no es una imagen válida o está dañado.")
    finally:
        image.seek(0)


def validate_phone(value):
    phone_regex = re.compile(r'^\d{10}$')  # Permite solo 10 dígitos
    if not phone_regex.match(value):
        raise ValidationError("El número de teléfono no es válido. Deben ser 10 dígitos.")
