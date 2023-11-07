import pygame
from pygame import Surface
from Map import Map
from network import Network
from Camera import Camera


def redrawWindow(win, player, player2, mapa, camera, widt, heigh):
    win.fill('black')
    win = mapa.DRAWMAP(win, camera)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main(widt, heigh):
    run = True
    n = Network()
    p = n.getP()
    print(p)
    mapa = Map(3000, 3000)
    clock = pygame.time.Clock()
    camera = Camera(widt, heigh, 2000, 2000)
    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        camera.update(p)
        redrawWindow(screen, p, p2, mapa, camera, widt, heigh)


if __name__ == "__main__":
    width = 1500
    height = 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("CS2D")
    anim = 0
    main(width, height)
