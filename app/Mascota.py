
class Mascota:

    def __init__(self, id_mascota=None, nombre=None, tipo=None, raza=None, id_cliente=None):
        self._id_mascota = id_mascota
        self._nombre = nombre
        self._tipo = tipo
        self._raza = raza
        self._id_cliente = id_cliente

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo
    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, raza):
        self._raza = raza

    def __str__(self):
        return f"""
            ID Mascota: {self._id_mascota}
            ID Cliente: {self._id_cliente}
            Nombre: {self._nombre}
            Tipo: {self._tipo}  
            Raza: {self._raza}
            """





