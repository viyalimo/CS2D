import pygamefrom Character import Water_animclass Map:    def __init__(self, num_map):        self.color = ('red', "blue", 'green')        self.num_map = num_map        self.width = None        self.height = None        self.tile_size = 45        self.imbg1 = pygame.image.load('images/oh shit.jpg').convert_alpha()        self.imbg1 = pygame.transform.scale(self.imbg1, [self.tile_size, self.tile_size])        self.imbg2 = pygame.image.load('images/границы карты.png').convert_alpha()        self.imbg2 = pygame.transform.scale(self.imbg2, [self.tile_size, self.tile_size])        self.imbg3 = pygame.image.load('images/обычная трава.png').convert_alpha()        self.imbg3 = pygame.transform.scale(self.imbg3, [self.tile_size, self.tile_size])        self.imbg4 = pygame.image.load('images/ground.jpg').convert_alpha()        self.imbg4 = pygame.transform.scale(self.imbg4, [self.tile_size, self.tile_size])        self.imbg5 = pygame.image.load('images/камень.png').convert_alpha()        self.imbg5 = pygame.transform.scale(self.imbg5, [self.tile_size, self.tile_size])        self.imbg6 = pygame.image.load('images/мост.png').convert_alpha()        self.imbg6 = pygame.transform.scale(self.imbg6, [self.tile_size, self.tile_size])        self.imbgE = pygame.image.load('most/E_мост.png').convert_alpha()        self.imbgN = pygame.image.load('most/E_мост.png').convert_alpha()        self.imbgNE = pygame.image.load('most/E_мост.png').convert_alpha()        self.imbgNW = pygame.image.load('most/E_мост.png').convert_alpha()        self.imbgS = pygame.image.load('most/E_мост.png').convert_alpha()        self.imbgSE = pygame.image.load('most/E_мост.png').convert_alpha()        self.imbgSW = pygame.image.load('most/E_мост.png').convert_alpha()        self.imbgW = pygame.image.load('most/E_мост.png').convert_alpha()        self.obstacles = []  # Список для хранения объектов препятствий        self.player_x = 0        self.player_y = 0        self.player_weight = 0        self.player_height = 0        self.obstac = []        self.speed = 15        self.Direct = "L"        self.player_Direct = "L"        self.player_rect = pygame.Rect(self.player_x, self.player_y, self.player_weight, self.player_height)        self.sum_obstac = self.L_obst()        self.water_anim = 0        # Добавьте здесь код для загрузки карты, тайлов и других параметров.    def L_obst(self):        smo = 0        world = self.View_world(self.num_map)[0]        for i in range(len(world)):            for j in range(len(world[i])):                if world[i][j] == "O":                    smo += 1        return smo    def View_world(self, view_world):        if view_world == 1:            world = ["TTTTTTTTTTTTTTTTTTTTTTTTTW     TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBOOOOOOOOBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBMMMMMMMMBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBMMMMMMMMBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBMMMMMMMMBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBOOOOOOOOBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TBBBBBBBBBBBBBBBBBBBBBBBO      OBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT",                     "TTTTTTTTTTTTTTTTTTTTTTTTT      TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"                     ]            self.width = len(world[0]) * self.tile_size            self.height = (len(world)) * self.tile_size            data = (world, self.width, self.height)            return data    def DRAWMAP(self, win, camera):        world = self.View_world(self.num_map)[0]        win.fill('black')        for row in range(len(world)):            for col in range(len(world[row])):                x = col * self.tile_size                y = row * self.tile_size                if world[row][col] == 'B':                    tile_rect = pygame.Rect(x, y, self.tile_size, self.tile_size)                    shifted_tile_rect = camera.apply(tile_rect)  # Применить сдвиг к тайлу                    win.blit(self.imbg1, shifted_tile_rect)                elif world[row][col] == 'T':                    tile_rect = pygame.Rect(x, y, self.tile_size, self.tile_size)                    shifted_tile_rect = camera.apply(tile_rect)  # Применить сдвиг к тайлу                    win.blit(self.imbg2, shifted_tile_rect)                # elif world[row][col] == 'N':                #     tile_rect = pygame.Rect(x, y, tile_Size, tile_Size)                #     shifted_tile_rect = camera.apply(tile_rect)  # Применить сдвиг к тайлу                #     win.blit(self.imbg4, shifted_tile_rect)                elif world[row][col] == 'W':                    tile_rect = pygame.Rect(x, y, self.tile_size, self.tile_size)                    shifted_tile_rect = camera.apply(tile_rect)  # Применить сдвиг к тайлу                    win.blit(Water_anim(self.water_anim), shifted_tile_rect)                    if self.water_anim < 3:                        self.water_anim += 1                    else:                        self.water_anim = 0                elif world[row][col] == 'M':                    tile_rect = pygame.Rect(x, y, self.tile_size, self.tile_size)                    shifted_tile_rect = camera.apply(tile_rect)  # Применить сдвиг к тайлу                    win.blit(self.imbg6, shifted_tile_rect)                elif world[row][col] == "O":                    tile_rect = pygame.Rect(x, y, self.tile_size, self.tile_size)                    if len(self.obstac) < self.sum_obstac:                        self.obstac.append((x, y, self.tile_size))                    shifted_tile_rect = camera.apply(tile_rect)                    win.blit(self.imbg5, shifted_tile_rect)                else:                    tile_rect = pygame.Rect(x, y, self.tile_size, self.tile_size)                    # pygame.draw.rect(win, 'blue', camera.apply(pygame.Rect(x, y, self.tile_size, self.tile_size)))                    shifted_tile_rect = camera.apply(tile_rect)        return win    def H_W(self):        data = (self.View_world(self.num_map)[1], self.View_world(self.num_map)[2])        return data    def get_player(self, player):        self.player_x = player.x        self.player_y = player.y        self.player_weight = player.player_weight        self.player_height = player.player_height        self.player_Direct = player.Direction