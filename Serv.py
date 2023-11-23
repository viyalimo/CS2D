import socket
import threading
import pickle
from player import Player


class Server:
    def __init__(self, max_client):
        self.Max_size = 50
        self.s_m = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = str(socket.gethostbyname_ex(socket.gethostname())[-1][-1])  # добавление ID сервера
        self.port = 5555
        self.members = []
        self.log = []
        self.player1 = [750, 400, 'L']
        self.player2 = [850, 400, 'L']
        self.current_player = 0

    def listen(self):
        self.s_m.bind((self.host, self.port))
        print(f'Listening at {self.host}:{self.port}')
        try:
            while True:
                msg, addr = self.s_m.recvfrom(self.Max_size)
                if addr not in self.members:
                    if pickle.loads(msg)[0] == 'name':
                        self.members.append(addr)
                        if not msg:
                            return
                        client_id = addr[1]
                        user_name = pickle.loads(msg)[1]
                        print(f'Client {client_id} joined server, name: {user_name}')
                        self.current_player += 1
                        print(self.current_player, "current_player")
                        self.update_data(self.current_player)
                        if self.current_player == 1:
                            self.s_m.sendto(pickle.dumps((self.player1, self.player2, self.current_player)), addr)
                        if self.current_player == 2:
                            self.s_m.sendto(pickle.dumps((self.player2, self.player1, self.current_player)), addr)
                        # for member in self.members:
                        #     if member == addr:
                        #         continue
                        #     else:
                        #         msg = f'{user_name}, присоединился к игре'
                        #         self.s_m.sendto(pickle.dumps(msg), member)
                else:
                    if pickle.loads(msg)[0] == 'pos_update':
                        b = pickle.loads(msg)[1]
                        for member in self.members:
                            if member == addr:
                                if self.members.index(addr) == 0:
                                    self.player1[0] = b[0]
                                    self.player1[1] = b[1]
                                    self.player1[2] = b[2]
                                    self.s_m.sendto(pickle.dumps((self.current_player, (self.player2[0], self.player2[1], self.player2[2]))), member)
                                    continue
                                if self.members.index(addr) == 1:
                                    self.player2[0] = b[0]
                                    self.player2[1] = b[1]
                                    self.player2[2] = b[2]
                                    self.s_m.sendto(pickle.dumps((self.current_player, (self.player1[0], self.player1[1], self.player1[2]))), member)
                                    continue
                            else:
                                self.s_m.sendto(pickle.dumps((self.current_player, b)), member)
        except Exception as e:
            print(f"Error: {e}")

    def update_data(self, qn_player):
        self.current_player = qn_player


if __name__ == "__main__":
    server = Server(10)
    server.listen()
