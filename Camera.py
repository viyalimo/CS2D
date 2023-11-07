import pygame

class Camera:
    def __init__(self, width, height, map_width, map_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, entity):
        return entity.move(self.camera.topleft)

    def update(self, target):
        x = -target.x + int(self.width / 2)
        y = -target.y + int(self.height / 2)

        # Ограничьте камеру, чтобы она не выходила за пределы карты
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.map_width - self.width), x)
        y = max(-(self.map_height - self.height), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)