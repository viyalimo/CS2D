import pygame
from Obstacle import Obstacle
from player import Player


class Map:
    def __init__(self, num_map):
        self.num_map = num_map
        self.width = None
        self.height = None
        self.tile_size = 50
        self.imbg1 = pygame.image.load('images/oh shit.jpg').convert_alpha()
        self.imbg2 = pygame.image.load('images/препятствие.png').convert_alpha()
        self.imbg3 = pygame.image.load('images/обычная трава.png').convert_alpha()
        self.imbg4 = pygame.image.load('images/ground.jpg').convert_alpha()
        self.obstacles = []  # Список для хранения объектов препятствий
        self.player_x = 0
        self.player_y = 0
        self.player_weight = 0
        self.player_height = 0
        self.speed = 10
        self.Direct = "L"
        self.player_Direct = "L"
        self.map_speed = 10
        self.player_rect = pygame.Rect(self.player_x, self.player_y, self.player_weight, self.player_height)

        # Добавьте здесь код для загрузки карты, тайлов и других параметров.

    def View_world(self, view_world):
        if view_world == 1:
            world = ["NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBOOBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBOOBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                     ]
            self.width = len(world[0]) * self.tile_size - 15
            self.height = len(world) * self.tile_size
            data = (world, self.width, self.height,)
        return data

    def DRAWMAP(self, win, camera, player):
        world = self.View_world(self.num_map)[0]
        tile_Size = 50
        win.fill('black')
        for row in range(len(world)):
            for col in range(len(world[row])):
                x = col * tile_Size
                y = row * tile_Size

                if world[row][col] == 'B':
                    tile_rect = pygame.Rect(x, y, tile_Size, tile_Size)
                    shifted_tile_rect = camera.apply(tile_rect)  # Применить сдвиг к тайлу
                    win.blit(self.imbg1, shifted_tile_rect)
                elif world[row][col] == 'T':
                    tile_rect = pygame.Rect(x, y, tile_Size, tile_Size)
                    shifted_tile_rect = camera.apply(tile_rect)  # Применить сдвиг к тайлу
                    win.blit(self.imbg2, shifted_tile_rect)
                elif world[row][col] == 'N':
                    tile_rect = pygame.Rect(x, y, tile_Size, tile_Size)
                    shifted_tile_rect = camera.apply(tile_rect)  # Применить сдвиг к тайлу
                    win.blit(self.imbg4, shifted_tile_rect)
                elif world[row][col] == "O":
                    tile_rect = pygame.Rect(x, y, tile_Size, tile_Size)
                    obstacle = Obstacle(x, y, tile_Size, tile_Size, "Red")
                    shifted_tile_rect = camera.apply(tile_rect)
                    self.obstacles.append(obstacle)  # Добавляем препятствие в список
                    win.blit(self.imbg2, shifted_tile_rect)
                else:
                    pygame.draw.rect(win, 'blue', camera.apply(pygame.Rect(x, y, tile_Size, tile_Size)))
        for obstacle in self.obstacles:
            if player.anim_rect.colliderect(obstacle.rect):
                print("TRUE")
                # Если есть столкновение между игроком и препятствием, установите скорость игрока в ноль
                if player.Direction == "R":  # Если игрок двигается вправо
                    self.Direct = "R"
                    self.player_rect.x = obstacle.rect.left - self.player_rect.width
                elif self.player_Direct == "L":  # Если игрок двигается влево
                    self.speed = 0
                    self.Direct = "L"
                    self.player_rect.x = obstacle.rect.right
                else:
                    self.speed = 10
                if self.player_Direct == "D":  # Если игрок двигается вниз
                    self.speed = 0
                    self.Direct = "D"
                    self.player_rect.y = obstacle.rect.top - self.player_rect.height
                elif self.player_Direct == "U":  # Если игрок двигается вверх
                    self.Direct = "U"
                    self.speed = 0
                    self.player_rect.y = obstacle.rect.bottom
                else:
                    self.speed = 0
        return win

    def H_W(self):
        data = (self.View_world(self.num_map)[1], self.View_world(self.num_map)[2])
        return data

    def get_player(self, player):
        self.player_x = player.x
        self.player_y = player.y
        self.player_weight = player.player_weight
        self.player_height = player.player_height
        self.player_Direct = player.Direction
