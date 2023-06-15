import psycopg2 as bd  # importamos psycopg2 y agregamos un alias bd

conexion = bd.connect(
    user='postgres',
    password='2014gustavo',
    host='localhost',
    port='5432',
    database='test_bd'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            query = "INSERT INTO persona(nombre, apellido,email) VALUES (%s, %s, %s)"
            valores = ("Alex", "Rojas", "arojas@mail.com")
            cursor.execute(query, valores)

            query = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            valores = ("Juan Carlos", "Roldan", "jcroldan@mail.com", 5)
            cursor.execute(query, valores)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
print("Termina la transaccion")