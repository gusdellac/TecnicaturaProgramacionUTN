--Consulta informacion con filtros
SELECT * FROM persona WHERE id_persona in (1, 2, 3);

--Insertamos nuevos datos a la tabla
INSERT INTO persona(nombre, apellido, email) VALUES ('Susana', 'Lara', 'slara@mail.com');

--Consultamos todos los datos de la tabla
SELECT * FROM persona ORDER BY id_persona;

--Modificamos datos de una fila
UPDATE persona SET nombre = 'Ivonne', apellido = 'Esparza', email = 'iesparza@mail.com' WHERE id_persona = 4;
UPDATE persona SET nombre = 'Agus', apellido = 'De Llac', email = 'adellac@mail.com' WHERE id_persona = 5;
UPDATE persona SET nombre = 'Ardui', apellido = 'Glickman', email = 'aglickman@mail.com' WHERE id_persona = 3;

--Eliminamos datos
DELETE FROM persona WHERE id_persona = 4;