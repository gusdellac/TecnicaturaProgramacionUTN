import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='2014gustavo',
    host='localhost',
    port='5432',
    database='test_bd'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            query = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ("Juan Carlos", "Roldan", "rcarlos@mail.com", 2),
                ("Romina", "Ayala", "ayalar@mail.com", 5)
            )  # tupla de tuplas
            cursor.executemany(query, valores)
            registros_modificados = cursor.rowcount
            print(f"Los registros modificados son: {registros_modificados}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()