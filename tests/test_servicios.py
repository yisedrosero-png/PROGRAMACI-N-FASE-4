# se importan las clases de servicios especificos para validar sus calculos
from models.Services import Consulting, EquipmentRental

# funcion para realizar la prueba unitaria de los costos de servicios 
def probar_servicios():
    print(" Probando calculo de costos de servicios ")
    try:
        # probamos una consultoria (ejemplo: 2 horas)
        servicio1 = Consulting(id_servicio="S-01", nombre="Asesoría Java", precio_base=50)
        print(f" {servicio1.nombre} | Costo total: {servicio1.calcular_costo(horas=2)}")
        
        # probamos alquiler de equipo (ejemplo: 3 dias)
        servicio2 = EquipmentRental(id_servicio="S-02", nombre="Laptop Pro", precio_base=30)
        print(f" {servicio2.nombre} | Costo total: {servicio2.calcular_costo(dias=3)}")
    except Exception as e:
        print(f" Error en servicios: {e}")

if __name__ == "__main__":
    probar_servicios()