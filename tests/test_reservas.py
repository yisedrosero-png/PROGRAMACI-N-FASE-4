# se importan las clases nesesarias desde el paquete de modelos        
from models.Order import Order
from models.Customer import Customer
from models.Services import Consulting
from utils.gestor_logs import log_error_message
from utils.validadores import validate_not_empty

# ahora se crea la funcion para realizar la prueba unitaria del proceso de reserva 
def probar_reserva():
    print("\n[TEST] Integrated Reservation System")
    try:
         # creamos cliente y servicio para la prueba
        cliente = Customer("C-001", "Ana Gomez", "ana@mail.com", "555", "Av. Central")
        servicio = Consulting("S-01", "Python Training", 100)
        id_system = "R-001" 
        validate_not_empty(id_system, "Order ID")
        
        # creamos la orden
        nueva_orden = Order(id_system="R-001", customer_id=cliente.id_system)
        nueva_orden.add_service(servicio)
        
        # esta parte es para confirmar o no el exito de la operacion
        print(f"Reservation successful for Client ID: {nueva_orden.customer_id}")
        print(f"Total services in order: {len(nueva_orden.service_list)}")

        # prueba de Error - Intentar agregar un servicio nulo
        if not servicio:
            raise ValueError("Cannot add an empty service to the order")
            
    except Exception as e:
        print(f"System Failure: {e}")
        log_error_message(f"Reservation Flow Error: {e}")

if __name__ == "__main__":
    probar_reserva()