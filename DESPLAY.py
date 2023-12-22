import pygame
import sys
from Bacground import background_anim
import socket
from player import Player
from Map import Map
from Camera import Camera
import pygame_gui
from network import Network
from Character import Animation1
from HP import HP
from Button import Button


def redrawWindow(win, player, player2, mapa, camera, bullets, scr_weight, scr_height, health):  # отрисовка основного геймплея
    # print(player2)
    hp = HP(scr_weight, scr_height)
    win.fill('black')
    win = mapa.DRAWMAP(win, camera)
    player.draw(win)
    if not player2:
        pass
    else:
        if (player.x > player2[0] + mapa.width) and (player.y > player2[1] + mapa.height):
            pass
        else:
            anim_surface = Animation1(player2[2])[player2[3]]
            anim_surface = pygame.transform.scale(anim_surface, [65, 90])
            anim_rect = anim_surface.get_rect()
            anim_rect.topleft = (player2[0], player2[1])
            win.blit(anim_surface, camera.apply(anim_rect))

    for bullet in bullets:
        # if not win.get_rect().collidepoint([bullet[0][0], bullet[0][1]]):
        b_img = pygame.Surface([10, 4]).convert_alpha()
        b_img.fill([255, 255, 0])
        b_img = pygame.transform.rotate(b_img, bullet[1])
        bullet_rect = b_img.get_rect(center=[bullet[0][0], bullet[0][1]])
        win.blit(b_img, camera.apply(bullet_rect))
    hp.HP_blit(health, win)
    pygame.display.update()


def main(screen, weight, height, mapa, camera, inf):  # основной цикл
    run = True
    p2 = None
    bullets = []
    n = Network(str(inf))
    pl1, pl2 = n.connect(mapa.H_W()[0], mapa.H_W()[1], mapa.tile_size)
    p = Player(pl1[0], pl1[1], pl1[2])
    p2 = pl2  # 2 игрок
    p.get_map(mapa.H_W()[0], mapa.H_W()[1], mapa.tile_size)
    print(mapa.H_W()[0], mapa.H_W()[1])
    p.get_src(weight, height)
    clock = pygame.time.Clock()
    Butt = Button(1, 1, 1, 1, '1', 'images/ground.jpg', )
    HP = 5
    while run:
        coord_bul = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inf = Butt.escape_press(screen, weight, height, n)
                    if inf == "Exit":
                        main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx = p.x + (mx - p.coordinateblit[0])
                my = p.y + (my - p.coordinateblit[1])
                if p.x > mx:
                    coord_bul.append([p.x - 0.1, p.y + p.player_height / 2, mx, my])
                elif p.x + p.player_weight < mx:
                    coord_bul.append([p.x + p.player_weight + 0.1, p.y + p.player_height / 2, mx, my])
                elif (p.x <= mx <= p.x + p.player_weight) and (p.y < my):
                    coord_bul.append([p.x + p.player_weight / 2, p.y + p.player_height + 0.1, mx, my])
                elif (p.x <= mx <= p.x + p.player_weight) and (p.y > my):
                    coord_bul.append([p.x + p.player_weight / 2, p.y + 0.1, mx, my])
                else:
                    continue
        data, true_pos, bullets, HP = n.Send(p, coord_bul)
        # print(data, "PLAYER 1")
        p.x = true_pos[0]
        p.y = true_pos[1]
        if n.qplayer == 1:
            p2 = None
        if n.qplayer == 2:
            p2 = data

        p.move(camera, mapa.obstac)
        # print('camera:', camera.x, camera.y, 'player:', p.x, p.y, p.Direction)
        # print(f'c_x: {camera.x}, c_y: {camera.y}, p_x: {p.x}, p_y: {p.y}')
        redrawWindow(screen, p, p2, mapa, camera, bullets, weight, height, HP)
        clock.tick(60)  # FPS


def main_menu():
    button_weight, button_height = 200, 100
    screen_weight, screen_height = 1500, 800  # размер окна приложения
    screen = pygame.display.set_mode([screen_weight, screen_height])  # создание окна приложения
    pygame.display.set_caption("CS2D")  # название окна приложенния
    green_button = Button(screen_weight / 2 - (200 / 2), 400, button_weight, button_height, 'play',
                          'Button/play_button_not_press2.png', 'Button/green_button_press.png')
    red_button = Button(screen_weight / 2 - (200 / 2), (green_button.y + green_button.height), button_weight,
                        button_height, 'Exit', 'Button/red_button_not_press.png', 'Button/red_button_press.png')
    running = True
    i = 0

    clock = pygame.time.Clock()
    while running:
        pygame.display.flip()
        screen.fill([0, 0, 0])
        an, ln = background_anim(i, screen_weight, screen_height)
        an_rect = an.get_rect()
        screen.blit(an, an_rect)
        font = pygame.font.Font(None, 72)
        text_surface = font.render("CS_2D", True, [255, 255, 255])
        text_rect = text_surface.get_rect(center=(screen_weight / 2, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            ret = green_button.green_handle_event(event, screen, screen_weight, screen_height)
            if ret is not None:
                inf, mapa, camera = ret[0], ret[1], ret[2]
                main(screen, screen_weight, screen_height, mapa, camera, inf)
            red_button.red_handle_event(event)

        if i < (ln - 1):
            i += 1
        else:
            i = 0

        green_button.check_hover(pygame.mouse.get_pos())
        green_button.draw(screen)
        red_button.check_hover(pygame.mouse.get_pos())
        red_button.draw(screen)
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    main_menu()
