import pygame
from pygame import Surface

from network import Network
from Map import View_world, block_size


def redrawWindow(win, player, player2):
    win = DRAWMAP(win)
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


def DRAWMAP(win):
    world = View_world(1)
    tile_Size = block_size()
    win.fill('black')
    for row in range(len(world)):
        for col in range(len(world[row])):
            x = col * tile_Size
            y = row * tile_Size

            if world[row][col] == 'B':
                win.blit(imbg, (x, y, tile_Size, tile_Size))
            else:
                pygame.draw.rect(win, 'gray10', (x, y, tile_Size, tile_Size), 1)
    return win


if __name__ == "__main__":
    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption("CS2D")
    imbg = pygame.image.load('images/обычная трава.png').convert_alpha()
    anim = 0
    main()
