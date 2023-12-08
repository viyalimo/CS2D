import pygame


class Camera:
    def __init__(self, sc_width, sc_height, map_width, map_height):
        self.camera = pygame.Rect(0, 0, sc_width, sc_height)
        self.x_center = -sc_width // 2
        self.y_center = -sc_height // 2
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.map_width = map_width
        self.map_height = map_height
        self.x = 0
        self.y = 0
        self.min_x = sc_width / 2
        self.min_y = sc_height / 2
        self.max_x = map_width - self.min_x
        self.max_y = map_height - self.min_y

    def apply(self, entity):
        self.x = -(max(0, min(- self.x, (self.map_width - self.sc_width))))
        self.y = -(max(0, min(- self.y, (self.map_height - self.sc_height))))
        self.camera = pygame.Rect(self.x, self.y, self.sc_width, self.sc_height)
        return entity.move(self.camera.topleft)

    def update(self, p_x, p_y):
        self.x = p_x
        self.y = p_y
        self.x_center = p_x - (self.sc_width // 2)
        self.y_center = p_y - (self.sc_height // 2)
        self.x = -(max(0, min(-self.x, (self.map_width - self.sc_width))))
        self.y = -(max(0, min(-self.y, (self.map_height - self.sc_height))))
        self.camera = pygame.Rect(self.x, self.y, self.sc_width, self.sc_height)
