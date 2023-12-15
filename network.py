import socket
import pickle
import threading
from server import Server


class Network:
    def __init__(self, HOST_CL):
        self.port = 5555
        self.max_size = 5000
        self.max_client = 10
        self.qplayer = 0
        self.s_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if HOST_CL == "HOST":
            self.host = str(socket.gethostbyname_ex(socket.gethostname())[-1][-1])
            self.server = (self.host, self.port)
            threading.Thread(target=self.start_server, name="thr-server", daemon=True).start()
        else:
            self.host = str(HOST_CL)
            self.server = (self.host, self.port)
        self.bullets = []

    def start_server(self):
        server = Server(self.max_client, self.host)

    def connect(self, mapa_x, mapa_y, tile_size):
        try:
            self.s_c.connect(self.server)
            self.s_c.send(pickle.dumps(('CONNECT', mapa_x, mapa_y, tile_size)))
            print('Вы присоединились к серверу!')
            start_data = pickle.loads(self.s_c.recv(self.max_size))
            print(start_data)
            print(start_data)
            self.qplayer = start_data[2]
            if start_data[1] == 'None':
                p2 = None
            else:
                p2 = start_data[1][0]
            return start_data[0], p2
        except Exception as e:
            print(f"Exception connect: {e}")

    def Send(self, player, bul: list):
        try:
            # print(bul, "SEND")

            self.s_c.send(pickle.dumps((player.x, player.y, player.Direction, player.anim, bul)))
            pos = pickle.loads(self.s_c.recv(self.max_size))
            # print(pos, "posssssssssssssssssssss")
            true_pos = [pos[0][0][0], pos[0][0][1], pos[0][0][2], pos[0][0][3]]
            # print(true_pos, 'true_pos')
            self.qplayer = pos[2]
            # print(pos[3], 'pos[0][2]')
            print('bul', pos[3])
            if self.qplayer == 1:
                return None, true_pos, pos[3]
            else:
                return pos[1][0], true_pos, pos[3]
        except Exception as e:
            print(f'Exception send: {e}')

    def Disconect(self):
        try:
            self.s_c.send(pickle.dumps('Disconect'))
        except Exception as e:
            print(f'ERROR: {e}')

