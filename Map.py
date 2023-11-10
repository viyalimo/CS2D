import pygame


class Map:
    def __init__(self, num_map):
        self.num_map = num_map
        self.width = None
        self.height = None
        self.tile_size = 32
        self.imbg1 = pygame.image.load('images/обычная трава.png').convert_alpha()
        self.imbg2 = pygame.image.load('images/препятствие.png').convert_alpha()
        # Добавьте здесь код для загрузки карты, тайлов и других параметров.

    def View_world(self, view_world):
        if view_world == 1:
            world = ["                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "              TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBT              ",
                     "              TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT              ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",
                     "                                                                                           ",

                     ]
            map_width = len(world[0]) * self.tile_size
            map_hight = len(world) * self.tile_size
            data = (world, map_width, map_hight,)
        return data

    def DRAWMAP(self, win, camera):
        world = self.View_world(self.num_map)[0]
        tile_Size = 50
        win.fill('black')
        for row in range(len(world)):
            for col in range(len(world[row])):
                x = col * tile_Size
                y = row * tile_Size

                if world[row][col] == 'B':
                    win.blit(self.imbg1, camera.apply(pygame.Rect(x, y, tile_Size, tile_Size)))
                elif world[row][col] == 'T':
                    win.blit(self.imbg2, camera.apply(pygame.Rect(x, y, tile_Size, tile_Size)))
                else:
                    pygame.draw.rect(win, 'blue', camera.apply(pygame.Rect(x, y, tile_Size, tile_Size)))
        return win

    def H_W(self):
        data = (self.View_world(self.num_map)[1], self.View_world(self.num_map)[2])
        return data