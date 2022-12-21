"""Controlador.py"""

from tkinter import Tk
import observador
import vista

__author__ = "Tresen Federico"
__maintainer__ = "Tresen Federico"
__email__ = "fede-vl@hotmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"


class controller:
    def __init__(self, root):

        """Launcher de la aplicación"""

        self.root = root
        self.objeto2 = vista.ventana(self.root)
        self.el_observador = observador.ConcreteObserverA(self.objeto2.objeto1)


if __name__ == "__main__":
    root = Tk()

    objeto3 = controller(root)

    root.mainloop()
