import pygame
import sys
import math
import time
from scipy.interpolate import CubicSpline

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Размеры окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Размеры сетки и препятствий
GRID_SIZE = 50
OBSTACLE_SIZE = GRID_SIZE

# Создание окна
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption("Простая 2D игра")

# Создание игрока
player_size = 25
player_x = (WINDOW_WIDTH - player_size) // 2
player_y = (WINDOW_HEIGHT - player_size) // 2
player_speed = 2

# Создание камеры
camera = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

# Создание препятствий
obstacles = [(100, 100), (300, 200), (400, 400), (550, 350)]

# Создание пуль
bullets = []

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка движения игрока
    keys = pygame.key.get_pressed()
    player_dx, player_dy = 0, 0
    if keys[pygame.K_LEFT]:
        player_dx = -player_speed
    if keys[pygame.K_RIGHT]:
        player_dx = player_speed
    if keys[pygame.K_UP]:
        player_dy = -player_speed
    if keys[pygame.K_DOWN]:
        player_dy = player_speed

    # Проверка столкновения игрока с препятствиями
    player_rect = pygame.Rect(player_x + player_dx, player_y + player_dy, player_size, player_size)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE)
        if player_rect.colliderect(obstacle_rect):
            player_dx, player_dy = 0, 0
            break  # Прекратить проверку столкновения, если уже произошло

    player_x += player_dx
    player_y += player_dy

    # Ограничение игрока в пределах окна
    player_x = max(0, min(player_x, WINDOW_WIDTH - player_size))
    player_y = max(0, min(player_y, WINDOW_HEIGHT - player_size))

    bullet_speed = 5
    # Обработка стрельбы
    if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(f'mouse_x: {mouse_x}, player_x:{player_x}, mouse_y: {mouse_y}, player_y: {player_y}')
        angle = math.atan2(mouse_y - (player_y + player_size / 2), mouse_x - (player_x + player_size / 2))

        # Используем интерполяцию сплайнами для просчета траектории пули
        t = [0, 1]  # параметр t для интерполяции
        control_points = [(player_x + player_size / 2, player_y + player_size / 2),
                          (mouse_x, mouse_y)]  # начальная и конечная точки
        cs = CubicSpline(t, control_points, bc_type='clamped')  # создаем кубический сплайн

        bullet_x = player_x + player_size / 2
        bullet_y = player_y + player_size / 2
        bullets.append([bullet_x, bullet_y, angle, cs])


    # Перемещение пуль
    bullets_to_remove = []
    for bullet in bullets:
        bullet[0] += bullet_speed * math.cos(bullet[2])
        bullet[1] += bullet_speed * math.sin(bullet[2])

        # Проверка столкновения пуль с препятствиями
        for obstacle in obstacles:
            if pygame.Rect(obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE).collidepoint(bullet[0], bullet[1]):
                bullets_to_remove.append(bullet)

    # Удаление пуль, которые столкнулись с препятствиями
    for bullet in bullets_to_remove:
        bullets.remove(bullet)



    # Заполнение экрана зеленым цветом
    screen.fill(GREEN)

    # Обновление камеры
    camera.center = player_x + player_size // 2, player_y + player_size // 2

    # Отрисовка сетки
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WINDOW_WIDTH, y))

    # Отрисовка препятствий
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE))

    # Отрисовка игрока
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))

    # Отрисовка пуль
    for bullet in bullets:
        pygame.draw.circle(screen, YELLOW, (int(bullet[0]), int(bullet[1])), 3)

    pygame.display.update()

# Завершение Pygame
pygame.quit()
sys.exit()
