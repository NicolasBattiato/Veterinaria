
from ClientesDAO import ClientesDAO
from Cliente import Cliente
from Conexion import Conexion

if __name__ == "__main__":
    cliente1 = Cliente(nombre="Nicolas", apellido="Battiato", dni=45065534)
    clienteIngresada = ClientesDAO.insertarCliente(cliente1)
    print(f"Cliente insertado: {clienteIngresada}")
