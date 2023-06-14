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
            query = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = (
                ("Carlos", "Lara", "clara@mail.com"),
                ("Marcos", "Canto", "mcanto@mail.com"),
                ("Marcelo", "Cuenca", "cuencam@mail.com")
            )  # tupla de tuplas
            cursor.executemany(query, valores)
            # conexion.commit() esto se utiliza para guardar los cambios de la bd, no es necesario cuando utilizamos
            # sintaxis con with
            registros_insertados = cursor.rowcount
            print(f"Los registros insertados son: {registros_insertados}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()