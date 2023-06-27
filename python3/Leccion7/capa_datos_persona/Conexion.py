# import psycopg2 as bd
from psycopg2 import pool
from logger_base import log
import sys
# psycopg2 as db -- se puede realizar la importacion de modulos sin usar import

class Conexion:
    _DATABASE = "test_bd"
    _USERNAME = "postgres"
    _PASSWORD = "2014gustavo"
    _DB_PORT = "5432"
    _HOST = "localhost"
    _conexion = None
    _cursor = None
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
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


    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f"Creacion de pool de conexiones exitosa {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un error al obtener el pool de conexiones: {e}")
                sys.exit()
        else:
            return cls._pool

if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()

    # Conexion.obtenerConexion()
    # Conexion.obtenerCursor()
