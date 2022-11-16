from Constantes import MI_CONSTANTE  # importamos la constante
from Constantes import Matematicas as ConstantePI  # importamos la clase Matematicas y le asignamos un nuevo nombre
# para este módulo con palabra reservada as

print(MI_CONSTANTE)
MI_CONSTANTE = "Modificamos el valor de la constante"  # es posible modificar el valor de una constante, por lo que
# las constantes en python existen por convención
print(MI_CONSTANTE)

print(ConstantePI.PI)