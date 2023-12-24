import pygame

pygame.init()
width = 6 * 45
height = 60 * 45
water_tile = [
    pygame.transform.scale(pygame.image.load('water/water_frame_1.png'), [width, height]),
    pygame.transform.scale(pygame.image.load('water/water_frame_2.png'), [width, height]),
    pygame.transform.scale(pygame.image.load('water/water_frame_3.png'), [width, height]),
    pygame.transform.scale(pygame.image.load('water/water_frame_4.png'), [width, height])
]

walk_right = [
            pygame.image.load('Character1/Right/право 1.png'),
            pygame.image.load('Character1/Right/право 2.png'),
            pygame.image.load('Character1/Right/право 11.png'),
            pygame.image.load('Character1/Right/право 3.png')
        ]

walk_left = [
            pygame.image.load('Character1/Left/лево 1.png'),
            pygame.image.load('Character1/Left/лево 2.png'),
            pygame.image.load('Character1/Left/лево 11.png'),
            pygame.image.load('Character1/Left/лево 3.png')
        ]

walk_up = [
            pygame.image.load('Character1/Back/назад 1.png'),
            pygame.image.load('Character1/Back/назад 2.png'),
            pygame.image.load('Character1/Back/назад 11.png'),
            pygame.image.load('Character1/Back/назад 3.png')
        ]

walk_down = [
            pygame.image.load('Character1/Forward/прямо 1.png'),
            pygame.image.load('Character1/Forward/прямо 2.png'),
            pygame.image.load('Character1/Forward/прямо 11.png'),
            pygame.image.load('Character1/Forward/прямо 3.png')
        ]

walk_all = [
                pygame.image.load('Character1/Right/право 1.png'),
                pygame.image.load('Character1/Left/лево 1.png'),
                pygame.image.load('Character1/Back/назад 1.png'),
                pygame.image.load('Character1/Forward/прямо 1.png')
            ]


def Animation1(an):  # функция для передачи массивов с анимациями в класс Desplay
    pygame.init()
    if an == "R":
        return walk_right
    elif an == "L":
        return walk_left
    elif an == "U":
        return walk_up
    elif an == "D":
        return walk_down
    else:
        if an == "A":
            return walk_all


def Water_anim(anim):
    return water_tile[anim]
