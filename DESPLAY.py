import pygame
import sys
from Button import Button
from Bacground import background_anim


def main_menu(green_button, screen, screen_weight, red_button, screen_height):
    running = True
    i = 0
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 0))
        an, ln = background_anim(i, screen_weight, screen_height)
        an_rect = an.get_rect()
        screen.blit(an, an_rect)
        font = pygame.font.Font(None, 72)
        text_surface = font.render("Button test", True, [255, 255, 255])
        text_rect = text_surface.get_rect(center=(screen_weight/2, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            green_button.green_handle_event(event, screen, screen_weight, screen_height)
            red_button.red_handle_event(event)

        if i < (ln-1):
            i += 1
        else:
            i = 0

        green_button.check_hover(pygame.mouse.get_pos())
        green_button.draw(screen)
        red_button.check_hover(pygame.mouse.get_pos())
        red_button.draw(screen)
        pygame.display.flip()
        clock.tick(20)


def start():

    button_weight, button_height = 200, 100
    screen_weight, screen_height = 1500, 800  # размер окна приложения
    screen = pygame.display.set_mode([screen_weight, screen_height])  # создание окна приложения
    pygame.display.set_caption("CS2D")  # название окна приложенния
    green_button = Button(screen_weight/2 - (200/2), 400, button_weight, button_height, 'play', 'Button/play_button_not_press2.png', 'Button/green_button_press.png')
    red_button = Button(screen_weight/2 - (200/2), (green_button.y+green_button.height), button_weight, button_height, 'Exit', 'Button/red_button_not_press.png', 'Button/red_button_press.png')
    main_menu(green_button, screen, screen_weight, red_button, screen_height)


if __name__ == "__main__":
    pygame.init()
    start()
