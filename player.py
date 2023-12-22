import pygame
from Character import Animation1


class Player:
    def __init__(self, x, y, Direction):
        pygame.init()
        # self.connected = True
        self.tile_size = 45
        self.map_height = 0
        self.map_weight = 0
        self.player_weight = 0
        self.player_height = 0
        self.Direction = Direction
        self.scr_weight = 0
        self.scr_height = 0
        self.start_pos = (750, 400)
        self.x = x
        self.y = y
        self.rect = (x, y)
        self.speed = 15
        self.anim = 0
        self.run = False
        self.anim_surface = None
        self.anim_rect = None
        self.camera_move_x = False
        self.camera_move_y = False
        self.camera_mx = 0
        self.camera_my = 0
        self.coordinateblit = [self.x, self.y]

    def draw(self, win, camera):
        ticreite = pygame.time.Clock()
        self.anim_surface = Animation1(self.Direction)[self.anim]
        self.anim_surface = pygame.transform.scale(self.anim_surface, [65, 90])
        self.anim_rect = self.anim_surface.get_rect()
        self.player_weight = self.anim_rect.width
        self.player_height = self.anim_rect.height
        self.anim_rect.topleft = self.rect
        win.blit(self.anim_surface, self.coordinateblit)

        if self.anim < 3 and self.run:
            self.anim += 1
        else:
            if self.anim == 3:
                self.anim = 0
                self.run = False
        ticreite.tick(20)

    def move(self, camera, obstacles):
        self.anim_surface = Animation1(self.Direction)[self.anim]
        self.anim_rect = self.anim_surface.get_rect()
        now_press = pygame.key.get_pressed()
        player_dx, player_dy = 0, 0
        camera_dx, camera_dy = 0, 0
        # camera_center_x = -self.camera_mx + (self.scr_weight / 2)
        # camera_center_y = -self.camera_my + (self.scr_height / 2)

        if now_press[pygame.K_LEFT] or now_press[pygame.K_a]:
            self.run = True
            self.Direction = "L"
            player_dx -= self.speed
            camera_dx += self.speed

        if now_press[pygame.K_RIGHT] or now_press[pygame.K_d]:
            self.run = True
            self.Direction = 'R'
            player_dx += self.speed
            camera_dx -= self.speed

        if now_press[pygame.K_UP] or now_press[pygame.K_w]:
            self.run = True
            self.Direction = "U"
            player_dy -= self.speed
            camera_dy += self.speed

        if now_press[pygame.K_DOWN] or now_press[pygame.K_s]:
            self.run = True
            self.Direction = "D"
            player_dy += self.speed
            camera_dy -= self.speed

        self.anim_rect = pygame.Rect(self.x + player_dx, self.y + player_dy, self.anim_rect.width, self.anim_rect.height)

        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle[2], obstacle[2])
            if self.anim_rect.colliderect(obstacle_rect):
                player_dx, player_dy = 0, 0
                camera_dx, camera_dy = 0, 0
                break  # Прекратить проверку столкновения, если уже произошло


        if camera.min_x > self.x and camera.min_y > self.y:
            camera_dx = 0
            camera_dy = 0
            self.update_camera_move(self.rect[0], self.rect[1])
            # print('11111111111111')
        elif camera.min_x > self.x and (camera.min_y <= self.y <= camera.max_y):
            camera_dx = 0
            self.update_camera_move(self.rect[0], self.start_pos[1])
            # print('2222222222222')
        elif (camera.min_x <= (self.x ) <= camera.max_x) and camera.min_y > (self.y ):
            camera_dy = 0
            self.update_camera_move(self.start_pos[0], self.rect[1])
            # print('3333333333333')
        elif camera.min_x > self.x and camera.max_y < self.y:
            camera_dx = 0
            camera_dy = 0
            self.update_camera_move(self.rect[0], self.y - (self.map_height - self.scr_height))
            # print('4444444444444')
        elif camera.max_x < self.x and camera.min_y > self.y:
            camera_dx = 0
            camera_dy = 0
            self.update_camera_move(self.x - (self.map_weight - self.scr_weight), self.rect[1])
            # print('5555555555555')
        elif camera.max_x <= self.x and camera.max_y <= self.y:
            camera_dx = 0
            camera_dy = 0
            self.update_camera_move(self.x - (self.map_weight - self.scr_weight), self.y - (self.map_height - self.scr_height))
            # print('6666666666666')
        elif camera.max_x <= self.x and (camera.min_y <= self.y <= camera.max_y):
            camera_dx = 0
            self.update_camera_move(self.x - (self.map_weight - self.scr_weight), self.start_pos[1])
            # print('777777777777')
        elif (camera.min_x <= self.x <= camera.max_x) and camera.max_y < self.y:
            # win.blit(self.anim_surface, (self.start_pos[0], self.rect[1]))
            # camera_dx = self.speed
            camera_dy = 0
            self.update_camera_move(self.start_pos[0], self.y - (self.map_height - self.scr_height))
            # print('888888888888')
        else:
            # win.blit(self.anim_surface, self.start_pos)
            # camera_dx = self.speed
            # camera_dy = self.speed
            self.update_camera_move(self.start_pos[0], self.start_pos[1])
            # print('999999999999')

        camera.x += camera_dx
        camera.y += camera_dy
        self.x += player_dx
        self.y += player_dy
        # print('cameradx', camera_dx, 'camerady', camera_dy)

        self.x = max(self.tile_size, min(self.x, (self.map_weight - 2.5 * self.tile_size)))
        self.y = max(self.tile_size, min(self.y, (self.map_height - 3 * self.tile_size)))
        self.update(camera)

    def update(self, camera):
        self.run = self.run
        self.Direction = self.Direction
        self.anim = self.anim
        self.rect = (self.x, self.y)
        camera.update(camera.x, camera.y)

    def update_camera_move(self, x, y):
        self.coordinateblit[0] = x
        self.coordinateblit[1] = y
        # print(x, y, 'отображение игрока на этич координатах', 'playerx:', self.x, 'playery', self.y)

    def get_map(self, weight, height, tile_size):
        # self.tile_size = tile_size
        self.map_weight = weight
        self.map_height = height

    def get_src(self, weight, height):
        self.scr_weight = weight
        self.scr_height = height
