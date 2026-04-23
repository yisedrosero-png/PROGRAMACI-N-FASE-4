# se importa la clase base EntidadBase para definir la estructura de la clase Order
from models.Entidad_base import EntidadBase

# se define la clase hija que hereda de EntidadBase, con un atributo adicional customer_id y una lista de servicios incluidos en el pedido
class Order(EntidadBase):
    def __init__(self, id_system, customer_id):
        super().__init__(id_system)
        self.customer_id = customer_id # se define un atributo para almacenar el id del cliente que realiza el pedido
        self.service_list = [] # se define un atributo para almacenar la lista de servicios incluidos en el pedido, inicialmente vacía
    # se define un método para calcular el total del pedido sumando el precio de cada servicio en la lista
    def calculate_total(self):
        total = 0
        for service in self.service_list:
            total += service.calculate_cost()
        return total
    def add_service(self, service):
        self.service_list.append(service) # se define un método para agregar un servicio a la lista de servicios incluidos en el pedido, inicialmente vacía

    # se define un método para obtener la información del pedido, que devuelve una cadena con los detalles del pedido, incluyendo el total calculado
    def get_info(self):
         return f"Order ID: {self.id_system}, Customer ID: {self.customer_id}, Total: ${self.calculate_total()}"