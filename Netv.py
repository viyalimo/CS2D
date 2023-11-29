import socket
import pickle
import threading
from Serv import Server

class Network:
    def __init__(self, host_con):
        self.port = 5555
        self.s_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.Max_size = 50
        self.p = self.connect()
        self.players = 0
        self.log = []
        self.run_server = None

        if host_con == "HOST":
            self.host = str(socket.gethostbyname_ex(socket.gethostname())[-1][-1])
            self.server = (self.host, self.port)
            self.start_server = threading.Thread(target=self.start_server).start()
            self.start_game()
            print('sheet')
        else:
            self.host = str(input("Введите адрес сервера: "))
            self.server = (self.host, self.port)
            print("вы присоеденились к серверу")
            self.start_game()

    def start_server(self):
        self.run_server = Server(10, self.host)
        self.run_server.start_new_thread()

    def start_game(self):
        print('start_game')
        self.p = self.connect()

    def connect(self):
        try:
            self.s_c.connect(self.server)
            self.s_c.sendto(pickle.dumps(('name', f'{input("введите ваше имя=> ")}')), self.server)
            msg = self.s_c.recv(self.Max_size)
            self.players = pickle.loads(msg)[2]
            return pickle.loads(msg)[0], pickle.loads(msg)[1]
        except:
            pass

    def getP(self):
        return self.p

    def update(self, player):
        self.s_c.connect(self.server)
        self.s_c.sendto(pickle.dumps((f'pos_update', (player.x, player.y, player.Direction))), self.server)
        msg = self.s_c.recv(self.Max_size)
        print(pickle.loads(msg), "updateeeeeeeeeeeeeeeeeeeeeeee")
        if pickle.loads(msg)[1]:
            self.log.append(pickle.loads(msg)[1])
        self.players = pickle.loads(msg)[0]
        b = pickle.loads(msg)[1]
        if not b:
            return self.players, self.log[len(self.log)-1]
        else:
            return self.players, b




    # def listen(self, s: socket.socket):
    #     while True:
    #         try:
    #             msg = s.recv(self.Max_size)
    #             if not msg:
    #                 break
    #             else:
    #                 print(pickle.loads(msg).split()[0])
    #                 return pickle.loads(msg).split()[1]
    #         except Exception as e:
    #             print(f'Error: {e}')
    #             break

    # def connect(self, player):
    #     self.s_c.connect((self.host, self.port))
    #
    #     threading.Thread(target=self.listen, args=(self.s_c,), daemon=True).start()
    #     self.s_c.send(pickle.dumps(f'__join {input("введите ваше имя=> ")}'))
    #
    #     try:
    #         while True:
    #             msg = input(f'you: ')
    #             self.s_c.send(pickle.dumps(msg))  # отправка сообщения
    #     except KeyboardInterrupt:
    #         pass  # Обработка прерывания (Ctrl+C)
    #
    #     finally:
    #         self.s_c.close()  # Закрытие сокета при выходе из цикла
