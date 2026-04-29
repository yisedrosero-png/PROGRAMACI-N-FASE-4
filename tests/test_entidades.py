# se importa la clase customer desde el paquete de modelos para la validacion
from models.Customer import Customer

# funcion para realizar la prueva unitaria de la creacion de un cliente 
def probar_cliente():
    print("Probando creación de cliente ")
    try:
        # intentamos crear un cliente valido
        nuevo_cliente = Customer(id_system="C-001", name="Juan Perez", email="juan@mail.com", phone="12345", address="Calle 123")
        print(f" Cliente creado: {nuevo_cliente.name}")
    except Exception as e:
        print(f" Error al crear cliente: {e}")

if __name__ == "__main__":
    probar_cliente() 