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
        try:
            x = -target.x + self.sc_width // 2
            print(x)
            y = -target.y + self.sc_height // 2
            print(y)
        except:
            x = -target[0] + self.sc_width // 2
            y = -target[1] + self.sc_height // 2

        self.camera = pygame.Rect(x, y, self.sc_width, self.sc_height)
        """ fuck camera"""
