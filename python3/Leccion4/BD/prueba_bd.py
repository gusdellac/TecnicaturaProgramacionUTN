# instalar modulos para conectar con postgresql , comando : pip install psycopg2
import psycopg2  # importamos modulo psycopg2

# creamos la conexion con la db
conexion = psycopg2.connect(
    user='postgres',
    password='2014gustavo',
    host='localhost',
    port='5432',
    database='test_bd'
)
# print(conexion)
# cursor = conexion.cursor()  # metodo cursor retorna un objeto que nos permite el acceso a datos de una db

# conexion a bd usando with
try:
    with conexion:
        with conexion.cursor() as cursor:
            query = 'SELECT * FROM persona WHERE id_persona = %s'  # guardamos la
            # consulta sql como string en variable query // %s placeholder , enviamos un parametro en la query
            id_persona = input("Digite un numero para el id_persona: ")
            cursor.execute(query, (id_persona,))  # metodo execute del objeto // pasamos la query y el parametro dentro
            # de una tupla

            # cursor nos permite realizar la consulta sql
            # registros = cursor.fetchall()  # metodo fetchall retorna un array con los datos devueltos por la consulta
            registros = cursor.fetchone()  # retorna una tupla
            # anterior
            print(registros)
            # al utilizar with no es necesario cerrar el cursor ( cursor.close() )
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()  # cerramos conexion a bd