import logging as log  # importamos paquete logging y renombramos con alias log

# docs.python.org/3/howto/logging.html
# llamamos una configuracion basica

# configuracion del log
log.basicConfig(level=log.INFO,
                format="%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt="%I:%M:%S %p",
                handlers=[
                    log.FileHandler("capa_datos.log"),
                    log.StreamHandler()
                ])

# test de los niveles del log
if __name__ == "__main__":
    log.debug("Mensaje a nivel debug")
    log.info("Mensaje a nivel info")
    log.warning("Mensaje a nivel warning")
    log.error("Mensaje a nivel error")
    log.critical("Mensaje a nivel critical")
