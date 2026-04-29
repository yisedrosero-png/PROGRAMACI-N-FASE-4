# se importan las clases nesesarias desde el paquete de modelos
from models.Order import Order
from models.Customer import Customer
from models.Services import Consulting

# ahora se crea la funcion para realizar la prueba unitaria del proceso de reserva 
def probar_reserva():
    print("Probando sistema de reservas")
    try:
        # 1. creamos cliente y servicio para la prueba
        cliente = Customer("C-001", "Ana Gomez", "ana@mail.com", "555", "Av. Central")
        servicio = Consulting("S-01", "Asesoría Python", 100)
        
        # 2. creamos la orden
        nueva_orden = Order(id_system="R-001", customer_id=cliente.id_system)
        nueva_orden.add_service(servicio)
        
        # 3. esta parte es para confirmar o no el exito de la operacion 
        print(f" Reserva exitosa para el cliente ID: {nueva_orden.customer_id}")
        print(f" Servicios en la reserva: {len(nueva_orden.service_list)}")
    except Exception as e:
        print(f" Error en la reserva: {e}")

if __name__ == "__main__":
    probar_reserva()