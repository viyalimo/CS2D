import socket
import pickle
import threading
from server import Server


class Network:
    def __init__(self, HOST_CL):
        self.port = 5555
        self.max_size = 2000
        self.max_client = 10
        self.qplayer = 0
        self.s_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if HOST_CL == "HOST":
            self.host = str(socket.gethostbyname_ex(socket.gethostname())[-1][-1])
            self.server = (self.host, self.port)
            thr_serv = threading.Thread(target=self.start_server, name="thr-server", daemon=True)
            thr_serv.start()
        else:
            self.host = str(HOST_CL)
            self.server = (self.host, self.port)

    def start_server(self):
        server = Server(self.max_client, self.host)

    def connect(self):
        #try:
            self.s_c.connect(self.server)
            self.s_c.send(pickle.dumps('CONNECT'))
            print('Вы присоединились к серверу!')
            start_data = pickle.loads(self.s_c.recv(self.max_size))
            self.qplayer = start_data[2]
            if start_data[1] == 'None':
                p2 = None
                #print('None')
            else:
                p2 = start_data[1]
            return start_data[0], p2
        # except Exception as e:
        #     print(f"Exception connect: {e}")

    def Send(self, player):
        # try:
            self.s_c.send(pickle.dumps((player.x, player.y, player.Direction, player.anim)))
            pos = pickle.loads(self.s_c.recv(self.max_size))
            #print(pos, "posssssssssssssssssssss")
            self.qplayer = pos[1]
            if self.qplayer == 1:
                return None
            else:
                return pos[0]
        # except Exception as e:
        #     print(f'Exception send: {e}')
