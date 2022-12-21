"""DECORADORES QUE INFORMAN DE :

1.    Ingreso de nuevo registro

2.    Eliminación de registro

3.    Actualización de registro"""


def decorador_ingreso_de_registro(funcion):
    def envoltura(*args):
        funcion(*args)
        print("Se ha realizado un alta de registro")

    return envoltura


def decorador_baja_de_registro(funcion):
    def envoltura(*args):
        funcion(*args)
        print("Se ha realizado una baja de registro")

    return envoltura


def decorador_actualizacion_de_registro(funcion):
    def envoltura(*args):
        funcion(*args)
        print("Se han actualizado los registros")

    return envoltura
