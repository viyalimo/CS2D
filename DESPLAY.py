
import pygame
import sys
from Bacground import background_anim
from player import Player
from network import Network
from Character import Animation1
from HP import HP
from bul_shop import Bull_shop
from Button import Button


screen_weight, screen_height = 1500, 800

hp = HP(screen_weight, screen_height)
b_shop = Bull_shop(screen_weight, screen_height)


def redrawWindow(win, player, player_data, mapa, camera, bullets, scr_weight, scr_height, health, bull_shop):  # отрисовка основного геймплея
    # print(player2)
    win.fill('black')
    win = mapa.DRAWMAP(win, camera)
    player.draw(win)
    player2 = player_data[0]
    player3 = player_data[1]
    player4 = player_data[2]
    if not player2:
        pass
    else:
        anim_surface = Animation1(player2[2])[player2[3]]
        anim_surface = pygame.transform.scale(anim_surface, [65, 90])
        anim_rect = anim_surface.get_rect()
        anim_rect.topleft = (player2[0], player2[1])
        win.blit(anim_surface, camera.apply(anim_rect))
        del anim_surface

    if not player3:
        pass
    else:
        anim_surface = Animation1(player3[2])[player3[3]]
        anim_surface = pygame.transform.scale(anim_surface, [65, 90])
        anim_rect = anim_surface.get_rect()
        anim_rect.topleft = (player3[0], player3[1])
        win.blit(anim_surface, camera.apply(anim_rect))
        del anim_surface

    if not player4:
        pass
    else:
        anim_surface = Animation1(player4[2])[player4[3]]
        anim_surface = pygame.transform.scale(anim_surface, [65, 90])
        anim_rect = anim_surface.get_rect()
        anim_rect.topleft = (player4[0], player4[1])
        win.blit(anim_surface, camera.apply(anim_rect))
        del anim_surface

    for bullet in bullets:
        b_img = pygame.Surface([10, 4]).convert_alpha()
        b_img.fill([255, 255, 0])
        b_img = pygame.transform.rotate(b_img, bullet[1])
        bullet_rect = b_img.get_rect(center=[bullet[0][0], bullet[0][1]])
        win.blit(b_img, camera.apply(bullet_rect))
        del b_img
    hp.HP_blit(health, win)
    b_shop.bul_shop_blit(bull_shop, win)
    pygame.display.update()


def main(screen, weight, height, mapa, camera, inf):  # основной цикл
    run = True
    Butt = Button(1, 1, 1, 1, '1', 'images/grass.jpg', )
    n = Network(str(inf))
    inf = n.connect(mapa.H_W()[0], mapa.H_W()[1], mapa.tile_size, mapa.obstacles_player, mapa.obstac_bul)
    if inf is None:
        Butt.connect(screen, weight, height, 'Error')
    pl1, pl2, pl3, pl4 = inf
    p = Player(pl1[0], pl1[1], pl1[2])
    p2 = pl2  # 2 игрок
    p3 = pl3
    p4 = pl4
    p.get_map(mapa.H_W()[0], mapa.H_W()[1], mapa.tile_size)
    print(mapa.H_W()[0], mapa.H_W()[1])
    p.get_src(weight, height)
    clock = pygame.time.Clock()
    HP = 5
    bull_shop = 24
    while run:
        coord_bul = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                n.Disconect()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inf = Butt.escape_press(screen, weight, height, n)
                    if inf == "Exit":
                        main_menu()
                if event.key == pygame.K_r:
                    coord_bul = 'recharge'
            if event.type == pygame.MOUSEBUTTONDOWN and bull_shop > 0 and isinstance(coord_bul, list):
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
        data, true_pos, bullets, HP, bull_shop = n.Send(p, coord_bul)

        p.x = true_pos[0]
        p.y = true_pos[1]
        if n.qplayer == 1:
            p2 = None
            p3 = None
            p4 = None
        if n.qplayer == 2:
            if data is None:
                p2 = data
            else:
                p2 = data[0]
            p3 = None
            p4 = None
        if n.qplayer == 3:
            if data is None:
                p2 = None
                p3 = None
            elif len(data) == 1:
                p2 = data[0]
                p3 = None
            else:
                p2 = data[0]
                p3 = data[1]
            p4 = None
        if n.qplayer == 4:
            if data is None:
                p2 = None
                p3 = None
                p4 = None
            elif len(data) == 1:
                p2 = data[0]
                p3 = None
                p4 = None
            elif len(data) == 2:
                p2 = data[0]
                p3 = data[1]
                p4 = None
            else:
                p2 = data[0]
                p3 = data[1]
                p4 = data[2]

        player_data = [p2, p3, p4]
        p.move(camera, mapa.obstacles_player, mapa.obstac_bul)
        redrawWindow(screen, p, player_data, mapa, camera, bullets, weight, height, HP, bull_shop)
        clock.tick(60)  # FPS

def main_menu():
    button_weight, button_height = 200, 100
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
        clock.tick(10)


if __name__ == "__main__":
    pygame.init()
    main_menu()
