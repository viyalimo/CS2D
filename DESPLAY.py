import pygame
import sys
from Bacground import background_anim
import socket
from player import Player
from Map import Map
from Camera import Camera
import pygame_gui
from network import Network


def escape_press(screen, weight, height, n):  # меню во время игры
    running = True
    green_button = Button(weight / 2 - (200 / 2), 400, 200, 100, 'продолжить', 'Button/play_button_not_press2.png',
                          'Button/green_button_press.png')
    red_button = Button(weight / 2 - (200 / 2), (green_button.y + green_button.height), 200, 100, 'Выйти',
                        'Button/red_button_not_press.png', 'Button/red_button_press.png')
    i = 0
    clock = pygame.time.Clock()
    while running:
        pygame.display.flip()
        screen.fill((0, 0, 0))
        an, ln = background_anim(i, weight, height)
        an_rect = an.get_rect()
        screen.blit(an, an_rect)
        font = pygame.font.Font(None, 72)
        text_surface = font.render(f"Ваш IP:{socket.gethostbyname_ex(socket.gethostname())[-1][-1]}", True,
                                   [255, 255, 255])
        text_rect = text_surface.get_rect(center=(weight / 2, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return None

            if red_button.red_back_main_menu(event):
                running = False
                n.Disconect()
                main_menu()
            cont = green_button.green_escape(event)
            if cont:
                running = False
                return None

        if i < (ln - 1):
            i += 1
        else:
            i = 0
        green_button.check_hover(pygame.mouse.get_pos())
        green_button.draw(screen)
        red_button.check_hover(pygame.mouse.get_pos())
        red_button.draw(screen)
        clock.tick(60)


def connect(screen, weight, height):
    running = True
    clock = pygame.time.Clock()
    # Создание менеджера элементов пользовательского интерфейса
    manager = pygame_gui.UIManager((weight, height))
    # Создание поля ввода текста
    input_box = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect([weight / 2 - (400 / 2), 300], [400, 50]), manager=manager)
    # Создание кнопки
    green_button_CON = Button(weight / 2 - (200 / 2), 400, 200, 100, 'Начать игру!',
                              'Button/play_button_not_press2.png', 'Button/green_button_press.png')
    red_button_back = Button(weight / 2 - (200 / 2), (green_button_CON.y + green_button_CON.height), 200, 100, 'назад',
                             'Button/red_button_not_press.png', 'Button/red_button_press.png')
    i = 0
    clock = pygame.time.Clock()
    while running:
        time_delta = clock.tick(60) / 1000.0
        pygame.display.flip()
        screen.fill([0, 0, 0])
        an, ln = background_anim(i, weight, height)
        an_rect = an.get_rect()
        screen.blit(an, an_rect)
        font = pygame.font.Font(None, 72)
        text_surface = font.render("Введите IP адрес сервера ниже", True, [255, 255, 255])
        text_rect = text_surface.get_rect(center=(weight / 2, 50))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            inf = input_box.text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inf = input_box.text
                    input_box.kill()  # Удаление поля ввода текста
            green_button_CON.yellow_handle_startcon(event, screen, weight, height, inf)
            if red_button_back.red_back(event):
                running = False
                return None
            manager.process_events(event)
        if i < (ln - 1):
            i += 1
        else:
            i = 0
        manager.update(time_delta)
        manager.draw_ui(screen)
        green_button_CON.check_hover(pygame.mouse.get_pos())
        green_button_CON.draw(screen)
        red_button_back.check_hover(pygame.mouse.get_pos())
        red_button_back.draw(screen)
        clock.tick(60)


def redrawWindow(win, player, player2, mapa, camera, bullets, scr_weight, scr_height):  # отрисовка основного геймплея
    # print(player2)
    win.fill('black')
    win = mapa.DRAWMAP(win, camera)
    player.draw(win, camera)
    if not player2:
        pass
    else:
        if (player.x > player2.x + mapa.width) and (player.y > player2.y + mapa.height):
            pass
        else:
            player2.Draw_player2(win, player2, camera)
    for bullet in bullets:
        # if not win.get_rect().collidepoint([bullet[0][0], bullet[0][1]]):
        b_img = pygame.Surface([10, 4]).convert_alpha()
        b_img.fill([255, 255, 0])
        b_img = pygame.transform.rotate(b_img, bullet[1])
        bullet_rect = b_img.get_rect(center=[bullet[0][0], bullet[0][1]])
        win.blit(b_img, camera.apply(bullet_rect))
    pygame.display.update()


def main(screen, weight, height, mapa, camera, inf):  # основной цикл
    run = True
    p2 = None
    bullets = []
    n = Network(str(inf))
    pl1, pl2 = n.connect(mapa.H_W()[0], mapa.H_W()[1], mapa.tile_size)
    p = Player(pl1[0], pl1[1], pl1[2])
    if isinstance(pl2, list):
        p2 = Player(pl2[0], pl2[1], pl2[2])
    else:
        p2 = None
    p.get_map(mapa.H_W()[0], mapa.H_W()[1], mapa.tile_size)
    print(mapa.H_W()[0], mapa.H_W()[1])
    p.get_src(weight, height)
    clock = pygame.time.Clock()
    while run:
        coord_bul = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape_press(screen, weight, height, n)
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

        data, true_pos, bullets = n.Send(p, coord_bul)
        # print(data, "PLAYER 1")
        p.x = true_pos[0]
        p.y = true_pos[1]
        if n.qplayer == 1:
            p2 = None
        if n.qplayer == 2:
            if not isinstance(p2, Player):
                p2 = Player(data[0], data[1], data[2])
            else:
                p2.x = data[0]
                p2.y = data[1]
                p2.Direction = data[2]
                p2.anim = data[3]

        p.move(camera, mapa.obstac)
        # print('camera:', camera.x, camera.y, 'player:', p.x, p.y, p.Direction)
        # print(f'c_x: {camera.x}, c_y: {camera.y}, p_x: {p.x}, p_y: {p.y}')
        redrawWindow(screen, p, p2, mapa, camera, bullets, weight, height)
        clock.tick(60)  # FPS


def host_con(screen, screen_weight, screen_height):  # меню хоста
    running = True
    yellow_button_HOST = Button(screen_weight / 2 - (300 / 2), 400, 300, 100, "создать", 'Button/yellow_button.png')
    yellow_button_CON = Button(screen_weight / 2 - (300 / 2), (yellow_button_HOST.y + yellow_button_HOST.height), 300,
                               100, 'присоединиться', 'Button/yellow_button.png')
    red_back = Button(screen_weight / 2 - (300 / 2), (yellow_button_CON.y + yellow_button_CON.height), 300, 100,
                      'назад', 'Button/red_button_not_press.png', 'Button/red_button_press.png')
    i = 0
    clock = pygame.time.Clock()
    while running:
        pygame.display.flip()
        screen.fill((0, 0, 0))
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

            yellow_button_HOST.yellow_handle_event_HOST(event, screen, screen_weight, screen_height)
            yellow_button_CON.yellow_handle_event_CON(event, screen, screen_weight, screen_height)
            con = red_back.red_back(event)
            if con:
                running = False
                return None

        if i < (ln - 1):
            i += 1
        else:
            i = 0
        yellow_button_HOST.draw(screen)
        yellow_button_HOST.check_hover(pygame.mouse.get_pos())
        yellow_button_CON.draw(screen)
        yellow_button_CON.check_hover(pygame.mouse.get_pos())
        red_back.draw(screen)
        red_back.check_hover(pygame.mouse.get_pos())
        clock.tick(60)


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

            green_button.green_handle_event(event, screen, screen_weight, screen_height)
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


class Button:
    def __init__(self, x, y, weight, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.weight = weight
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, [weight, height])
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, [weight, height])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False

    def draw(self, screen):  # отрисовка кнопки на экране
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, [255, 255, 255])
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):  # проверка наведения мыши на кнопку
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def green_handle_event(self, event, screen, weight, height):  # действие кнопки начального меню
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if host_con(screen, weight, height):
                return None
            if self.sound:
                self.sound.play()

    def red_handle_event(self, event):  # выход из игры в начальном меню
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            print('exit')
            # if self.sound:
            #     self.sound.play()
            pygame.quit()
            sys.exit()

    def red_back_main_menu(self, event):  # выход из игры в начальном меню
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            return True
        return False

    def yellow_handle_event_HOST(self, event, screen, weight, height):  # действие кнопки HOST
        mapa = Map(1)
        camera = Camera(weight, height, mapa.H_W()[0], mapa.H_W()[1])
        inf = "HOST"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            main(screen, weight, height, mapa, camera, inf)
            if self.sound:
                self.sound.play()

    def yellow_handle_event_CON(self, event, screen, weight, height):  # действие кнопки присоединиться
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            connect(screen, weight, height)
            if self.sound:
                self.sound.play()

    def yellow_handle_startcon(self, event, screen, weight, height,
                               inf):  # начало игры после нажатия кнопки начать игру в подключении
        mapa = Map(1)
        camera = Camera(weight, height, mapa.H_W()[0], mapa.H_W()[1])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if not isinstance(inf, str):
                inf = str(inf)
            main(screen, weight, height, mapa, camera, inf)

    def green_escape(self, event):  # запуск игры из escape
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            return True
        return False

    def red_back(self, event):  # кнопка возвращения
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            return True
        return False


if __name__ == "__main__":
    pygame.init()
    main_menu()
