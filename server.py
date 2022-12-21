from pathlib import Path
import subprocess
import threading
from log import objetolog
import os
import sys

theproc = ""


class Server:
    """clase con los metodos para prender y apagar servidor."""

    def __init__(
        self,
    ):
        # PASO 1 - AGREGO RUTA A SERVIDOR
        self.raiz = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.raiz, "src", "servidor", "udp_server_t.py")

    def prender(
        self,
    ):
        print("prender")

    def try_connection(
        self,
    ):

        if theproc != "":
            theproc.kill()
            threading.Thread(
                target=self.lanzar_servidor, args=(True,), daemon=True
            ).start()
        else:
            threading.Thread(
                target=self.lanzar_servidor, args=(True,), daemon=True
            ).start()
        # ==================LOG ==================
        objetolog.imprimir("prender server", "", "", "")
        # ==================   # ==================

    def lanzar_servidor(self, var):

        the_path = self.ruta_server
        if var == True:
            global theproc
            theproc = subprocess.Popen([sys.executable, the_path])
            theproc.communicate()
        else:
            print("")

    # =================== INNIT AND STOP SERVER ======================
    def stop_server(
        self,
    ):

        global theproc
        if theproc != "":
            theproc.kill()
            # ==================LOG ==================
            objetolog.imprimir("apagar server", "", "", "")
            # ==================    ==================
