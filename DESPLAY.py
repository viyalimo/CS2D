import pygame
from pygame import Surface
from Map import Map
from network import Network
from Camera import Camera
from player import Player


def redrawWindow(win, player, player2, mapa, camera, widt, heigh):
    win.fill('black')
    win = mapa.DRAWMAP(win, camera)
    player.draw(win)
    try:
        player2.draw(win)
    except:
        pass
    pygame.display.update()


def main(widt, heigh):
    run = True  # состояние игрового процесса
    try:
        n = Network()  # создание объекта класса, отвечающего за передачу и отправку информации на сервер
        p = n.getP()  # взятие начального положения игрока
    except:
        p = Player(0, 0, "L")

    mapa = Map(1)  # создание объекта класса Map, который создаёт карту
    clock = pygame.time.Clock()  # создание внутренних часов
    camera = Camera(widt, heigh, 3000,
                    3000)  # создание объекта класса Camera и передача размеров видимой области, а также передача размеров карты
    while run:  # запуск основного игрового цикла
        try:
            p2 = n.send(p) # отправка позиции игрока 1 и приём информации об координатах игрока 2
        except:
            pass
        for event in pygame.event.get():  # функция закрытия окна
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()  # изменение координат игрока 1
        camera.update(p)  # обновление камеры относительно игрока 1
        redrawWindow(screen, p, p2, mapa, camera, widt, heigh)  # отрисовка игрового окна для игрока 1
        clock.tick(60)  # FPS


if __name__ == "__main__":
    width = 1500  # размер окна приложения
    height = 800
    screen = pygame.display.set_mode((width, height))  # создание окна приложения
    pygame.display.set_caption("CS2D")  # название окна приложенния
    main(width, height)  # переход в функцию main с передачей высоты и ширины окна
