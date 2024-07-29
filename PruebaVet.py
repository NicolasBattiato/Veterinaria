
from ClientesDAO import ClientesDAO
from Cliente import Cliente
from Conexion import Conexion
from Mascota import Mascota
from Veterinaria import Veterinaria

if __name__ == "__main__":

    print("MENU DE OPERACIONES VETERINARIA".center(50, "-"))
    print(f"""
            1. Insertar CLiente
            2. Insertar Mascota al Cliente
            3. Actualizar Cliente
            4. Actualizar Mascota
            5. Eliminar Cliente
            6. Eliminar Mascota
            7. Listar Clientes
            8. Listar Mascota
            9. Salir""")

    opcion = int(input("Ingrese una opcion del menu(0 o mayor a 9 para salir): "))

    while (opcion >= 9 or opcion != 0):
        if opcion == 1:
            nombre = input("Ingrese el Nombre del Cliente: ")
            apellido = input("Ingrese el Apellido del Cliente: ")
            dni = int(input("Ingrese el DNI del Cliente: "))
            cliente1 = Cliente(nombre=nombre, apellido=apellido, dni=dni)
            clientesIngresados = ClientesDAO.insertarCliente(cliente1)
            print(f"Cliente ingresado: {clientesIngresados}")

        elif opcion == 2:
            nombre = input("Ingrese el Nombre de la Mascota: ")
            tipo = input("Ingrese el tipo de la Mascota: ")
            raza = input("Ingrese la raza de la Mascota: ")
            mascota1 = Mascota(nombre=nombre, tipo=tipo, raza=raza)
            clienteMascota = int(input("Ingrese el id del Cliente que adopta la mascota: "))
            clienteMas1 = Cliente(clienteMascota)
            mascotaInsert = ClientesDAO.insertarMascota(mascota1, clienteMas1)
            print(f"Mascota ingresada: {mascotaInsert} al cliente: {clienteMas1}")

        elif opcion == 3:
            clienteMod = int(input("Ingrese el id del Cliente que quiere actualizar: "))
            nombre = input("Ingrese el Nombre del Cliente: ")
            apellido = input("Ingrese el Apellido del Cliente: ")
            dni = int(input("Ingrese el DNI del Cliente: "))
            clienteU = Cliente(clienteMod, nombre=nombre, apellido=apellido, dni=dni)
            clienteAct = ClientesDAO.actualizarCliente(clienteU)
            print(f"Cliente actualizado: {clienteAct}")

        elif opcion == 4:
            mascotaMod = int(input("Ingrese el id de la Mascota que quiere actualizar: "))
            nombre = input("Ingrese el Nombre de la Mascota: ")
            tipo = input("Ingrese el tipo de la Mascota: ")
            raza = input("Ingrese la raza de la Mascota: ")
            mascotaU = Mascota(mascotaMod, nombre=nombre, tipo=tipo, raza=raza)
            mascotaAct = ClientesDAO.actualizarMascota(mascotaU)
            print(f"Mascota actualizada: {mascotaAct}")

        elif opcion == 5:
            clienteEliminar = int(input("Ingrese el id del cliente a eliminar: "))
            clienteE = Cliente(clienteEliminar)
            clienteEliminado = ClientesDAO.eliminarCliente(clienteE)
            print(f"Cliente eliminado: {clienteEliminado}")

        elif opcion == 6:
            mascotaEliminar = int(input("Ingrese el id de la mascota a eliminar: "))
            mascotaE = Mascota(mascotaEliminar)
            mascotaEliminada = ClientesDAO.eliminarMascota(mascotaE)
            print(f"Mascota eliminada: {mascotaEliminada}")

        elif opcion == 7:
            clientes = ClientesDAO.seleccionarCliente()
            for cliente in clientes:
                print(f"Clientes encontrados: {cliente}")


        elif opcion == 8:
            mascotas = ClientesDAO.seleccionarMascota()
            for mascota in mascotas:
                print(f"Mascotas encontradas: {mascota}")

        print("MENU DE OPERACIONES VETERINARIA".center(50, "-"))
        print(f"""
                    1. Insertar CLiente
                    2. Insertar Mascota al Cliente
                    3. Actualizar Cliente
                    4. Actualizar Mascota
                    5. Eliminar Cliente
                    6. Eliminar Mascota
                    7. Listar Clientes
                    8. Listar Mascota
                    9. Salir""")

        opcion = int(input("Ingrese una opcion(0 o <9 para salir): "))

    print("El programa termino...")






