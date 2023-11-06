import pygame


class Character:
    posx = None  # место появления игрока на карте по координате x
    posy = None
    speed = None  # скорость персонажа
    x_stop = None  # максимальное значение где игрок может находится на карте
    y_stop = None
    # анимации персонажа
    walk_right = []
    walk_left = []
    walk_up = []
    walk_down = []
    walk_all = []


ch1 = Character()
ch1.posx = 400
ch1.posy = 400
ch1.speed = 1
ch1.x_stop = 1440
ch1.y_stop = 660


def Animation1(an):  # функция для передачи массивов с анимациями в класс Desplay
    if an == "R":
        walk_right = [
            pygame.image.load('Character1/Right/право 1.png').convert_alpha(),
            pygame.image.load('Character1/Right/право 2.png').convert_alpha(),
            pygame.image.load('Character1/Right/право 11.png').convert_alpha(),
            pygame.image.load('Character1/Right/право 3.png').convert_alpha()
        ]
        return walk_right
    elif an == "L":
        walk_left = [
            pygame.image.load('Character1/Left/лево 1.png').convert_alpha(),
            pygame.image.load('Character1/Left/лево 2.png').convert_alpha(),
            pygame.image.load('Character1/Left/лево 11.png').convert_alpha(),
            pygame.image.load('Character1/Left/лево 3.png').convert_alpha()
        ]
        return walk_left
    elif an == "U":
        walk_up = [
            pygame.image.load('Character1/Back/назад 1.png').convert_alpha(),
            pygame.image.load('Character1/Back/назад 2.png').convert_alpha(),
            pygame.image.load('Character1/Back/назад 11.png').convert_alpha(),
            pygame.image.load('Character1/Back/назад 3.png').convert_alpha()
        ]
        return walk_up
    elif an == "D":
        walk_down = [
            pygame.image.load('Character1/Forward/прямо 1.png').convert_alpha(),
            pygame.image.load('Character1/Forward/прямо 2.png').convert_alpha(),
            pygame.image.load('Character1/Forward/прямо 11.png').convert_alpha(),
            pygame.image.load('Character1/Forward/прямо 3.png').convert_alpha()
        ]
        return walk_down
    else:
        if an == "A":
            walk_all = [
                pygame.image.load('Character1/Right/право 1.png').convert_alpha(),
                pygame.image.load('Character1/Left/лево 1.png').convert_alpha(),
                pygame.image.load('Character1/Back/назад 1.png').convert_alpha(),
                pygame.image.load('Character1/Forward/прямо 1.png').convert_alpha()
            ]
            return walk_all
