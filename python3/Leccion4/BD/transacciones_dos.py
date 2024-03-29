import psycopg2 as bd  # importamos psycopg2 y agregamos un alias bd

conexion = bd.connect(
    user='postgres',
    password='2014gustavo',
    host='localhost',
    port='5432',
    database='test_bd'
)

try:
    # conexion.autocommit = False  # evitamos el autoguardado
    cursor = conexion.cursor()
    query = "INSERT INTO persona(nombre, apellido,email) VALUES (%s, %s, %s)"
    valores = ("Carlos", "Robertinho21321313", "clara@mail.com")
    cursor.execute(query, valores)

    query = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    valores = ("Juan", "Juarez", "jcjuarez@mail.com", 5)
    cursor.execute(query, valores)

    conexion.commit()  # guardamos cambios en la bd
    print("Termina la transaccion")
except Exception as e:
    conexion.rollback()  # si ocurre algun error no se guarda nada en la bd
    print(f"Ocurrio un error: {e} , se realizo rollback")
finally:
    conexion.close()