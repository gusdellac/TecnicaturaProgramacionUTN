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
cursor = conexion.cursor()  # metodo cursor retorna un objeto que nos permite el acceso a datos de una db
query = 'SELECT * FROM persona'  # guardamos la consulta sql como string en variable query
cursor.execute(query)  # metodo execute del objeto cursor nos permite realizar la consulta sql
registros = cursor.fetchall()  # metodo fetchall retorna un array con los datos devueltos por la consulta anterior
print(registros)

cursor.close()
conexion.close()