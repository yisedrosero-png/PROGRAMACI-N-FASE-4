# se iporta la clase base EntidadBase y las clases abstractas ABC y abstractmethod para definir la estructura de las clase customer
from models.Entidad_base import EntidadBase

# se define la clase hija que hereda de EntidadBase, con un atributo adicional customer
class Customer(EntidadBase):
    def __init__(self, id_system, name, email, phone, address):
        super().__init__(id_system)
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
# se define un método para obtener la información del cliente, que devuelve una cadena con los detalles del cliente
    def get_info(self):
        return f"Customer ID: {self.id_system}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"
