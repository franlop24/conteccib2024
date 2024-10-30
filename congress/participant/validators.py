# validators.py
from django.core.exceptions import ValidationError
from PIL import Image

def validate_image(image):
    # Validar tamaño en KB
    max_size_kb = 800  # Tamaño máximo en KB
    if image:
        if image.size > max_size_kb * 1024:
            raise ValidationError(f"El tamaño máximo permitido para la imagen es de {max_size_kb}KB.")

        # Validar dimensiones (ancho y alto)
        max_width = 640  # Ancho máximo en píxeles
        max_height = 720  # Alto máximo en píxeles

        # Abrir la imagen con Pillow
        img = Image.open(image)
        width, height = img.size

        if width > max_width or height > max_height:
            raise ValidationError(f"Las dimensiones máximas permitidas son {max_width}x{max_height} píxeles.")
