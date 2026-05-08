# se importan librerias para permitir que el archivo pueda encontrar las carpetas models y utils
import sys
import os

# se agrega la ruta principal del proyecto para poder importar las clases desde la carpeta tests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# se importan las clases necesarias del sistema
from models.Customer import Customer
from models.Order import Order
from models.Services import Consulting, EquipmentRental, RoomReservation
from models.catalog import ServiceCatalog

# se importan las funciones de validacion y el gestor de logs
from utils.validadores import (
    validate_email,
    validate_not_empty,
    validate_only_numbers,
    validate_range,
    validate_safe_text
)
from utils.gestor_logs import log_error_message


# se define una funcion general para ejecutar cada prueba sin detener el programa cuando ocurre un error
def ejecutar_prueba(numero, descripcion, funcion):
    print("\n------------------------------------------------------------")
    print(f"Operacion {numero}: {descripcion}")
    print("------------------------------------------------------------")

    try:
        funcion()
        print("Resultado: operacion ejecutada correctamente")
    except Exception as e:
        print(f"Resultado: error controlado -> {e}")
        log_error_message(f"Operacion {numero} - {descripcion}: {e}")
    finally:
        print("El sistema continua funcionando despues de la operacion")


# se prueba el registro de un cliente valido
def probar_cliente_valido():
    name = "Carlos Perez"
    email = "carlos@mail.com"
    phone = "3001234567"
    address = "Calle 10"

    validate_not_empty(name, "Name")
    validate_safe_text(name, "Name")
    validate_email(email)
    validate_only_numbers(phone, "Phone")
    validate_not_empty(address, "Address")
    validate_safe_text(address, "Address")

    cliente = Customer("C-001", name, email, phone, address)
    print(cliente.get_info())


# se prueba un cliente con nombre vacio para validar el manejo del error
def probar_cliente_nombre_vacio():
    name = ""
    email = "ana@mail.com"
    phone = "3005555555"
    address = "Carrera 20"

    validate_not_empty(name, "Name")
    validate_email(email)
    validate_only_numbers(phone, "Phone")

    cliente = Customer("C-002", name, email, phone, address)
    print(cliente.get_info())


# se prueba un cliente con correo invalido
def probar_cliente_correo_invalido():
    name = "Ana Gomez"
    email = "correo-invalido"
    phone = "3005555555"
    address = "Carrera 20"

    validate_not_empty(name, "Name")
    validate_email(email)
    validate_only_numbers(phone, "Phone")

    cliente = Customer("C-003", name, email, phone, address)
    print(cliente.get_info())


# se prueba un cliente con telefono invalido
def probar_cliente_telefono_invalido():
    name = "Luis Martinez"
    email = "luis@mail.com"
    phone = "ABC123"
    address = "Avenida Central"

    validate_not_empty(name, "Name")
    validate_email(email)
    validate_only_numbers(phone, "Phone")

    cliente = Customer("C-004", name, email, phone, address)
    print(cliente.get_info())


# se prueba la creacion correcta de un servicio de consultoria
def probar_servicio_consultoria_valido():
    servicio = Consulting("S-001", "Asesoria en Python", 100000, 2)

    validate_not_empty(servicio.name, "Service Name")
    validate_range(servicio.price, min_val=1, field_name="Service Price")
    validate_range(servicio.hours, min_val=1, field_name="Service Hours")

    print(servicio.get_info())


# se prueba un servicio con precio invalido
def probar_servicio_precio_invalido():
    servicio = Consulting("S-002", "Asesoria con precio invalido", -50000, 2)

    validate_not_empty(servicio.name, "Service Name")
    validate_range(servicio.price, min_val=1, field_name="Service Price")
    validate_range(servicio.hours, min_val=1, field_name="Service Hours")

    print(servicio.get_info())


# se prueba la creacion correcta de un alquiler de equipo
def probar_alquiler_equipo_valido():
    servicio = EquipmentRental("E-001", "Portatil de alto rendimiento", 80000, 3)

    validate_not_empty(servicio.name, "Equipment Name")
    validate_range(servicio.price, min_val=1, field_name="Equipment Price")
    validate_range(servicio.days, min_val=1, field_name="Rental Days")

    print(servicio.get_info())


# se prueba la creacion correcta de una reserva de sala
def probar_reserva_sala_valida():
    servicio = RoomReservation("R-001", "Sala de reuniones", 120000, 4)

    validate_not_empty(servicio.name, "Room Name")
    validate_range(servicio.price, min_val=1, field_name="Room Price")
    validate_range(servicio.hours, min_val=1, field_name="Reservation Hours")

    print(servicio.get_info())


# se prueba la busqueda de un servicio existente dentro del catalogo
def probar_busqueda_servicio_existente():
    catalogo = ServiceCatalog()
    servicio = catalogo.find_service_by_id("C001")

    if servicio is None:
        raise ValueError("Service not found")

    print(servicio.get_info())


# se prueba la busqueda de un servicio que no existe dentro del catalogo
def probar_busqueda_servicio_inexistente():
    catalogo = ServiceCatalog()
    servicio = catalogo.find_service_by_id("NO-EXISTE")

    if servicio is None:
        raise ValueError("Service not found in catalog")

    print(servicio.get_info())


# se prueba la creacion de una orden valida con dos servicios
def probar_orden_valida():
    cliente = Customer("C-005", "Martha Rios", "martha@mail.com", "3112223333", "Calle 30")

    servicio_1 = Consulting("S-003", "Asesoria de arquitectura", 150000, 2)
    servicio_2 = EquipmentRental("E-002", "Equipo de videoconferencia", 90000, 1)

    orden = Order("O-001", cliente.id_system)
    orden.add_service(servicio_1)
    orden.add_service(servicio_2)

    print(orden.get_info())
    print(f"Cliente relacionado: {cliente.name}")
    print(f"Total de servicios agregados: {len(orden.service_list)}")


# se prueba un error al intentar agregar un servicio vacio a una orden
def probar_servicio_vacio_en_orden():
    cliente = Customer("C-006", "Pedro Lopez", "pedro@mail.com", "3124445555", "Calle 40")
    orden = Order("O-002", cliente.id_system)

    servicio = None

    if servicio is None:
        raise ValueError("Cannot add an empty service to the order")

    orden.add_service(servicio)
    print(orden.get_info())


# se prueba un calculo adicional aplicando impuesto y descuento de forma manual
def probar_calculo_con_impuesto_descuento():
    servicio = Consulting("S-004", "Consultoria especializada", 200000, 3)

    costo_base = servicio.calculate_cost()
    impuesto = costo_base * 0.19
    descuento = 50000
    total = costo_base + impuesto - descuento

    print(f"Costo base: {costo_base}")
    print(f"Impuesto 19%: {impuesto}")
    print(f"Descuento: {descuento}")
    print(f"Total final: {total}")


# se define la funcion principal para ejecutar todas las operaciones simuladas
def main():
    print("\n============================================================")
    print("SIMULACION DE OPERACIONES DEL SISTEMA SOFTWARE FJ")
    print("============================================================")

    ejecutar_prueba(1, "Registro de cliente valido", probar_cliente_valido)
    ejecutar_prueba(2, "Registro de cliente con nombre vacio", probar_cliente_nombre_vacio)
    ejecutar_prueba(3, "Registro de cliente con correo invalido", probar_cliente_correo_invalido)
    ejecutar_prueba(4, "Registro de cliente con telefono invalido", probar_cliente_telefono_invalido)
    ejecutar_prueba(5, "Creacion de servicio de consultoria valido", probar_servicio_consultoria_valido)
    ejecutar_prueba(6, "Creacion de servicio con precio invalido", probar_servicio_precio_invalido)
    ejecutar_prueba(7, "Creacion de alquiler de equipo valido", probar_alquiler_equipo_valido)
    ejecutar_prueba(8, "Creacion de reserva de sala valida", probar_reserva_sala_valida)
    ejecutar_prueba(9, "Busqueda de servicio existente en catalogo", probar_busqueda_servicio_existente)
    ejecutar_prueba(10, "Busqueda de servicio inexistente en catalogo", probar_busqueda_servicio_inexistente)
    ejecutar_prueba(11, "Creacion de orden valida y calculo de total", probar_orden_valida)
    ejecutar_prueba(12, "Intento de agregar servicio vacio a una orden", probar_servicio_vacio_en_orden)
    ejecutar_prueba(13, "Calculo con impuesto y descuento", probar_calculo_con_impuesto_descuento)

    print("\n============================================================")
    print("SIMULACION FINALIZADA")
    print("El sistema ejecuto operaciones correctas y errores controlados.")
    print("============================================================")


# se ejecuta la funcion principal cuando el archivo se corre directamente
if __name__ == "__main__":
    main()