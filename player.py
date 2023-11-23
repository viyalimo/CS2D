import pygame
from Character import Animation1


class Player:
    def __init__(self, x, y, Direction):
        pygame.init()
        # self.connected = True
        self.tile_size = None
        self.map_height = 0
        self.map_weight = 0
        self.player_weight = 0
        self.player_height = 0
        self.Direction = Direction
        self.scr_weight = 0
        self.scr_height = 0
        self.start_pos = (x, y)
        self.x = x
        self.y = y
        self.rect = (x, y)
        self.speed = 15
        self.anim = 0
        self.run = False
        self.anim_surface = None
        self.anim_rect = None

    def draw(self, win):
        ticreite = pygame.time.Clock()
        self.anim_surface = Animation1(self.Direction)[self.anim]
        self.anim_rect = self.anim_surface.get_rect()
        self.player_weight = self.anim_rect.width
        self.player_height = self.anim_rect.height
        self.anim_rect.topleft = self.rect
        win.blit(self.anim_surface, self.start_pos)
        if self.anim < 3 and self.run:
            self.anim += 1
        else:
            if self.anim == 3:
                self.anim = 0
                self.run = False
        ticreite.tick(25)

    def Draw_player2(self, win, player2, camera):
        ticreite = pygame.time.Clock()
        anim_surface = Animation1(player2.Direction)[player2.anim]
        anim_rect = anim_surface.get_rect()
        self.player_weight = anim_rect.width
        self.player_height = anim_rect.height
        anim_rect.topleft = (player2.x, player2.y)
        win.blit(anim_surface, camera.apply(anim_rect))
        if self.anim < 3 and self.run:
            self.anim += 1
        else:
            if self.anim == 3:
                self.anim = 0
                self.run = False
        ticreite.tick(25)

    def move(self, camera, obstacles):
        self.anim_surface = Animation1(self.Direction)[self.anim]
        self.anim_rect = self.anim_surface.get_rect()
        now_press = pygame.key.get_pressed()
        player_dx, player_dy = 0, 0
        camera_dx, camera_dy = 0, 0
        if now_press[pygame.K_LEFT] or now_press[pygame.K_a]:
            self.run = True
            self.Direction = "L"
            player_dx -= self.speed
            camera_dx += self.speed

        if now_press[pygame.K_RIGHT] or now_press[pygame.K_d]:
            self.run = True
            self.Direction = 'R'
            player_dx += self.speed
            camera_dx -= self.speed

        if now_press[pygame.K_UP] or now_press[pygame.K_w]:
            self.run = True
            self.Direction = "U"
            player_dy -= self.speed
            camera_dy += self.speed

        if now_press[pygame.K_DOWN] or now_press[pygame.K_s]:
            self.run = True
            self.Direction = "D"
            player_dy += self.speed
            camera_dy -= self.speed

        self.anim_rect = pygame.Rect(self.x + player_dx, self.y + player_dy, self.anim_rect.width,
                                     self.anim_rect.height)
        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle[2], obstacle[2])
            if self.anim_rect.colliderect(obstacle_rect):
                player_dx, player_dy = 0, 0
                camera_dx, camera_dy = 0, 0
                break  # Прекратить проверку столкновения, если уже произошло

        self.x += player_dx
        self.y += player_dy
        camera.x += camera_dx
        camera.y += camera_dy

        self.x = max(self.scr_weight // 2, min(self.x, self.map_weight - self.scr_weight // 2))
        self.y = max(self.scr_height // 2, min(self.y, self.map_height - self.scr_height // 2))
        self.update(camera)

    def update(self, camera):
        self.run = self.run
        self.Direction = self.Direction
        self.anim = self.anim
        self.rect = (self.x, self.y)
        camera.update(camera.x, camera.y)

        #  print(self.x, self.y, self.Direction)

    def get_map(self, weight, height, tile_size):
        self.tile_size = tile_size
        self.map_weight = weight
        self.map_height = height

    def get_src(self, weight, height):
        self.scr_weight = weight
        self.scr_height = height
