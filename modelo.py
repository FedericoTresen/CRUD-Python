"""Modelo.py"""

import re
from tkinter import messagebox
from peewee import *
from decoradores import *
from observador import Sujeto
from log import objetolog

# ##############################################
# FUNCIONES PARA ASIGNAR A LOS BOTONES
# ##############################################

db = SqliteDatabase("obra_social.db")


class BaseModel(Model):
    class Meta:
        database = db


class Afiliados(BaseModel):
    """Clase afiliados: determina los campos que van a formar la tabla Afiliados.
    -Apellido
    -Nombre
    -Documento"""

    apellido = CharField()
    nombre = CharField()
    documento = CharField(unique=True)


db.connect()
db.create_tables([Afiliados])


class CRUD(Sujeto):
    """Clase de altas, bajas, modificaciones y consultas."""

    def __init__(
        self,
    ):
        pass

    @decorador_ingreso_de_registro
    def alta(self, apellido, nombre, documento, tree):
        """Metodo que da un alta de registro.
        Parametro1: Apellido
        Parametro2: Nombre
        Parametro3: Documento"""
        alfa = "[A-Za-z]"
        numericos = "[0-9]"
        try:
            if (
                (re.search(alfa, apellido.get()) is not None)
                and (re.search(alfa, nombre.get()) is not None)
                and (re.search(numericos, documento.get()) is not None)
            ):

                afiliado = Afiliados()
                afiliado.apellido = apellido.get()
                afiliado.nombre = nombre.get()
                afiliado.documento = documento.get()
                afiliado.save()

                messagebox.showinfo("ALTA", "Afiliado dado de alta exitosamente!")
                self.actualizar_treeview(tree)
                # NOTIFICAR---------------------------------------------------
                self.notificar(apellido.get(), nombre.get(), documento.get())
                # LOG---------------------------------------------------
                objetolog.imprimir(
                    "alta", apellido.get(), nombre.get(), documento.get()
                )
                # ---------------------------------------------------
                apellido.set("")
                nombre.set("")
                documento.set("")

            else:
                messagebox.showinfo(
                    "ERROR",
                    "datos ingresados no válidos, verifique e intente nuevamente",
                )
        except:
            return False

    @decorador_baja_de_registro
    def borrar(self, tree):
        """Metodo que elimina el registro seleccionado."""

        try:
            if messagebox.askyesno(
                message="¿Desea dar de baja a este afiliado?",
                title="ADVERTENCIA",
            ):

                valor = tree.selection()
                item = tree.item(valor)
                mi_id = item["text"]
                borrar = Afiliados.get(Afiliados.id == mi_id)
                borrar.delete_instance()
                # LOG---------------------------------------------------
                objetolog.imprimir(
                    "baja",
                    (item["values"][0]),
                    (item["values"][1]),
                    (item["values"][2]),
                )
                # --------------------------------------------------
                tree.delete(valor)
                messagebox.showinfo("ELIMINAR", "Afiliado eliminado correctamente!")
            else:
                pass
        except:
            return False

    def modificar(self, apellido, nombre, documento, tree):
        """Metodo que edita un registro seleccionado con doble click reemplazandolo por los parametros colocados en los campos
        Parametro1: Apellido
        Parametro2: Nombre
        Parametro3: Documento"""
        try:
            item_seleccionado = tree.focus()
            valor_id = tree.item(item_seleccionado)
            alfa = "[A-Za-z]"
            numericos = "[0-9]"
            if messagebox.askyesno(
                message="¿Desea editar datos del afiliado?",
                title="ADVERTENCIA",
            ):
                if (
                    (re.search(alfa, apellido.get()) is not None)
                    and (re.search(alfa, nombre.get()) is not None)
                    and (re.search(numericos, documento.get()) is not None)
                ):
                    item_seleccionado = tree.focus()
                    valor_id = tree.item(item_seleccionado)
                    # LOG---------------------------------------------------
                    objetolog.imprimir(
                        "modificar",
                        (valor_id["values"][0]),
                        (valor_id["values"][1]),
                        (valor_id["values"][2]),
                    )
                    # ------------------------------------------------------
                    modificar = Afiliados.update(
                        apellido=apellido.get(),
                        nombre=nombre.get(),
                        documento=documento.get(),
                    ).where(Afiliados.id == valor_id["text"])
                    modificar.execute()
                    apellido.set("")
                    nombre.set("")
                    documento.set("")
                    self.actualizar_treeview(tree)
                    messagebox.showinfo(
                        "MODIFICACION", "Afiliado modificado exitosamente!"
                    )

                else:
                    messagebox.showinfo(
                        "ERROR",
                        "datos ingresados no válidos, verifique e intente nuevamente",
                    )

            else:
                pass
        except:
            return False

    @decorador_actualizacion_de_registro
    def actualizar_treeview(self, mitreview):
        """Metodo que elimina todos los registros del treeview y los vuelve a imprimir, actualizandolos."""

        try:
            records = mitreview.get_children()
            for element in records:
                mitreview.delete(element)

            for fila in Afiliados.select():
                print(fila)
                mitreview.insert(
                    "",
                    0,
                    text=fila.id,
                    values=(fila.apellido, fila.nombre, fila.documento),
                )
        except:
            return False

    def consultar(self, apellido, nombre, documento, tree):
        """Metodo que permite buscar un Afiliado por cualquiera de sus parametros
        Parametro1: Apellido
        Parametro2: Nombre
        Parametro3: Documento"""
        try:
            data = (apellido.get(), nombre.get(), documento.get())
            records = tree.get_children()
            for element in records:
                tree.delete(element)

            for fila in Afiliados.select():
                if (len(data[0]) == 0) and (len(data[1]) == 0) and (len(data[2]) == 0):
                    tree.insert(
                        "",
                        0,
                        text=fila.id,
                        values=(fila.apellido, fila.nombre, fila.documento),
                    )
                else:
                    pass

                if (len(data[0]) != 0) and (len(data[1]) == 0) and (len(data[2]) == 0):
                    if fila.apellido == data[0]:
                        tree.insert(
                            "",
                            0,
                            text=fila.id,
                            values=(fila.apellido, fila.nombre, fila.documento),
                        )
                    else:
                        pass
                else:
                    pass

                if (len(data[1]) != 0) and (len(data[0]) == 0) and (len(data[2]) == 0):
                    if fila.nombre == data[1]:
                        tree.insert(
                            "",
                            0,
                            text=fila.id,
                            values=(fila.apellido, fila.nombre, fila.documento),
                        )

                    else:
                        pass
                else:
                    pass

                if (len(data[2]) != 0) and (len(data[0]) == 0) and (len(data[1]) == 0):
                    if str(fila.documento) == data[2]:
                        tree.insert(
                            "",
                            0,
                            text=fila.id,
                            values=(fila.apellido, fila.nombre, fila.documento),
                        )
                    else:
                        pass
                else:
                    pass

                if (len(data[0]) != 0) and (len(data[1]) != 0) and (len(data[2]) == 0):
                    if (fila.apellido == data[0]) and (fila.nombre == data[1]):
                        tree.insert(
                            "",
                            0,
                            text=fila.id,
                            values=(fila.apellido, fila.nombre, fila.documento),
                        )
                    else:
                        pass
                else:
                    pass

                if (len(data[0]) != 0) and (len(data[1]) == 0) and (len(data[2]) != 0):
                    if (fila.apellido == data[0]) and (str(fila.documento) == data[2]):
                        tree.insert(
                            "",
                            0,
                            text=fila.id,
                            values=(fila.apellido, fila.nombre, fila.documento),
                        )
                    else:
                        pass
                else:
                    pass

                if (len(data[0]) == 0) and (len(data[1]) != 0) and (len(data[2]) != 0):
                    if (fila.nombre == data[1]) and (str(fila.documento) == data[2]):
                        tree.insert(
                            "",
                            0,
                            text=fila.id,
                            values=(fila.apellido, fila.nombre, fila.documento),
                        )
                    else:
                        pass
                else:
                    pass

                if (len(data[0]) != 0) and (len(data[1]) != 0) and (len(data[2]) != 0):
                    if (
                        (fila.apellido == data[0])
                        and (fila.nombre == data[1])
                        and (str(fila.documento) == data[2])
                    ):
                        tree.insert(
                            "",
                            0,
                            text=fila.id,
                            values=(fila.apellido, fila.nombre, fila.documento),
                        )

                    else:
                        pass
                else:
                    pass
        except:
            return False
