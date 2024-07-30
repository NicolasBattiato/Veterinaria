from psycopg2 import pool
from psycopg2 import sql
import sys


class Conexion:
    _DATABASE = "Veterinaria_db"
    _USERNAME = "postgres"
    _PASSWORD = "Nico0603"
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN = 1
    _MAX = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN, cls._MAX,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                print(f"Conexion exitosa: {cls._pool}")
                return cls._pool

            except Exception as e:
                print(f"Ocurrio un problema en la conexion del pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        print(f"Conexion exitosa del pool: {conexion}")
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        print(f"se recupero la conexion al pool: {conexion}")

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()

    @classmethod
    def createTable(cls):
        tablas = (
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente SERIAL PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                apellido VARCHAR(255) NOT NULL,
                dni INT NOT NULL
            )        
            """
            ,
            """
            CREATE TABLE IF NOT EXISTS mascotas (
                id_mascota SERIAL PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                tipo VARCHAR(255) NOT NULL,
                raza VARCHAR(255) NOT NULL,
                id_cliente INT,
                FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)                 
            )
            """

        )
        conexion = None
        try:
            conexion = cls.obtenerConexion()
            cursor = conexion.cursor()
            for tabla in tablas:
                cursor.execute(tabla)
            conexion.commit()
            cursor.close()
            print(f"Tablas creadas exitosamente...")
        except Exception as e:
            print(f"Ocurrio un error: {e}...")
        finally:
            if conexion:
                cls.liberarConexion(conexion)


if __name__ == "__main__":
    Conexion.createTable()
