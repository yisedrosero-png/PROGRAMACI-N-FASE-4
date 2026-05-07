# se importan las clases de servicios especificos para validar sus calculos   
from models.Services import Consulting, EquipmentRental
from utils.gestor_logs import log_error_message
from utils.validadores import validate_range

# funcion para realizar la prueba unitaria de los costos de servicios 
def probar_servicios():
    print("\n[TEST] Services Cost Calculation")
    
    try:
       # probamos una consultoria (ejemplo: 2 horas)
        s1 = Consulting("S-01", "Java Consulting", 50)
        print(f"{s1.nombre} | Total Cost (2h): ${s1.calculate_cost(horas=2)}")

        # probamos alquiler de equipo (ejemplo: 3 dias)
        s2 = EquipmentRental("S-02", "Laptop Pro", 30)
        print(f"{s2.nombre} | Total Cost (3 days): ${s2.calculate_cost(dias=3)}")

        # Sobrecarga, Aplicando parametro opcional (Descuento)
        # Demostramos la capacidad del método de recibir argumentos extra (**kwargs)
        print(f"{s1.nombre} | Discounted Cost: ${s1.calculate_cost(horas=2, discount=10)}")

        # Prueba de Error - Precio base negativo
        validate_range(s1.precio_base, min_val=0, field_name="Service Price")
        raise ValueError("Negative price detected in service")

    except Exception as e:
        print(f"Critical: {e}")
        log_error_message(f"Service Calculation Error: {e}")

if __name__ == "__main__":
    probar_servicios()