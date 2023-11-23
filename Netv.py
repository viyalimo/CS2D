import socket
import pickle

class Network:
    def __init__(self):
        self.host = '192.168.0.104'
        self.port = 5555
        self.server = (self.host, self.port)
        self.s_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.Max_size = 50
        self.p = self.connect()
        self.players = 0
        self.log = []

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
