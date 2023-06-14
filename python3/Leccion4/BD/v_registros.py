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
            query = 'SELECT * FROM persona WHERE id_persona IN (1, 2, 3)'
            # id_persona = input("Digite un numero para el id_persona: ")
            cursor.execute(query)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()