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
            query = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input("Digite los números de registros a eliminar (separados por coma): ")
            valores = (tuple(entrada.split(",")),)  # tupla de tuplas
            cursor.execute(query, valores)
            registros_eliminados = cursor.rowcount
            print(f"Los registros eliminados son: {registros_eliminados}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()