import pygame
from pygame import Surface
from Map import Map
from network import Network


def redrawWindow(win, player, player2, map):
    win.fill('black')
    win = map.DRAWMAP(win)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    map = Map(2000, 2000)
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(screen, p, p2, map)


if __name__ == "__main__":
    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption("CS2D")
    anim = 0
    main()

# class Camera:
#     def __init__(self):
