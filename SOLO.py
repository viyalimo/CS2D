import pygame
from Map import Map
from Camera import Camera
from player import Player


def redrawWindow(win, player, mapa, camera, weight, height):
    win.fill('black')
    win = mapa.DRAWMAP(win, camera)
    player.draw(win, camera)
    pygame.display.update()


def main(weight, height, mapa, camera):
    run = True  # состояние игрового процесса
    p = Player(weight // 2, height // 2, "L")
    p.get_map(mapa.H_W()[0], mapa.H_W()[1])
    print(mapa.H_W()[0], mapa.H_W()[1])
    p.get_src(weight, height)
    clock = pygame.time.Clock()  # создание внутренних часов
    while run:  # запуск основного игрового цикла
        for event in pygame.event.get():  # функция закрытия окна
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move(camera)  # изменение координат игрока 1
        print(p.x, p.y, p.Direction)
        #camera.center(p.x, p.y)
        # print(camera.x, camera.y)
        redrawWindow(screen, p, mapa, camera, weight, height)  # отрисовка игрового окна для игрока 1
        clock.tick(60)  # FPS


if __name__ == "__main__":
    screen_width, screen_height = 1500, 800  # размер окна приложения
    screen = pygame.display.set_mode((screen_width, screen_height))  # создание окна приложения
    pygame.display.set_caption("CS2D")  # название окна приложенния
    mapa = Map(1)
    camera = Camera(screen_width, screen_height, mapa.H_W()[0], mapa.H_W()[1])
    main(screen_width, screen_height, mapa, camera)  # переход в функцию main с передачей высоты и ширины окна

