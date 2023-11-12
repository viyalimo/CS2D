import socket
from _thread import *
from player import Player
import pickle

server = str(socket.gethostbyname_ex(socket.gethostname())[-1][-1])  # добавление ID сервера
print(socket.gethostbyname_ex(socket.gethostname())[-1][-1])
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание TCP сокета
currentPlayer = 0
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)  # ожидание подключения
print("Waiting for a connection, Server Started")

players = [Player(750, 400, "L"), Player(850, 400, "L")]


def threaded_client(con, player):
    print(player, "номер игрока")
    con.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(con.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending: ", reply)

            con.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    con.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))  # выделение потока
    currentPlayer += 1
