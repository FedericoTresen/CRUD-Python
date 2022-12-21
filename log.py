import datetime
import os


class Log:
    def imprimir(self, accion, apellido, nombre, dni):
        "crea un .txt que registra con fecha y hora las acciones realizadas por los usuarios de la app"

        archivo = open("archivolog.txt", "a")
        ahora = datetime.datetime.now()
        ahora = ahora.strftime(("%d/%m/%Y %H:%M:%S"))
        ahora = str(ahora)

        if accion == "alta":
            archivo.write(
                f"{ahora} ALTA de registro: APELLIDO: {apellido} NOMBRE: {nombre} DNI: {dni} \n"
            )
        elif accion == "baja":
            archivo.write(
                f"{ahora} BAJA de registro: APELLIDO: {apellido} NOMBRE: {nombre} DNI: {dni} \n"
            )
        elif accion == "modificar":
            archivo.write(
                f"{ahora} MODIFICACION del registro: APELLIDO: {apellido} NOMBRE: {nombre} DNI: {dni} \n"
            )
        elif accion == "prender server":
            archivo.write(ahora + " SE HA PRENDIDO EL SERVIDOR \n")

        elif accion == "apagar server":
            archivo.write(ahora + " SE HA APAGADO EL SERVIDOR \n")

        elif accion == "conexion server":
            archivo.write(ahora + " SE ESTABLECE CONEXION CON EL SERVIDOR \n")

        else:
            pass

        archivo.close()


objetolog = Log()
