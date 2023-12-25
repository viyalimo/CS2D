import socket
import pickle
import threading
import logging  # Добавлен импорт модуля logging
import time

from server import Server


class Network:
    def __init__(self, HOST_CL):
        self.port = 5555
        self.max_size_send = 1150
        self.max_client = 4
        self.qplayer = 0
        self.s_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if HOST_CL == "HOST":
            self.host = str(socket.gethostbyname_ex(socket.gethostname())[-1][-1])
            self.server = (self.host, self.port)
            threading.Thread(target=self.start_server, name="thr-server", daemon=True).start()
        elif HOST_CL == "GLOBAL":
            self.host = '217.28.221.98'
            self.server = (self.host, self.port)
        else:
            self.host = str(HOST_CL)
            self.server = (self.host, self.port)
        self.bullets = []

        # Настройка логгирования
        logging.basicConfig(filename='netw.log', level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def start_server(self):
        Server(self.max_client, self.host)

    def connect(self, mapa_x, mapa_y, tile_size, obst_pl, obst_bul):
        try:
            self.s_c.connect(self.server)
            self.s_c.send(pickle.dumps(('CONNECT', mapa_x, mapa_y, tile_size, obst_pl, [])))
            logging.info('Успешное подключение к серверу')
            start_data = pickle.loads(self.s_c.recv(self.max_size_send))
            self.qplayer = start_data[2]
            p2 = start_data[1][0]
            p3 = start_data[1][1]
            p4 = start_data[1][2]
            time.sleep(0.5)
            return start_data[0], p2, p3, p4
        except Exception as e:
            print(f'Exception Connect: {e}')

    def Send(self, player, bul: list):
        try:
            self.s_c.send(pickle.dumps((player.x, player.y, player.Direction, player.anim, bul)))
            pos = pickle.loads(self.s_c.recv(self.max_size_send))
            true_pos = [pos[0][0][0], pos[0][0][1], pos[0][0][2], pos[0][0][3]]
            HP = pos[0][2]
            bull_shop = pos[0][3]
            self.qplayer = pos[2]
            if self.qplayer == 1:
                return None, true_pos, pos[3], HP, bull_shop
            elif self.qplayer == 2:
                return pos[1], true_pos, pos[3], HP, bull_shop
            elif self.qplayer == 3:
                return pos[1], true_pos, pos[3], HP, bull_shop
            else:
                return pos[1], true_pos, pos[3], HP, bull_shop
        except Exception as e:
            logging.error(f'Ошибка при отправке данных: {e}')

    def Disconect(self):
        try:
            self.s_c.send(pickle.dumps('Disconect'))
        except Exception as e:
            logging.error(f'Ошибка при отключении: {e}')
