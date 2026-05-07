# se importa la clase customer desde el paquete de modelos para la validacion   
from models.Customer import Customer
# importación de utilidades segun el estandar del equipo
from utils.validadores import validate_email, validate_only_numbers, validate_not_empty
from utils.gestor_logs import log_error_message

def probar_cliente():
    print("\n[TEST] Customer Entity Creation")
    
    # lista de casos para cubrir exito y errores (4 casos)
    casos = [
        {"id": "C-001", "name": "Juan Perez", "email": "juan@mail.com", "phone": "12345"}, # Éxito
        {"id": "C-002", "name": "Ana Lopez", "email": "email-invalido", "phone": "555"},   # Error Email
        {"id": "C-003", "name": "Luis Diaz", "email": "luis@mail.com", "phone": "abc"},    # Error Phone
        {"id": "C-004", "name": "", "email": "test@mail.com", "phone": "999"}              # Error Nombre
    ]

    for datos in casos:
        try:
            print(f"Testing client: {datos['name']}...")
            # Uso de Validadores antes de crear el objeto
            if not validate_email(datos['email']):
                raise ValueError("Invalid email format detected")
            if not validate_only_numbers(datos['phone']):
                raise ValueError("Invalid phone format: only numbers allowed")
            
            nuevo_cliente = Customer(datos['id'], datos['name'], datos['email'], datos['phone'], "Calle 123")
            print(f"Success: Customer {nuevo_cliente.name} created.")
            
        except Exception as e:
            # integración obligatoria con el Gestor de Logs
            print(f"Error: {e}")
            log_error_message(f"Entity Test Failure: {e}")

if __name__ == "__main__":
    probar_cliente()