import pygame
from Character import Animation1


class Player:
    def __init__(self, x, y, map_width, map_hight, Direction):
        self.map_height = map_hight
        self.map_weight = map_hight
        self.Direction = "L"
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
        anim_rect.topleft = self.rect
        win.blit(anim_surface, anim_rect)  # Использовать координаты topleft из self.rect
        if self.anim < 3 and self.run:
            self.anim += 1
        else:
            if self.anim == 3:
                self.anim = 0
                self.run = False
        ticreite.tick(25)

    def move(self):
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

        self.update()

    def update(self):
        self.run = self.run
        self.Direction = self.Direction
        self.anim = self.anim
        self.rect = (self.x, self.y)
        #  print(self.x, self.y, self.Direction)
