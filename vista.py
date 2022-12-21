from logging import root
from tkinter import StringVar
from tkinter import Entry
from tkinter import Label
from tkinter import ttk
from tkinter import Tk
from tkinter import Button
from modelo import CRUD
from server import *


class ventana:
    """Ventana de la aplicación"""

    def __init__(self, windows):

        """Campos, botones y confección de la ventana"""

        self.root = windows

        self.root.title("Gestion de beneficiarios")
        self.objeto1 = CRUD()
        self.objeto4 = Server()

        titulo = Label(
            self.root,
            text="Obra social",
            bg="lightblue",
            fg="black",
            height=1,
            width=108,
        )
        titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w")

        apellido = Label(self.root, text="Apellido")
        apellido.grid(row=1, column=0, sticky="w")
        nombre = Label(self.root, text="Nombre")
        nombre.grid(row=1, column=1, sticky="w")
        documento = Label(self.root, text="Nº Documento ")
        documento.grid(row=1, column=2, sticky="w")

        # VARIABLES
        self.a_val, self.b_val, self.c_val = StringVar(), StringVar(), StringVar()
        w_ancho = 30
        mi_id = StringVar()

        entrada_apellido = Entry(self.root, textvariable=self.a_val, width=w_ancho)
        entrada_apellido.grid(row=2, column=0)
        entrada_nombre = Entry(self.root, textvariable=self.b_val, width=w_ancho)
        entrada_nombre.grid(row=2, column=1)
        entrada_dni = Entry(self.root, textvariable=self.c_val, width=w_ancho)
        entrada_dni.grid(row=2, column=2)

        def seleccionar_usando_click(event):

            """metodo para seleccionar un campo con doble click para luego poder modificarlo"""

            item = self.tree.identify("item", event.x, event.y)
            mi_id.set(self.tree.item(item, "text"))
            self.a_val.set(self.tree.item(item, "values")[0])
            self.b_val.set(self.tree.item(item, "values")[1])
            self.c_val.set(self.tree.item(item, "values")[2])

        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=100, minwidth=50, anchor="w")
        self.tree.column("col1", width=220, minwidth=80)
        self.tree.column("col2", width=220, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="Nro afiliado")
        self.tree.heading("col1", text="Apellido")
        self.tree.heading("col2", text="Nombre")
        self.tree.heading("col3", text="Nº Documento")
        self.tree.grid(row=10, column=0, columnspan=5)

        # --------------------------------------------------
        # BOTONES
        # --------------------------------------------------

        self.boton_baja = Button(
            self.root,
            text="    Registrar baja    ",
            command=lambda: self.objeto1.borrar(self.tree),
        )
        self.boton_baja.grid(row=19, column=0)

        boton_modificar = Button(
            self.root,
            text="    Modificar    ",
            command=lambda: self.objeto1.modificar(
                self.a_val, self.b_val, self.c_val, self.tree
            ),
        )
        boton_modificar.grid(row=19, column=1)

        self.boton_alta = Button(
            self.root,
            text="    Alta beneficiario    ",
            command=lambda: self.objeto1.alta(
                self.a_val, self.b_val, self.c_val, self.tree
            ),
        )
        self.boton_alta.grid(row=19, column=2)

        self.boton_consulta = Button(
            self.root,
            text="    Consultar    ",
            command=lambda: self.objeto1.consultar(
                self.a_val, self.b_val, self.c_val, self.tree
            ),
        )
        self.boton_consulta.grid(row=2, column=3)

        self.boton_vertodo = Button(
            self.root,
            text="    Ver todos    ",
            command=lambda: self.objeto1.actualizar_treeview(self.tree),
        )
        self.boton_vertodo.grid(row=19, column=3)

        # BOTONES SERVIDOR
        # -------------------------------------------------------------------------------------
        self.boton_prender = Button(
            self.root,
            text="Prender server",
            command=lambda: self.objeto4.try_connection(),
        )
        self.boton_prender.grid(row=6, column=0)

        self.boton_apagar = Button(
            self.root, text="Apagar server", command=lambda: self.objeto4.stop_server()
        )
        self.boton_apagar.grid(row=6, column=2)
        # -------------------------------------------------------------------------------------

        self.tree.bind("<Double-1>", seleccionar_usando_click)

        self.objeto1.actualizar_treeview(self.tree)
