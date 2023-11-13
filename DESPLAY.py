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
    if (player.x > player2.x + mapa.width) and (player.y > player2.y + mapa.height):
        pass
    else:
        player2.Draw_player2(win, player2, camera)
    pygame.display.update()


def main(weight, height, mapa, camera):
    run = True
    n = Network()
    p = n.getP()
    p.get_map(mapa.H_W()[0], mapa.H_W()[1])
    p.get_src(weight, height)
    clock = pygame.time.Clock()
    while run:
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move(camera)
        redrawWindow(screen, p, p2, mapa, camera, weight, height)
        clock.tick(60)  # FPS


if __name__ == "__main__":
    screen_weight, screen_height = 1500, 800  # размер окна приложения
    screen = pygame.display.set_mode((screen_weight, screen_height))  # создание окна приложения
    pygame.display.set_caption("CS2D")  # название окна приложенния
    mapa = Map(1)
    camera = Camera(screen_weight, screen_height, mapa.H_W()[0], mapa.H_W()[1])
    main(screen_weight, screen_height, mapa, camera)  # переход в функцию main с передачей высоты и ширины окна
