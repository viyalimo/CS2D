import pygame
from Character import Animation1


class Player:
    def __init__(self, x, y, Direction):
        self.map_height = 0
        self.map_weight = 0
        self.player_weight = 0
        self.player_height = 0
        self.Direction = "L"
        self.scr_weight = 0
        self.scr_height = 0
        self.x = x
        self.y = y
        # self.screen_width = screen_width
        # self.height = height
        # self.color = color
        self.rect = (x, y)
        self.speed = 10
        self.anim = 0
        self.run = False

    def draw(self, win):
        ticreite = pygame.time.Clock()
        anim_surface = Animation1(self.Direction)[self.anim]
        anim_rect = anim_surface.get_rect()
        self.player_weight = anim_rect.width
        self.player_height = anim_rect.height
        anim_rect.topleft = self.rect
        win.blit(anim_surface, anim_rect)  # Использовать координаты topleft из self.rect
        if self.anim < 3 and self.run:
            self.anim += 1
        else:
            if self.anim == 3:
                self.anim = 0
                self.run = False
        ticreite.tick(25)

    def move(self, camera):
        now_press = pygame.key.get_pressed()
        if now_press[pygame.K_LEFT] or now_press[pygame.K_a]:
            self.run = True
            self.x -= self.speed
            self.Direction = "L"
        if now_press[pygame.K_RIGHT] or now_press[pygame.K_d]:
            self.run = True
            self.Direction = 'R'
            self.x += self.speed
        if now_press[pygame.K_UP] or now_press[pygame.K_w]:
            self.run = True
            self.y -= self.speed
            self.Direction = "U"
        if now_press[pygame.K_DOWN] or now_press[pygame.K_s]:
            self.run = True
            self.y += self.speed
            self.Direction = "D"
        self.x = max(self.scr_weight // 2, min(self.x, self.map_weight - self.player_weight))
        self.y = max(self.scr_height // 2, min(self.y, self.map_height - self.player_height))
        data = (self.x, self.y)
        camera.update(data)
        self.update()

    def update(self):
        self.run = self.run
        self.Direction = self.Direction
        self.anim = self.anim
        self.rect = (self.x, self.y)
        #  print(self.x, self.y, self.Direction)

    def get_map(self, weight, height):
        self.map_weight = weight
        self.map_height = height

    def get_src(self, weight, height):
        self.scr_weight = weight
        self.scr_height = height