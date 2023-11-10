import pygame
from Map import Map
from Camera import Camera
from player import Player


def H_W_MAP(width, hight):
    data = (width, hight)
    return data


def redrawWindow(win, player, mapa, camera, widt, heigh):
    win.fill('black')
    win = mapa.DRAWMAP(win, camera)
    player.draw(win)
    camera.update(player)
    pygame.display.update()


def main(widt, heigh):
    run = True  # состояние игрового процесса
    mapa = Map(1)  # создание объекта класса Map, который создаёт карту
    p = Player(0, 0, mapa.H_W()[0], mapa.H_W()[1], "L")
    clock = pygame.time.Clock()  # создание внутренних часов
    camera = Camera(widt, heigh, mapa.H_W()[0], mapa.H_W()[1])  # создание объекта класса Camera и передача размеров видимой области, а также передача размеров карты
    while run:  # запуск основного игрового цикла
        for event in pygame.event.get():  # функция закрытия окна
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()  # изменение координат игрока 1
        print(p.x, p.y, p.Direction)
        camera.update(p)  # обновление камеры относительно игрока 1
        redrawWindow(screen, p, mapa, camera, widt, heigh)  # отрисовка игрового окна для игрока 1
        clock.tick(60)  # FPS


if __name__ == "__main__":
    screen_width, screen_height = 1500, 800  # размер окна приложения
    screen = pygame.display.set_mode((screen_width, screen_height))  # создание окна приложения
    pygame.display.set_caption("CS2D")  # название окна приложенния
    main(screen_width, screen_height)  # переход в функцию main с передачей высоты и ширины окна


