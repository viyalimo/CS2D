import pygame

# Инициализация Pygame
pygame.init()

# Размер экрана
screen_width, screen_height = 800, 600

# Размер игровой карты (больше, чем размер экрана)
map_width, map_height = 1600, 1200

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Game with Camera")

# Цвета
green = (0, 255, 0)
black = (0, 0, 0)

# Создание игровой карты (здесь представлена в виде сетки)
tile_size = 32  # Размер тайла
map_grid = [[0 for y in range(map_height // tile_size)] for x in range(map_width // tile_size)]

# Создание игрока
player = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
player_color = (255, 0, 0)
player_speed = 5

# Создание камеры
camera = pygame.Rect(0, 0, screen_width, screen_height)

# Главный цикл игры
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка ввода и движения игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Ограничение игрока в пределах карты
    player.x = max(0, min(player.x, map_width - player.width))
    player.y = max(0, min(player.y, map_height - player.height))

    # Обновление камеры: центрирование камеры на игроке
    camera.center = player.center

    # Ограничение камеры, чтобы не выходила за пределы карты
    camera.x = max(0, min(camera.x, map_width - camera.width))
    camera.y = max(0, min(camera.y, map_height - camera.height))

    # Очистка экрана
    screen.fill(black)

    # Отрисовка видимой области карты (с учетом смещения камеры)
    for x in range(camera.x // tile_size, (camera.x + camera.width) // tile_size + 1):
        for y in range(camera.y // tile_size, (camera.y + camera.height) // tile_size + 1):
            if 0 <= x < len(map_grid) and 0 <= y < len(map_grid[0]):
                pygame.draw.rect(screen, green, pygame.Rect(x * tile_size - camera.x, y * tile_size - camera.y, tile_size, tile_size), 0)
                pygame.draw.rect(screen, black, pygame.Rect(x * tile_size - camera.x, y * tile_size - camera.y, tile_size, tile_size), 1)

    # Отрисовка игрока
    pygame.draw.rect(screen, player_color, player.move(-camera.x, -camera.y))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()