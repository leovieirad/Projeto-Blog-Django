from django.core.exceptions import ValidationError

def validate_png(image):
    if image.name.lower().endswith('.png'):
        raise ValidationError('Imagem precisa ser PNG.')