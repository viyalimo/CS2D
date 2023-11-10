import pygame
from player import Player

class Camera:
    def __init__(self, sc_width, sc_height, map_width, map_height):
        self.camera = pygame.Rect(0, 0, sc_width, sc_height)
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, entity):
        return entity.move(self.camera.topleft)

    def update(self, target):
        x = -target.x + int(self.sc_width / 2)
        print(target.x)
        y = -target.y + int(self.sc_height / 2)
        print(target.y)

        # Ограничьте камеру, чтобы она не выходила за пределы карты
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.map_width - self.sc_width), x)
        y = max(-(self.map_height - self.sc_height), y)

        self.camera = pygame.Rect(x, y, self.sc_width, self.sc_height)
