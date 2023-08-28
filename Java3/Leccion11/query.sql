-- Comenzamos con CRUD
-- Listar los estudiantes (read)
SELECT * FROM estudiantes2022;
-- Insertar estudiante (create)
INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES ("Juan","Perez","2615465466","juan@mail.com");
-- Modificar estudiante (update)
UPDATE estudiantes2022 SET nombre="Juan Carlos", apellido="Garcia" WHERE idestudiantes2022=1;
-- Eliminar estudiante (delete)
DELETE FROM estudiantes2022 WHERE idestudiantes2022=1;
ALTER TABLE estudiantes2022 AUTO_INCREMENT = 1;
