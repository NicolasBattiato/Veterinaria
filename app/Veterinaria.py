from app.Cliente import Cliente
from app.Mascota import Mascota


class Veterinaria:
    def __init__(self, nombre, clientes):
        self._nombre = nombre
        self._clientes = list(clientes)
        self._cliente = {}

    def registrarCliente(self, nombre, apellido, dni):
        self._cliente = {
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
            "Mascotas": []
        }
        self._clientes.append(self._cliente)

        print(f"""Cliente: 
                {self._cliente["Nombre"]}
                {self._cliente["Apellido"]}
                {self._cliente["DNI"]} 
                Cliente Registrado Correctamente...""")

    def agregarMascota(self, dni, Mascota):
        clienteBusqueda = False
        for cliente in self._clientes:
            if cliente["DNI"] == dni:
                mascota = {
                    "Nombre": Mascota.nombre,
                    "Tipo": Mascota.tipo,
                    "Raza": Mascota.raza
                }
                cliente["Mascotas"].append(mascota)
                clienteBusqueda = True
                print(cliente)
                print("Mascota Agregada con exito...")
                print("-------------------------------------")

        if not clienteBusqueda:
            print("Cliente no encontrado")

    def listarClientes(self):
        if not self._clientes:
            print("No se encontraron clientes registrados...")
        else:
            print("LISTADO DE CLIENTES")
            for cliente in self._clientes:
                print("-------------------------------------")
                print(
                    f"-Nombre cliente: {cliente["Nombre"]} | -Apellido: {cliente["Apellido"]} | -Dni: {cliente["DNI"]}")
                n = 1
                for mascota in cliente["Mascotas"]:
                    print(f"""
                Mascota {n}: """)
                    print(f"""
                    Nombre: {mascota["Nombre"]} | Tipo: {mascota["Tipo"]} | Raza: {mascota["Raza"]}""")
                    print("\n")
                    n += 1


if __name__ == "__main__":
    veterinaria = Veterinaria("Olmo", [])
    veterinaria.registrarCliente("Nicolas", "Batti", 2)
    veterinaria.registrarCliente("Gaston", "Batti", 45067457)
    mascota1 = Mascota("Abril", "Perro", "Caniche")
    mascota2 = Mascota("Uma", "Perro", "Caniche")
    veterinaria.agregarMascota(2, mascota1)
    veterinaria.agregarMascota(2, mascota2)
    veterinaria.listarClientes()
    print("\n")
    print(veterinaria)
