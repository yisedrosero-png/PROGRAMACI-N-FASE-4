# se importan las clases de los módulos Services, Customer y Order para utilizarlas en el código
from models.Customer import Customer
from models.Services import Consulting, EquipmentRental, RoomReservation
from models.catalog import ServiceCatalog
from models.Order import Order 

# se importan las funciones de validación y el gestor de logs para utilizarlos en el código
from utils.validadores import (
    validate_email,
    validate_not_empty,
    validate_only_numbers,
    validate_safe_text
)
from utils.gestor_logs import log_error_message

customer_list = [] # se define una lista para almacenar los clientes registrados en el sistema
catalog = ServiceCatalog() # se crea una instancia del catálogo de servicios para poder acceder a los servicios disponibles al crear un nuevo pedido    

# se define una función para registrar un nuevo cliente, que solicita al usuario ingresar los datos del cliente y devuelve una instancia de la clase Customer con esos datos
def register_customer():
    print("--- Customer Registration ---")

    # se utiliza un bucle while para permitir al usuario corregir los errores de validación sin salir del proceso de registro, y se manejan las excepciones para mostrar mensajes de error y registrar los errores en el log
    while True:
        try:
            name = input("Full Name: ")
            validate_not_empty(name, "Name")
            validate_safe_text(name, "Name")

            email = input("Email: ")
            validate_email(email)

            phone = input("Phone: ")
            validate_only_numbers(phone, "Phone")

            address = input("Address: ")
            validate_not_empty(address, "Address")
            validate_safe_text(address, "Address")

            # Creamos una nueva instancia de Customer con un ID generado automáticamente basado en la cantidad de clientes registrados
            new_customer = Customer(
                id_system=f"C{len(customer_list)+1:03d}", 
                name=name, 
                email=email, 
                phone=phone, 
                address=address
                )
    # se devuelve la nueva instancia de Customer creada con los datos ingresados por el usuario
            return new_customer
    
        except ValueError as error:
            # Si un validador lanza un error, saltamos aquí
            print(f"\n[!] Input Error: {error}")
            log_error_message(f"Registration Error: {error}")
            print("Please try again.\n")

# se define una función para crear un nuevo pedido, que muestra el catálogo de servicios disponibles, solicita al usuario ingresar el ID del servicio que desea contratar y devuelve una instancia de la clase Order con el cliente y el servicio seleccionado, o None si no se encuentra el servicio
def create_order(customer):
    print("\n--- Available Services ---")
    # se muestra el catálogo de servicios disponibles, iterando sobre la lista de servicios en el catálogo y mostrando la información de cada servicio utilizando el método get_info de cada servicio
    for s in catalog.services:
        print(s.get_info())
    
    service_id = input("Enter the ID of the service to hire: ")
    selected_service = catalog.find_service_by_id(service_id) # Buscar servicio por ID
    
    if selected_service:
        new_order = Order(id_system=f"O{len(customer_list)+1:03d}", customer_id=customer.id_system)
        new_order.add_service(selected_service) # Agregar el servicio seleccionado al pedido
        return new_order
    else:
        print("Service not found.")
        log_error_message(f"Order Error: Service ID {service_id} not found.") # Sugerencia técnica
        return None

# se llama a la función para registrar un nuevo cliente y se almacena el resultado en la variable new_client, luego se agrega el nuevo cliente a la lista de clientes registrados en el sistema y se muestra un mensaje de confirmación con el nombre y el ID del cliente registrado
new_client = register_customer() # se llama a la función para registrar un nuevo cliente y se almacena el resultado en la variable new_client
customer_list.append(new_client) # se agrega el nuevo cliente a la lista de clientes registrados en el sistema
print(f"Customer {new_client.name} registered successfully with ID: {new_client.id_system}") # se muestra un mensaje de confirmación con el nombre y el ID del cliente registrado

# se crea una instancia del catálogo de servicios para poder acceder a los servicios disponibles al crear un nuevo pedido
order = create_order(new_client)
if order:
    print(f"Order created successfully for {new_client.name}!")
    print(f"Service hired: {order.service_list[0].name}, Total Cost: ${order.calculate_total()}")
    