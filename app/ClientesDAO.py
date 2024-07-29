from Cliente import Cliente
from CursorPOOL import *
from Conexion import *
from Mascota import Mascota


class ClientesDAO:

    _SELECCIONAR_CLIENTE = "SELECT * FROM clientes ORDER BY id_cliente"
    _SELECCIONAR_MASCOTA = "SELECT * FROM mascotas ORDER BY id_mascota"

    _INSERT_CLIENTE = "INSERT INTO clientes(nombre, apellido, dni) VALUES(%s, %s, %s)"
    _INSERT_MASCOTA = "INSERT INTO mascotas(nombre, tipo, raza, id_cliente) VALUES(%s, %s, %s, %s)"

    _UPDATE_CLIENTE = "UPDATE clientes set nombre=%s, apellido=%s, dni=%s WHERE id_cliente=%s"
    _UPDATE_MASCOTA = "UPDATE mascotas set nombre=%s, tipo=%s, raza=%s WHERE id_mascota=%s"

    _DELETE_CLIENTE = "DELETE FROM clientes WHERE id_cliente=%s"
    _DELETE_MASCOTA = "DELETE FROM mascotas WHERE id_mascota=%s"

    #--------------------CRUD CLIENTE----------------------#
    @classmethod
    def seleccionarCliente(cls):
        with CursorPOOL() as cursor:
            cursor.execute(cls._SELECCIONAR_CLIENTE)
            registros = cursor.fetchall()
            clientesLista = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientesLista.append(cliente)
                return clientesLista

    @classmethod
    def insertarCliente(cls, cliente):
        with CursorPOOL() as cursor:
            valores = (cliente.nombre, cliente.apellido, cliente.dni)
            cursor.execute(cls._INSERT_CLIENTE, valores)
            print(f"Cliente Ingresado: {cliente}")
            return cursor.rowcount

    @classmethod
    def actualizarCliente(cls, cliente):
        with CursorPOOL() as cursor:
            valores = (cliente.nombre, cliente.apellido, cliente.dni, cliente.id_cliente)
            cursor.execute(cls._UPDATE_CLIENTE, valores)
            print(f"Cliente Actualizado: {cliente}")
            return cursor.rowcount

    @classmethod
    def eliminarCliente(cls, cliente):
        with CursorPOOL() as cursor:
            valores = (cliente.id_cliente,)
            cursor.execute(cls._DELETE_CLIENTE, valores)
            print(f"Cliente Eliminado: {cliente}")
            return cursor.rowcount

    #--------------------CRUD CLIENTE----------------------#

    # --------------------CRUD MASCOTA----------------------#
    @classmethod
    def seleccionarMascota(cls):
        with CursorPOOL() as cursor:
            cursor.execute(cls._SELECCIONAR_MASCOTA)
            registros = cursor.fetchall()
            listaMascotas = []
            for registro in registros:
                mascota = Mascota(registro[0], registro[1], registro[2], registro[3], registro[4])
                listaMascotas.append(mascota)
                return listaMascotas

    @classmethod
    def insertarMascota(cls, mascota, cliente):
        with CursorPOOL() as cursor:
            valores = (mascota.nombre, mascota.tipo, mascota.raza, cliente.id_cliente)
            cursor.execute(cls._INSERT_MASCOTA, valores)
            print(f"Mascota Ingresada: {mascota}")
            return cursor.rowcount

    @classmethod
    def actualizarMascota(cls, mascota):
        with CursorPOOL as cursor:
            valores = (mascota.nombre, mascota.tipo, mascota.raza, mascota.id_mascota)
            cursor.execute(cls._UPDATE_MASCOTA, valores)
            print(f"Mascota actualizada: {mascota}")
            return cursor.rowcount

    @classmethod
    def eliminarMascota(cls, mascota):
        with CursorPOOL as cursor:
            valores = (mascota.id_mascota, )
            cursor.execute(cls._DELETE_MASCOTA, valores)
            print(f"Mascota eliminada: {mascota}")
            return cursor.rowcount



if __name__  == "__main__":
    #---------------------------------Prueba Cliente----------------------------------------------
    # INSERT
    #cliente1 = Cliente(nombre="Nicolas", apellido="Battiato", dni=45065534)
    #clientesIngresados = ClientesDAO.insertarCliente(cliente1)
    #print(f"Cliente ingresado: {clientesIngresados}")


    # INSERT
    #cliente2 = Cliente(nombre="Gaston", apellido="Battiato", dni=44661614)
    #clienteIngresado = ClientesDAO.insertarCliente(cliente2)
    #print(f"Cliente ingresado: {clienteIngresado}")

    # DELETE
    #clienteE = Cliente(1)
    #clienteEliminado = ClientesDAO.eliminarCliente(clienteE)
    #print(f"Cliente eliminado: {clienteEliminado}")

    # UPDATE
    #clienteU = Cliente(2, nombre="Nicolas", apellido="Battiato", dni=45065534)
    #clienteAct = ClientesDAO.actualizarCliente(clienteU)
    #print(f"Cliente actualizado: {clienteAct}")

    #------------------------------Prueba Mascota--------------------------------------

    #mascota1 = Mascota(nombre="Abril", tipo="Perro", raza="Caniche")
    #clienteMas1 = Cliente(2)
    #mascotaInsert = ClientesDAO.insertarMascota(mascota1, clienteMas1)
    #print(f"Mascota ingresada: {mascotaInsert} al cliente: {clienteMas1}")

    # SELECT
    clientes = ClientesDAO.seleccionarCliente()
    for cliente in clientes:
        print(f"Clientes encontrados: {cliente}")

    mascotas = ClientesDAO.seleccionarMascota()
    for mascota in mascotas:
        print(f"Mascotas encontradas: {mascota}")




