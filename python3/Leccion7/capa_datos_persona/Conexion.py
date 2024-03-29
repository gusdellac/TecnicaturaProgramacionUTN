# import psycopg2 as bd
from psycopg2 import pool  # importamos modulo pool del paquete psycopg2
from logger_base import log  # importamos log del archivo logger_base
import sys  # importamos modulo sys
# psycopg2 as db -- se puede realizar la importacion de modulos sin usar import

class Conexion:
    # atributos de clase
    _DATABASE = "test_bd"
    _USERNAME = "postgres"
    _PASSWORD = "2014gustavo"
    _DB_PORT = "5432"
    _HOST = "localhost"
    _conexion = None
    _cursor = None
    _MIN_CON = 1  # minimo de conexiones del pool
    _MAX_CON = 5  # maximo de conexiones del pool
    _pool = None  # inicializamos el pool por defecto vacío (None)


    # metodo de clase para obtener una conexion del pool
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()  # metodo getconn() retorna un objeto de conexion al pool
        log.debug(f"Conexion obtenida del pool: {conexion}")
        return conexion

        # if cls._conexion is None:
        #     try:
        #         cls._conexion = bd.connect(host=cls._HOST,
        #                                    user=cls._USERNAME,
        #                                    password=cls._PASSWORD,
        #                                    port=cls._DB_PORT,
        #                                    database=cls._DATABASE)
        #         log.debug(f"Conexion Exitosa: {cls._conexion}")
        #         return cls._conexion
        #     except Exception as e:
        #         log.error(f"Ocurrio un error: {e}")
        #         sys.exit()
        # else:
        #     return cls._conexion

    # metodo de clase para obtener el cursor
    @classmethod
    def obtenerCursor(cls):
        pass

        # if cls._cursor is None:
        #     try:
        #         cls._cursor = cls.obtenerConexion().cursor()
        #         log.debug(f"Se abrio correctamente el cursor: {cls._cursor}")
        #         return cls._cursor
        #     except Exception as e:
        #         log.error(f"Ocurrio un error: {e}")
        #         sys.exit()
        # else:
        #     return cls._cursor

    # metodo de clase para obtener el pool de conexiones
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                # del modulo pool llamamos a la clase SimpleConnectionPool, esta clase internamente recibe
                # como argumento la clase AbstractConnectionPool a la cual se le envían como argumentos
                # (minconn, maxconn, *args, **kwargs). Almacenamos la clase en la var _pool, esto nos habilita
                # a utilizar sus metodos
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f"Creacion de pool de conexiones exitosa {cls._pool}")
                return cls._pool  # retornamos el pool
            except Exception as e:
                log.error(f"Ocurrio un error al obtener el pool de conexiones: {e}")
                sys.exit()
        else:
            return cls._pool  # si el pool de conexiones ya fue inicializado lo retornamos

    # metodo de clase para liberar una conexion del pool
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)  # con el metodo putconn() devolvemos el objeto que dejo de ser utilizado
        # por el cliente al pool de conexiones
        log.debug(f"Regresamos la conexion del pool: {conexion}")

    # metodo para cerrar todas las conexiones del pool
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()  # metodo closeall() realiza un cierre total de las conexiones

# test pool
if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)

    # conexion2 = Conexion.obtenerConexion()
    # conexion3 = Conexion.obtenerConexion()

    # Conexion.obtenerConexion()
    # Conexion.obtenerCursor()
