
class Cliente:


    def __init__(self,id_cliente=None, nombre= None, apellido= None, dni= None):

        self._id_cliente = id_cliente
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

        #GET Y SET de los atributos

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni




    def __str__(self):
        return f"""
                ID: {self._id_cliente}
                Nombre: {self._nombre}
                Apellido: {self._apellido}
                DNI: {self._dni}"""

if __name__ == "__main__":
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = int(input("Ingrese el dni sin puntos: "))
    cliente1 = Cliente(nombre, apellido, dni)
    print("\n")
    print(cliente1)








