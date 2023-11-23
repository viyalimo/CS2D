import pygame
from pygame import Surface
from Map import Map
from Netv import Network
from Camera import Camera
from player import Player


def redrawWindow(win, player, player2, mapa, camera, widt, heigh):
    print(player2, "sheet")
    win.fill('black')
    win = mapa.DRAWMAP(win, camera)
    player.draw(win)
    if not player2:
        pass
    else:
        if (player.x > player2.x + mapa.width) and (player.y > player2.y + mapa.height):
            pass
        else:
            player2.Draw_player2(win, player2, camera)
    pygame.display.update()


def main(weight, height, mapa, camera):
    run = True
    n = Network()
    players_data = n.getP()
    pl1 = players_data[0]
    pl2 = players_data[1]
    p = Player(pl1[0], pl1[1], pl1[2])
    p2 = Player(pl2[0], pl2[1], pl2[2])
    p.get_map(mapa.H_W()[0], mapa.H_W()[1], mapa.tile_size)
    print(mapa.H_W()[0], mapa.H_W()[1])
    p.get_src(weight, height)
    clock = pygame.time.Clock()
    current_player = 0
    solo_player = None
    while run:
        print("start", n.update(p))
        if n.update(p)[0] == 2:
            a = n.update(p)[1]
            # print(a, "players == 2")
            # print(a[0], 'toplayer')
            p2.x = a[0]
            p2.y = a[1]
            p2.Direction = a[2]
            solo_player = p2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move(camera, mapa.obstac)
        print(p.x, p.y, p.Direction)

        redrawWindow(screen, p, solo_player, mapa, camera, weight, height)
        clock.tick(60)  # FPS


if __name__ == "__main__":
    screen_weight, screen_height = 1500, 800  # размер окна приложения
    screen = pygame.display.set_mode((screen_weight, screen_height))  # создание окна приложения
    pygame.display.set_caption("CS2D")  # название окна приложенния
    mapa = Map(1)
    camera = Camera(screen_weight, screen_height, mapa.H_W()[0], mapa.H_W()[1])
    main(screen_weight, screen_height, mapa, camera)  # переход в функцию main с передачей высоты 'и ширины окна
