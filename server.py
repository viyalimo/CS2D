import socketimport threadingimport pickleimport mathimport pygameimport randomclass Bullet:    def __init__(self, x, y, mx, my):        self.pos = (x, y)        self.blid = -1        self.dir = (mx - x, my - y)        length = math.hypot(*self.dir)        if length == 0.0:            self.dir = (0, -1)        else:            self.dir = (self.dir[0] / length, self.dir[1] / length)        self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))        self.speed = 40    def update(self):        self.pos = (self.pos[0] + self.dir[0] * self.speed,                    self.pos[1] + self.dir[1] * self.speed)class Server:    def __init__(self, max_client, host):        self.max_client = max_client        self.host_server = host        self.port = 5555        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        self.max_size_msg_con = 5000        self.max_size_msg_send = 1000        self.Locker = threading.Lock()        self.qplayer = 0        print(f'Server Listen at {self.host_server}:{self.port}')        try:            self.server_sock.bind((self.host_server, self.port))        except Exception as e:            print(f"Exception bind: {e}")        self.server_sock.listen(max_client)        self.player_start_pos = ([45, 45, "L", 0], [45, 2565, 'L', 0], [2715, 2565, "L", 0], [2715, 45, "L", 0])        self.player_data = {}        self.members = []        self.bullets = []        self.qbullets = 0        self.mapa_x = 0        self.mapa_y = 0        self.tile_size = 0        self.bull = []        self.buls = []        self.player_size = [65, 90]        self.obstacle_player = []        self.HP = 6        self.bull_shop = 24        self.obstacle_bul = []        while True:            conn, addr = self.server_sock.accept()            threading.Thread(target=self.Listen, args=(conn, addr)).start()            print(threading.enumerate())    def Listen(self, conn, addr):        try:            while True:                msg = pickle.loads(conn.recv(self.max_size_msg_con))                client_id = addr[1]                if client_id not in self.members:                    self.members.append(client_id)                    self.qplayer = len(self.members)                if msg[0] == 'CONNECT':                    self.connect(msg, conn, client_id)                elif msg == 'Disconect':                    self.Disconnect(conn, client_id)                else:                    self.Sent(msg, conn, client_id)        except Exception as e:            print(f'ERROR LISTEN: {e}')    def Sent(self, msg, conn, client_id):        try:            player_data = []            self.coordinate_True(msg, client_id)            self.bullet(client_id)            for i in self.bullets:                self.bull.append([i.pos, i.angle])            self.collision('bul', client_id)            self.collision('player', client_id)            for member in self.members:                if member == client_id:                    if self.qplayer == 1:                        conn.send(pickle.dumps((self.player_data.get(client_id), 'None', self.qplayer, self.bull)))                        self.bull.clear()                        continue                else:                    if self.qplayer == 2:                        player_data = self.collision('cadr', client_id)                        conn.send(pickle.dumps((self.player_data.get(client_id), player_data, self.qplayer, self.bull)))                        self.bull.clear()                        continue                    else:                        for i in self.members:                            if i == client_id:                                continue                            else:                                player_data = self.collision('cadr', client_id)                        conn.send(pickle.dumps((self.player_data.get(client_id), player_data, self.qplayer, self.bull)))                        self.bull.clear()                        break        except Exception as e:            print(f'ERROR SEND: {e}')    def connect(self, msg, conn, client_id):        try:            print('connect', self.qplayer)            if self.qplayer == 1:                start_pos = self.player_start_pos[0]                conn.send(pickle.dumps((start_pos, [None, None, None], self.qplayer)))                self.player_data[client_id] = start_pos, [], self.HP, self.bull_shop                self.mapa_x = msg[1]                self.mapa_y = msg[2]                self.tile_size = msg[3]                self.obstacle_player = msg[4]                self.obstacle_bul = msg[5]            elif self.qplayer == 2:                start_pos = self.player_start_pos[1]                for member in self.members:                    if member == client_id:                        continue                    else:                        conn.send(pickle.dumps((start_pos, [self.player_data[member][0], None, None], self.qplayer)))                        self.player_data[client_id] = start_pos, [], self.HP, self.bull_shop                        continue            elif self.qplayer == 3:                player_data = []                start_pos = self.player_start_pos[2]                for member in self.members:                    if member == client_id:                        continue                    else:                        player_data.append(self.player_data[member][0])                        continue                conn.send(pickle.dumps((start_pos, [player_data[0], player_data[1], None], self.qplayer)))                self.player_data[client_id] = start_pos, [], self.HP, self.bull_shop            else:                player_data = []                start_pos = self.player_start_pos[3]                for member in self.members:                    if member == client_id:                        continue                    else:                        player_data.append(self.player_data[member][0])                        continue                conn.send(pickle.dumps((start_pos, [player_data[0], player_data[1], player_data[2]], self.qplayer)))                self.player_data[client_id] = start_pos, [], self.HP, self.bull_shop        except Exception as e:            print(f'ERROR CONNECT: {e}')    def Disconnect(self, conn, client_id):        try:            print(client_id, 'покинул игру')            self.members.pop(self.members.index(client_id))            del self.player_data[client_id]            self.qplayer = len(self.members)        except Exception as e:            print(f'ERROR DISCONNECT: {e}')    def coordinate_True(self, msg, client_id):        try:            if self.player_data.get(client_id)[0][0] + 15 == msg[0]:                self.player_data.get(client_id)[0][0] = msg[0]            elif self.player_data.get(client_id)[0][0] - 15 == msg[0]:                self.player_data.get(client_id)[0][0] = msg[0]            elif self.player_data.get(client_id)[0][0] == msg[0]:                self.player_data.get(client_id)[0][0] = msg[0]            else:                if self.player_data.get(client_id)[0][0] < msg[0]:                    self.player_data.get(client_id)[0][0] += 15                else:                    self.player_data.get(client_id)[0][0] -= 15            if self.player_data.get(client_id)[0][1] + 15 == msg[1]:                self.player_data.get(client_id)[0][1] = msg[1]            elif self.player_data.get(client_id)[0][1] - 15 == msg[1]:                self.player_data.get(client_id)[0][1] = msg[1]            elif self.player_data.get(client_id)[0][1] == msg[1]:                self.player_data.get(client_id)[0][1] = msg[1]            else:                if self.player_data.get(client_id)[0][1] < msg[1]:                    self.player_data.get(client_id)[0][1] += 15                else:                    self.player_data.get(client_id)[0][1] -= 15            self.player_data.get(client_id)[0][2] = msg[2]            self.player_data.get(client_id)[0][3] = msg[3]            if len(msg[4]) != 0:                if isinstance(msg[4], str):                    if msg[4] == 'recharge':                        self.player_data[client_id] = (                        self.player_data[client_id][0], self.player_data[client_id][1], self.player_data[client_id][2], self.bull_shop)                    else:                        pass                else:                    self.player_data[client_id] = (self.player_data[client_id][0], self.player_data[client_id][1], self.player_data[client_id][2], self.player_data[client_id][3]-1)                    if self.player_data[client_id][3] > 0:                        for i in msg[4]:                            self.player_data.get(client_id)[1].append(i)                    else:                        pass        except Exception as e:            print(f'ERROR coordinate True: {e}')    def collision(self, inf, client_id):        try:            if inf == 'bul':                obst = self.obstacle_player                for i in obst:                    obst_rect = pygame.Rect(i[0], i[1], i[2], i[3])                    obst_rect.topleft = [i[0], i[1]]                    bul = len(self.bull)                    if bul > 0:                        for b in range(bul):                            if b < bul:                                bul_x = self.bull[b][0][0]                                bul_y = self.bull[b][0][1]                                if obst_rect.collidepoint(bul_x, bul_y):                                    self.bull.pop(b)                                    self.bullets.pop(b)                                    bul -= 1                bul_len = len(self.bull)                for i in range(bul_len):                    if bul_len > 0 and i < bul_len:                        bul_pos = self.bull[i][0]                        if (bul_pos[0] <= self.tile_size or bul_pos[0] >= self.mapa_x - self.tile_size) or (bul_pos[1] <= self.tile_size or bul_pos[1] >= self.mapa_x - self.tile_size):                            if bul_len > 0 and i < bul_len:                                self.bull.pop(i)                                self.bullets.pop(i)                                bul_len -= 1                        if ((bul_pos[0] < self.player_data[client_id][0][0] - 750) or (bul_pos[0] > self.player_data[client_id][0][0] + 750)) or ((bul_pos[1] < self.player_data[client_id][0][1] - 400) or (bul_pos[1] > self.player_data[client_id][0][1] + 400)):                            if bul_len > 0 and i < bul_len:                                self.bull.pop(i)                                bul_len -= 1            if inf == "player":                for i in range(len(self.members)):                    pl_data = self.player_data[self.members[i]][0]                    pl_rect = pygame.Rect(pl_data[0], pl_data[1], self.player_size[0], self.player_size[1])                    pl_rect.topleft = [pl_data[0], pl_data[1]]                    bul = len(self.bull)                    if bul > 0:                        for b in range(bul):                            if b < bul:                                bul_x = self.bull[b][0][0]                                bul_y = self.bull[b][0][1]                                if pl_rect.collidepoint(bul_x, bul_y):                                    self.bull.pop(b)                                    self.bullets.pop(b)                                    bul -= 1                                    if self.player_data[self.members[i]][2] > 0:                                        self.player_data[self.members[i]] = (self.player_data[self.members[i]][0], self.player_data[self.members[i]][1], self.player_data[self.members[i]][2]-1, self.player_data[self.members[i]][3])                                    else:                                        start_pos = ([45, 45, "L", 0], [45, 2565, 'L', 0], [2715, 2565, "L", 0], [2715, 45, "L", 0])                                        n = random.randint(0, 3)                                        self.player_data[self.members[i]] = (start_pos[n], self.player_data[self.members[i]][1], self.HP, self.bull_shop)            if inf == 'cadr':                player_data = []                for member in self.members:                    if member == client_id:                        continue                    else:                        if (((self.player_data[client_id][0][0] + 750 + self.player_size[0]) < self.player_data[member][0][0]) or (self.player_data[client_id][0][0] - 750 > self.player_data[member][0][0])                                or ((self.player_data[client_id][0][1] - 400 - self.player_size[1]) > self.player_data[member][0][1]) or (self.player_data[client_id][0][1] + 400 < self.player_data[member][0][1])):                            continue                        else:                            player_data.append(self.player_data[member][0])                if len(player_data) > 0:                    return player_data                return None        except Exception as e:            print(f'ERROR COLLISION: {e}')    def bullet(self, client_id):        list_1 = []        list_2 = []        list_3 = []        for i in self.members:            if i == client_id:                if len(self.player_data[i][1]) == 0:                    list_1 = []                else:                    bul = Bullet(*self.player_data[i][1][0])                    list_1.append(bul)                    bul = None                if len(list_1) != 0 or len(list_2) != 0:                    list_3 = [list_1 + list_2]                self.player_data[client_id][1].clear()                continue            else:                if len(self.player_data[i][1]) == 0:                    list_2 = []                else:                    bul = Bullet(*self.player_data[i][1][0])                    list_2.append(bul)                    bul = None                if len(list_1) != 0 or len(list_2) != 0:                    list_3 = [list_1 + list_2]                self.player_data[i][1].clear()                continue        for bullets_data in list_3:            self.bullets.extend(bullets_data)        for bullet in self.bullets[:]:            bullet.update()