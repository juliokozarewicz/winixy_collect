from configs import *
import socket

class Serverconex:
    """
    Faz nconexão com o servidor de dados da 
    bolsa de valores.
    """
    
    def __init__(self):
        self.host = HOST
        self.port = PORT

    def server_conex(self):
        self.socket_cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_cnx.settimeout(1)
        self.socket_cnx.connect((self.host, self.port))

    def rec_data(self, env_paramet):
        self.env_server = env_paramet
        self.socket_cnx.sendall(str.encode(self.env_server))
        rec_data_server = self.socket_cnx.recv(10000)

        if len(rec_data_server) > 10000 or len(rec_data_server) < 25 :
            return

        return rec_data_server

