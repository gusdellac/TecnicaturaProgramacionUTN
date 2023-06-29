import logging

from capa_datos_persona.Conexion import Conexion
from capa_datos_persona.Persona import Persona
from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log


class PersonaDAO:
    """
    DAO : Data Acces Object
    """
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"

    # Definimos los metodos de clase

    # Read
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    # Create
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona insertada: {persona}")
            return cursor.rowcount

    # Update
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona actualizada: {persona}")
            return cursor.rowcount

    # Delete
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute("SELECT * FROM persona WHERE id_persona = %s", valores)
            fila_afectada = cursor.fetchone()
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Persona eliminada: {fila_afectada}")
            return cursor.rowcount


if __name__ == "__main__":

    # Eliminar un registro
    persona1 = Persona(id_persona=21)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas eliminadas: {personas_eliminadas}")

    # Actualizar un registro
    persona1 = Persona(id_persona=19, nombre="Arduizur", apellido="Glickman", email="aglickman@mail.com")
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actualizadas: {personas_actualizadas}")


    # Insertar un registro
    persona1 = Persona(nombre="Roman", apellido="Riquelme", email="rriquelme@mail.com")
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}")

    # Leer objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)