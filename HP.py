import pygame


class HP:
    def __init__(self, sc_weight, sc_height):
        self.sc_weight = sc_weight
        self.sc_height = sc_height
        self.size = [300, 15]
        self.tile_hp = [
            pygame.transform.scale(pygame.image.load('HP/HP_0.png'), self.size),
            pygame.transform.scale(pygame.image.load('HP/HP_1.png'), self.size),
            pygame.transform.scale(pygame.image.load('HP/HP_2.png'), self.size),
            pygame.transform.scale(pygame.image.load('HP/HP_3.png'), self.size),
            pygame.transform.scale(pygame.image.load('HP/HP_4.png'), self.size),
            pygame.transform.scale(pygame.image.load('HP/HP_5.png'), self.size),
            pygame.transform.scale(pygame.image.load('HP/HP_6.png'), self.size)
        ]

    def HP_blit(self, con, screen):
        HP_IMAGE = self.tile_hp[con]
        HP_rect = HP_IMAGE.get_rect()
        HP_rect.topleft = [0, 20]
        screen.blit(HP_IMAGE, HP_rect)

