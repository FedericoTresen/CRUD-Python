import socket
import sys
import binascii
from log import objetolog


"""CLIENTE QUE ENVIA UN STRING AL SERVIDOR"""

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ################################################333
mensaje = "Se establece comunicacion con el servidor"
# LOG---------------------------------------------------
objetolog.imprimir("conexion server", "", "", "")
# --------------------------------------------------
sock.sendto(mensaje.encode("UTF-8"), (HOST, PORT))
received = sock.recvfrom(1024)

# ===== ENVIO Y RECEPCIÓN DE DATOS =================

print(received)
# ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================
