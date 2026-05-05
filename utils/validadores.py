import re

def validate_not_empty(value, field_name="Field"):
    """
    Verifica que un campo no esté vacío
    """
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} cannot be empty")

def validate_length(value, min_len=1, max_len=255, field_name="Field"):
    """
    Verifica que el texto tenga una longitud válida
    """
    length = len(str(value))
    if length < min_len or length > max_len:
        raise ValueError(f"{field_name} must be between {min_len} and {max_len} characters")

def validate_email(email):
    """
    Verifica que el correo tenga formato válido
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format")

def validate_only_numbers(value, field_name="Field"):
    """
    Verifica que solo contenga números
    """
    if not str(value).isdigit():
        raise ValueError(f"{field_name} must contain only numbers")

def validate_range(value, min_val=None, max_val=None, field_name="Field"):
    """
    Verifica que un número esté dentro de un rango
    """
    try:
        number = float(value)
    except:
        raise ValueError(f"{field_name} must be a number")
    if min_val is not None and number < min_val:
        raise ValueError(f"{field_name} cannot be less than {min_val}")
    if max_val is not None and number > max_val:
        raise ValueError(f"{field_name} cannot be greater than {max_val}")

def validate_safe_text(value, field_name="Field"):
    """
    Evita caracteres peligrosos (SQL Injection básica)
    """
    pattern = r'^[a-zA-Z0-9\sáéíóúÁÉÍÓÚñÑ.,_-]+$'
    if not re.match(pattern, value):
        raise ValueError(f"{field_name} contains invalid characters")