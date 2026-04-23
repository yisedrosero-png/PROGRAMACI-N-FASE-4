# se define un sistema de gestión de pedidos con clases para clientes, productos y pedidos, utilizando herencia para compartir un atributo común id_system. Cada clase tiene atributos específicos y métodos para realizar operaciones relacionadas con su función en el sistema.
from abc import ABC, abstractmethod

# se define la clase base para las entidades del sistema, con un atributo común id_system
class EntidadBase(ABC):
    def __init__(self, id_system):
        self.id_system = id_system 

# se define un método abstracto para obtener información de la entidad, que debe ser implementado por las clases hijas
    @abstractmethod
    def get_info(self):
        pass