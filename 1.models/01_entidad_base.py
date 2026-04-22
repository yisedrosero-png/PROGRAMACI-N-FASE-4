
# se define la clase base para las entidades del sistema, con un atributo común id_system
class EntidadBase:
    def __init__(self, id_system):
        self.id_system = id_system

# se define la clase hija que hereda de EntidadBase, con un atributo adicional customer
class Customer(EntidadBase):
    def __init__(self, id_system, name, email, phone):
        super().__init__(id_system)
        self.name = name
        self.email = email
        self.phone = phone