import pygame


class Bull_shop:
    def __init__(self, sc_weight, sc_height):
        self.sc_weight = sc_weight
        self.sc_height = sc_height
        self.size = [300, 15]
        self.tile_bul_shop = [
            pygame.transform.scale(pygame.image.load('shop/shop_0.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_1.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_2.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_3.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_4.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_5.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_6.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_7.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_8.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_9.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_10.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_11.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_12.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_13.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_14.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_15.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_16.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_17.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_18.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_19.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_20.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_21.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_22.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_23.png'), self.size),
            pygame.transform.scale(pygame.image.load('shop/shop_24.png'), self.size),
        ]

    def bul_shop_blit(self, con, screen):
        bul_shop = self.tile_bul_shop[con]
        bul_shop_rect = bul_shop.get_rect()
        bul_shop_rect.topleft = [0, 40]
        screen.blit(bul_shop, bul_shop_rect)

