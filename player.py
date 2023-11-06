import pygame
from Character import Animation1


class Player:
    def __init__(self, x, y, Direction):
        self.Direction = "L"
        self.x = x
        self.y = y
        # self.width = width
        # self.height = height
        # self.color = color
        self.rect = (x, y)
        self.vel = 10
        self.anim = 0

    def draw(self, win):
        ticreite = pygame.time.Clock()
        # pygame.draw.rect(screen, self.color, self.rect)
        win.blit(Animation1(self.Direction)[self.anim], self.rect)
        if self.anim < 3:
            self.anim += 1
        else:
            self.anim = 0
        ticreite.tick(20)

    def move(self):
        now_press = pygame.key.get_pressed()
        if now_press[pygame.K_LEFT] or now_press[pygame.K_a]:
            self.x -= self.vel
            self.Direction = "L"
        if now_press[pygame.K_RIGHT] or now_press[pygame.K_d]:
            self.Direction = 'R'
            self.x += self.vel
        if now_press[pygame.K_UP] or now_press[pygame.K_w]:
            self.y -= self.vel
            self.Direction = "U"
        if now_press[pygame.K_DOWN] or now_press[pygame.K_s]:
            self.y += self.vel
            self.Direction = "D"

        self.update()

    def update(self):
        self.Direction = self.Direction
        self.anim = self.anim
        self.rect = (self.x, self.y)
        print(self.x, self.y, self.Direction)
