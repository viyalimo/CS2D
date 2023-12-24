import pygame
from Bacground import background_anim
import sys
from Map import Map
from Camera import Camera
import pygame_gui
from network import Network
import socket


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
            if self.sound:
                self.sound.play()
            ret = self.local_global(screen, weight, height)
            if ret is not None:
                return ret[0], ret[1], ret[2]

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
            # main(screen, weight, height, mapa, camera, inf)
            if self.sound:
                self.sound.play()
            print(inf, mapa, camera)
            return inf, mapa, camera

    def yellow_handle_event_CON(self, event, screen, weight, height):  # действие кнопки присоединиться
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            ret = self.connect(screen, weight, height, 'None')
            if ret is not None:
                return ret[0], ret[1], ret[2]
            if self.sound:
                self.sound.play()

    def yellow_handle_startcon(self, event, screen, weight, height,
                               inf):  # начало игры после нажатия кнопки начать игру в подключении
        mapa = Map(1)
        camera = Camera(weight, height, mapa.H_W()[0], mapa.H_W()[1])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if not isinstance(inf, str):
                inf = str(inf)
            return inf, mapa, camera

    def green_escape(self, event):  # запуск игры из escape
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            return True
        return False

    def red_back(self, event):  # кнопка возвращения
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            return True
        return False

    def host_con(self, screen, screen_weight, screen_height):  # меню хоста
        running = True
        yellow_button_HOST = Button(screen_weight / 2 - (300 / 2), 400, 300, 100, "создать", 'Button/yellow_button.png')
        yellow_button_CON = Button(screen_weight / 2 - (300 / 2), (yellow_button_HOST.y + yellow_button_HOST.height),
                                   300,
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

                ret = yellow_button_HOST.yellow_handle_event_HOST(event, screen, screen_weight, screen_height)
                if ret is not None:
                    return ret[0], ret[1], ret[2]
                ret = yellow_button_CON.yellow_handle_event_CON(event, screen, screen_weight, screen_height)
                if ret is not None:
                    return ret[0], ret[1], ret[2]
                # return inf, mapa, camera

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
            clock.tick(10)

    def escape_press(self, screen, weight, height, n):  # меню во время игры
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
                    return 'Exit'
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
            clock.tick(10)

    def connect(self, screen, weight, height, fin):
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
        red_button_back = Button(weight / 2 - (200 / 2), (green_button_CON.y + green_button_CON.height), 200, 100,
                                 'назад',
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
            if fin == 'None':
                text_surface = font.render("Введите IP адрес сервера ниже", True, [255, 255, 255])
                text_rect = text_surface.get_rect(center=(weight / 2, 50))
                screen.blit(text_surface, text_rect)
            if fin == 'Error':
                text_surface = font.render("Попробуйте ещё раз", True, [255, 255, 255])
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
                ret = green_button_CON.yellow_handle_startcon(event, screen, weight, height, inf)
                if ret is not None:
                    return ret[0], ret[1], ret[2]
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
            clock.tick(10)

    def local_global(self, screen, screen_weight, screen_height):
        button_weight, button_height = 300, 100
        green_button = Button(screen_weight / 2 - (300 / 2), 400, button_weight, button_height, 'глобальная сеть',
                              'Button/play_button_not_press2.png', 'Button/green_button_press.png')
        red_button = Button(screen_weight / 2 - (300 / 2), (green_button.y + green_button.height), button_weight,
                            button_height, 'локальная сеть', 'Button/play_button_not_press2.png',
                            'Button/green_button_press.png')
        red_button_back = Button(screen_weight / 2 - (300 / 2), (red_button.y + red_button.height), button_weight,
                                 button_height, 'назад', 'Button/red_button_not_press.png',
                                 'Button/red_button_press.png')
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
                ret = red_button.red_global(screen, screen_weight, screen_height, event)
                if ret is not None:
                    return ret[0], ret[1], ret[2]
                con = red_button_back.red_back(event)
                if con:
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
            red_button_back.check_hover(pygame.mouse.get_pos())
            red_button_back.draw(screen)
            clock.tick(10)

    def red_global(self, screen, weight, height, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            ret = self.host_con(screen, weight, height)
            if ret is not None:
                return ret[0], ret[1], ret[2]
