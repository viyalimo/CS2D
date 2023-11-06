import pygame


class Map:
    def __init__(self, height, width, view_world):
        self.height = height
        self.width = width
        self.X = 0
        self.Y = 0
        self.world = self.View_world(view_world)
        self.view_world = view_world
        print(self.world)

    def View_world(self, view_world):
        if view_world == 1:
            world = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ], ]
        return world


w1 = Map(2000, 2000, 1)
