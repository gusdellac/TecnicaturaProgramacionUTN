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
            query = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input("Digite el número de registro a eliminar: ")
            valores = (entrada,)  # tupla
            cursor.execute(query, valores)
            registros_eliminados = cursor.rowcount
            print(f"Los registros eliminados son: {registros_eliminados}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()