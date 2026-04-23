# se importa la clase base EntidadBase y las clases abstractas ABC y abstractmethod para definir la estructura de las clase Service
from models.Entidad_base import EntidadBase
from abc import ABC, abstractmethod

# se define la clase hija que hereda de EntidadBase, con un atributo adicional service
class Service(EntidadBase, ABC):
    def __init__(self, id_system, price):
        super().__init__(id_system)
        self.price = price
   
    # se define un método bastracto para obtener la informacion
    @abstractmethod
    def calculate_cost(self):
        pass

    #se define un método abstracto para obtener la información
    @abstractmethod
    def get_info(self):
        pass # se define un método para obtener la información del servicio, que devuelve una cadena con los detalles del servicio

# se define la clase hija que hereda de Service, con un atributo adicional hours
class Consulting(Service):
    def __init__(self, id_system, name, price, hours):
        super().__init__(id_system,float(price))
        self.name = name
        self.hours = float(hours)

    # se define un método para calcular el costo del servicio de consultoría, multiplicando el precio por hora por el número de horas, y devuelve el resultado
    def calculate_cost(self):
        return self.price * self.hours

    # se define un método para obtener la información del servicio de consultoría, que devuelve una cadena con los detalles del servicio, incluyendo el costo total calculado
    def get_info(self):
        return f"Consulting Service ID: {self.id_system}, Price per Hour: {self.price}, Hours: {self.hours}, Total Cost: {self.calculate_cost()}"

# se define la clase hija que hereda de Service, con un atributo adicional days    
class EquipmentRental(Service):
    def __init__(self, id_system, name, price_per_day, days):
        super().__init__(id_system, float(price_per_day))
        self.name = name
        self.days = float(days)

    # se define un método para calcular el costo del servicio de alquiler de equipo, multiplicando el precio por día por el número de días, y devuelve el resultado
    def calculate_cost(self):
        return self.price * self.days # se define un método para calcular el costo del servicio de alquiler de equipo, multiplicando el precio por día por el número de días, y devuelve el resultado

    # se define un método para obtener la información del servicio de alquiler de equipo, que devuelve una cadena con los detalles del servicio, incluyendo el costo total calculado
    def get_info(self):
        return f"Equipment Rental ID: {self.id_system}, Name: {self.name}, Price per Day: {self.price}, Days: {self.days}, Total Cost: {self.calculate_cost()}"

# se define la clase hija que hereda de Service, con un atributo adicional hours
class RoomReservation(Service):
    def __init__(self, id_system, name, price_per_hour, hours):
        super().__init__(id_system, float(price_per_hour))
        self.name = name
        self.hours = float(hours)

    # se define un método para calcular el costo del servicio de reserva de habitación, multiplicando el precio por hora por el número de horas, y devuelve el resultado
    def calculate_cost(self):
        return self.price * self.hours # se define un método para calcular el costo del servicio de reserva de habitación, multiplicando el precio por hora por el número de horas, y devuelve el resultado

    # se define un método para obtener la información del servicio de reserva de habitación, que devuelve una cadena con los detalles del servicio, incluyendo el costo total calculado
    def get_info(self):
        return f"Room Reservation ID: {self.id_system}, Name: {self.name}, Price per Hour: {self.price}, Hours: {self.hours}, Total Cost: {self.calculate_cost()}"