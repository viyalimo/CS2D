import pygame
from network import Network

width = 1100
heigh = 800
screen = pygame.display.set_mode((width, heigh))
pygame.display.set_caption("CS2D")
anim = 0


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(screen, p, p2)


if __name__ == "__main__":
    main()
"""xyiiiiiiiiiiiiiiiiiiiiiiiiiiii"""